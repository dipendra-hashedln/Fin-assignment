import os
import subprocess
import sys
import time

PROJECT_DIR = "generated_project"
VENV_DIR = os.path.join(PROJECT_DIR, "venv")
PYTHON_EXEC = os.path.join(VENV_DIR, "Scripts", "python.exe") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
REQUIREMENTS_PATH = os.path.join(PROJECT_DIR, "requirements.txt")
TESTS_DIR = os.path.join(PROJECT_DIR, "tests")

def create_virtualenv():
    print("🐍 Creating virtualenv...")
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
    print("✅ Virtualenv created at:", VENV_DIR)

def write_default_requirements():
    print("📝 Writing default requirements.txt...")
    with open(REQUIREMENTS_PATH, "w") as f:
        f.write("fastapi\npytest\npydantic\n")

def install_requirements():
    if not os.path.exists(REQUIREMENTS_PATH):
        write_default_requirements()

    print("📦 Installing dependencies from requirements.txt...")
    subprocess.run([PYTHON_EXEC, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([PYTHON_EXEC, "-m", "pip", "install", "-r", REQUIREMENTS_PATH], check=True)
    print("✅ Dependencies installed.")

def run_pytest() -> bool:
    print("🧪 Running tests...")
    result = subprocess.run([PYTHON_EXEC, "-m", "pytest", TESTS_DIR], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    return result.returncode == 0

def regenerate_code():
    print("🔁 Regenerating code using impl_from_tests.py...")
    subprocess.run([sys.executable, "app/services/impl_from_tests.py"])

def main() -> bool:
    create_virtualenv()
    install_requirements()

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        if run_pytest():
            print(f"🎉 Tests passed after {attempt} attempt(s).")
            return True
        print(f"🔄 Attempt {attempt} failed. Retrying code generation...")
        regenerate_code()
        time.sleep(1)

    print("❌ All retries exhausted. Some tests are still failing.")
    return False

if __name__ == "__main__":
    main()


