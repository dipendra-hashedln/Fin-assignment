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
    if result.returncode == 0:
        print("✅ All tests passed!")
        return True
    else:
        print("❌ Some tests failed.")
        return False

if __name__ == "__main__":
    create_virtualenv()
    install_requirements()
    run_pytest()


