
from fastapi import FastAPI, UploadFile, File
from app.srs_parser import analyze_srs
from app.project_generator import create_project_structure
import os
import shutil
from docx import Document

app = FastAPI()

@app.post("/upload-srs")
async def upload_srs(file: UploadFile = File(...)):
    if not file.filename.endswith(".docx"):
        return {"error": "Only .docx files are supported."}

    os.makedirs("out", exist_ok=True)
    docx_path = os.path.join("out", file.filename)
    with open(docx_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Extract raw text from .docx
    doc = Document(docx_path)
    raw_text = "\n".join([para.text for para in doc.paragraphs])
    text_path = os.path.join("out", "srs_text.txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(raw_text)

    # Step 1: Scaffold project folders
    project_path = "generated_project"
    create_project_structure(project_path)

    # Step 2: Analyze SRS and write aim.json
    aim_path = analyze_srs(text_path, project_path)

    return {
        "message": "Project generated successfully",
        "aim_json_path": aim_path,
        "project_folder": project_path
    }

