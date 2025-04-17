import os
import json
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), temperature=0, model_name="llama3-70b-8192")

def generate_test_code(endpoint: dict) -> str:
    method = endpoint.get("method", "GET")
    path = endpoint.get("path", "/unknown")
    description = endpoint.get("description", "No description provided.")

    prompt = f"""
    You are a FastAPI test engineer.

    Write a pytest unit test using HTTPX TestClient for this endpoint:
    - Method: {method}
    - Path: {path}
    - Description: {description}

    Requirements:
    - Use TestClient from fastapi.testclient
    - Import the app from 'from app.main import app'
    - Include a status code assertion
    - Return only runnable Python code (no markdown, no triple quotes, no text)
    """

    response = llm.invoke(prompt)
    raw = response.content if hasattr(response, "content") else str(response)

    # Clean markdown if any
    match = re.search(r"```(?:python)?\s*(.*?)```", raw, re.DOTALL)
    return match.group(1).strip() if match else raw.strip()

def main():
    aim_path = "generated_project/utils/aim.json"
    output_dir = "generated_project/tests"
    os.makedirs(output_dir, exist_ok=True)

    with open(aim_path, "r", encoding="utf-8") as f:
        aim = json.load(f)

    test_files = []
    for i, endpoint in enumerate(aim.get("api_endpoints", []), start=1):
        test_code = generate_test_code(endpoint)
        filename = f"test_{i}.py"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(test_code)

        test_files.append(filename)
        print(f"✅ Generated: {filename}")

    print(f"\n🎯 {len(test_files)} test files created in {output_dir}/")

if __name__ == "__main__":
    main()


