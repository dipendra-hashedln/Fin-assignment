import os
import zipfile

def zip_project(project_path: str) -> str:
    """
    Zip the given project folder and return the path to the zip file.
    """
    zip_name = os.path.basename(project_path.rstrip("/\\"))
    zip_path = f"generated_projects/{zip_name}.zip"
    os.makedirs("generated_projects", exist_ok=True)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(project_path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, start=project_path)
                zipf.write(full_path, arcname=rel_path)

    return zip_path


