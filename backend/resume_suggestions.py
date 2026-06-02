SKILL_WEIGHTS = {
    "python": 20,
    "sql": 15,
    "git": 10,
    "github": 10,
    "react": 15,
    "javascript": 10,
    "machine learning": 25,
    "deep learning": 25
}

JOB_PROFILES = {
    "Python Developer": ["python", "sql", "git"],
    "Frontend Developer": ["react", "javascript", "html", "css"],
    "Data Scientist": ["python", "machine learning", "sql"],
    "Software Developer": ["git", "github", "python", "java"]
}


def calculate_ats(found_skills):
    score = 0
    for skill in found_skills:
        score += SKILL_WEIGHTS.get(skill, 5)
    return min(score, 100)


def get_missing_skills(found_skills):
    all_skills = set(SKILL_WEIGHTS.keys())
    return list(all_skills - set(found_skills))


def recommend_jobs(found_skills):
    job_scores = {}

    for job, skills in JOB_PROFILES.items():
        match = len(set(found_skills) & set(skills))
        score = int((match / len(skills)) * 100)
        job_scores[job] = score

    sorted_jobs = sorted(job_scores.items(), key=lambda x: x[1], reverse=True)

    return [job for job, score in sorted_jobs if score > 30] or ["Software Engineer"]