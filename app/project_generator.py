import os
import shutil

def create_project_structure(project_root="generated_project"):
    if os.path.exists(project_root):
        shutil.rmtree(project_root)

    folders = [
        f"{project_root}/app/api/routes",
        f"{project_root}/app/models",
        f"{project_root}/app/services",
        f"{project_root}/tests",
        f"{project_root}/utils"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    files = {
        f"{project_root}/app/database.py": "",
        f"{project_root}/app/main.py": "",
        f"{project_root}/Dockerfile": "",
        f"{project_root}/requirements.txt": "fastapi\nhttpx\npydantic\npytest\n",
        f"{project_root}/.env": "",
        f"{project_root}/README.md": ""
    }

    for path, content in files.items():
        with open(path, "w") as f:
            f.write(content)

    print(f"📂 Project folder '{project_root}' created with initial files.")
    return project_root
