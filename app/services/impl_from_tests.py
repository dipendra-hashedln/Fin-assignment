import os
import glob
import json
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
    model_name="llama3-70b-8192"
)

def generate_code_for_test(test_code: str, aim_json: dict) -> str:
    prompt = f"""
You are a FastAPI backend developer.

Below is a pytest unit test. Your task is to generate minimal working implementation code to pass this test.

Requirements:
- Use Pydantic for request/response models
- Implement FastAPI route handler
- Add a dummy service class/method if needed
- Output only Python code. No explanations. No markdown. No headings. No code blocks. No triple quotes.

Test:
{test_code}
"""
    response = llm.invoke(prompt)
    return response.content if hasattr(response, "content") else str(response)

def clean_code(raw: str) -> str:
    # Remove markdown preambles like "**main.py**", etc.
    raw = re.sub(r"\*\*.*?\*\*", "", raw)
    raw = re.sub(r"Here is.*?:", "", raw, flags=re.IGNORECASE)

    # Remove code fences and triple quotes
    raw = re.sub(r"```(?:python)?", "", raw)
    raw = re.sub(r"```", "", raw)
    raw = re.sub(r'"""', "", raw)
    raw = re.sub(r"'''", "", raw)

    return raw.strip()

def main():
    aim_path = "generated_project/utils/aim.json"
    tests_path = "generated_project/tests"
    services_path = "generated_project/app/services"

    os.makedirs(services_path, exist_ok=True)

    with open(aim_path, "r", encoding="utf-8") as f:
        aim = json.load(f)

    test_files = glob.glob(f"{tests_path}/test_*.py")

    for i, test_file in enumerate(test_files, start=1):
        with open(test_file, "r", encoding="utf-8") as f:
            test_code = f.read()

        print(f"Generating code from: {os.path.basename(test_file)}")

        raw_code = generate_code_for_test(test_code, aim)
        clean = clean_code(raw_code)

        filename = f"impl_from_test_{i}.py"
        filepath = os.path.join(services_path, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(clean)

        print(f"Saved: {filename}")

    print("Implementation generation complete.")

if __name__ == "__main__":
    main()


