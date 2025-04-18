from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.pipeline.orchestrator import run_full_generation
import os

app = FastAPI()

@app.post("/upload-srs")
async def upload_srs(file: UploadFile = File(...)):
    if not file.filename.endswith(".docx"):
        raise HTTPException(400, "Only .docx files are supported.")
    
    os.makedirs("temp", exist_ok=True)
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        zip_path = run_full_generation(file_path)
    except Exception as e:
        raise HTTPException(500, f"Generation failed: {str(e)}")

    return FileResponse(zip_path, filename=os.path.basename(zip_path))

