import os
import subprocess
import sys
import time
import glob

PROJECT_DIR = "generated_project"
VENV_DIR = os.path.join(PROJECT_DIR, "venv")
PYTHON_EXEC = os.path.join(VENV_DIR, "Scripts", "python.exe") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
REQUIREMENTS_PATH = os.path.join(PROJECT_DIR, "requirements.txt")
TESTS_DIR = os.path.join(PROJECT_DIR, "tests")
IMPL_GENERATOR = ["python", "app/services/impl_from_tests.py"]

def create_virtualenv():
    print("🐍 Creating virtualenv...")
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
    print("✅ Virtualenv created at:", VENV_DIR)

def install_requirements():
    if not os.path.exists(REQUIREMENTS_PATH):
        print("⚠️  No requirements.txt found. Skipping install.")
        return
    print("📦 Installing dependencies from requirements.txt...")
    subprocess.run([PYTHON_EXEC, "-m", "pip", "install", "-r", REQUIREMENTS_PATH], check=True)
    print("✅ Dependencies installed.")

def run_pytest() -> bool:
    print("🧪 Running tests...")
    result = subprocess.run([PYTHON_EXEC, "-m", "pytest", TESTS_DIR], capture_output=True, text=True)

    print(result.stdout)
    print(result.stderr)

    if result.returncode == 0:
        print("✅ All tests passed!")
        return True
    else:
        print("❌ Tests failed with errors above.")
        return False

def regenerate_code():
    print("🔁 Regenerating code using impl_from_tests.py...")
    subprocess.run([sys.executable, "app/services/impl_from_tests.py"])




def main() -> bool:
    create_virtualenv()
    install_requirements()

    max_retries = 3
    attempt = 0

    while attempt < max_retries:
        passed = run_pytest()
        if passed:
            break
        attempt += 1
        print(f"🔄 Attempt {attempt} failed. Retrying code generation...")
        regenerate_code()
        time.sleep(2)

    if attempt == max_retries:
        print("❌ All retries exhausted. Some tests are still failing.")
        return False   # ✅ Instead of sys.exit(1)
    else:
        print(f"🎉 Tests passed after {attempt + 1} total attempts.")
        return True     # ✅ explicitly return success





