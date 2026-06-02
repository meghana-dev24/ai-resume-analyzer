from fastapi import FastAPI, UploadFile, File
from pdf_reader import extract_text_from_pdf
from pdf_reader import extract_text_from_pdf
from skill_extractor import extract_skills
from skill_extractor import (
    extract_skills,
    get_missing_skills,
    recommend_jobs
)
import shutil

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Resume Analyzer API Running"}

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    filepath = f"uploads/{file.filename}"

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "saved_to": filepath,
        "status": "uploaded successfully"
    }
@app.get("/read-pdf")
def read_pdf():

    pdf_path = "uploads/8_Biology_SEM-1_Textbook.pdf"

    text = extract_text_from_pdf(pdf_path)

    return {
        "text": text[:1000]
    }
@app.get("/analyze-resume")
def analyze_resume():

    pdf_path = "uploads/8_Biology_SEM-1_Textbook.pdf"

    text = extract_text_from_pdf(pdf_path)

    skills = extract_skills(text)

    missing_skills = get_missing_skills(skills)

    recommended_jobs = recommend_jobs(skills)

    ats_score = min(len(skills) * 20, 100)

    return {
        "skills_found": skills,
        "missing_skills": missing_skills,
        "recommended_jobs": recommended_jobs,
        "total_skills": len(skills),
        "ats_score": ats_score
    }