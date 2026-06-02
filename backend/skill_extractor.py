SKILLS = [
    "python",
    "java",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "node",
    "mongodb",
    "git",
    "github",
    "machine learning",
    "deep learning"
]

REQUIRED_SKILLS = [
    "python",
    "sql",
    "git",
    "github",
    "react"
]

def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills

def get_missing_skills(found_skills):
    missing_skills = []

    for skill in REQUIRED_SKILLS:
        if skill not in found_skills:
            missing_skills.append(skill)

    return missing_skills
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

    return jobs