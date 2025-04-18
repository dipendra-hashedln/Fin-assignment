from docx import Document

def extract_text_from_docx(docx_path: str) -> str:
    """
    Extract all text from a .docx file and return as a single string.
    """
    doc = Document(docx_path)
    full_text = [para.text.strip() for para in doc.paragraphs if para.text.strip()]
    return "\n".join(full_text)


