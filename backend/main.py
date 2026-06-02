from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import pdf_reader
import skill_extractor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- SKILLS ----------------
SKILLS = [
    "python", "java", "sql", "html", "css",
    "javascript", "react", "node", "mongodb",
    "git", "github", "machine learning", "deep learning"
]

# ---------------- ATS (SMART VERSION) ----------------
def calculate_ats(found_skills, text):
    if not found_skills:
        return 10

    base = (len(found_skills) / len(SKILLS)) * 70
    bonus = 0

    text_lower = text.lower()

    if "project" in text_lower:
        bonus += 10
    if "experience" in text_lower:
        bonus += 10
    if "intern" in text_lower:
        bonus += 5
    if len(text) > 1000:
        bonus += 5

    score = base + bonus
    return min(int(score), 100)


# ---------------- JOBS ----------------
def recommend_jobs(found_skills):
    jobs = []

    if "python" in found_skills:
        jobs.append("Python Developer")

    if "react" in found_skills:
        jobs.append("Frontend Developer")

    if "sql" in found_skills:
        jobs.append("Data Analyst")

    if "git" in found_skills:
        jobs.append("Software Developer")

    return jobs or ["Software Engineer"]


# ---------------- MISSING SKILLS ----------------
def get_missing_skills(found_skills):
    return [s for s in SKILLS if s not in found_skills]


# ---------------- API ----------------
@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):

    pdf_bytes = await file.read()

    text = pdf_reader.extract_text(pdf_bytes)

    found_skills = skill_extractor.extract_skills(text)

    return {
        "ats_score": calculate_ats(found_skills, text),
        "skills_found": found_skills,
        "missing_skills": get_missing_skills(found_skills),
        "recommended_jobs": recommend_jobs(found_skills)
    }