import os
import json
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), temperature=0, model_name="llama3-70b-8192")

def analyze_srs_content(text: str) -> dict:
    prompt = f"""
    Parse the provided Software Requirements Specification and generate structured JSON containing: - api_endpoints: array of endpoints including method, path, and description - database_schema: tables with their columns and relationships - business_rules: textual rules and logic to enforce - auth_requirements: roles, authentication mechanisms, and related details. Output only valid JSON, ensuring it is parsable by Python's json.loads(). Exclude markdown, comments, or explanations.

    SRS:
    {text}
    """

    try:
        response = llm.invoke(prompt)
        raw_response = response.content if hasattr(response, "content") else str(response)

        # Try normal JSON parse first
        return json.loads(raw_response)

    except json.JSONDecodeError:
        # Fallback: try to extract JSON from messy output
        match = re.search(r'\{.*\}', raw_response, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            return {
                "error": "❌ Failed to parse JSON from model response",
                "raw_response": raw_response
            }

def analyze_srs(text_path: str, project_root: str) -> str:
    with open(text_path, "r", encoding="utf-8") as f:
        srs_text = f.read()

    parsed_json = analyze_srs_content(srs_text)

    aim_dir = os.path.join(project_root, "utils")
    os.makedirs(aim_dir, exist_ok=True)

    aim_path = os.path.join(aim_dir, "aim.json")
    with open(aim_path, "w", encoding="utf-8") as f:
        json.dump(parsed_json, f, indent=2)

    print("aim.json saved at:", aim_path)
    return aim_path



