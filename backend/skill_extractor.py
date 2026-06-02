SKILLS = [
    "python", "java", "sql", "html", "css",
    "javascript", "react", "node", "mongodb",
    "git", "github", "machine learning", "deep learning"
]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS if skill in text]