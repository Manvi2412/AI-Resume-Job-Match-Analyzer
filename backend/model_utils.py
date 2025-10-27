import docx2txt
import re
from difflib import SequenceMatcher

def extract_text_from_resume(file_path):
    text = ""
    if file_path.endswith(".pdf"):
        from PyPDF2 import PdfReader
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
    elif file_path.endswith(".docx"):
        text = docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file format")
    return text

def clean_text(text):
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.lower()

def get_match_score(resume_text, job_description):
    resume_words = set(resume_text.split())
    jd_words = set(job_description.split())
    common = resume_words.intersection(jd_words)
    if len(jd_words) == 0:
        return 0
    return round(len(common) / len(jd_words) * 100, 2)

def get_missing_skills(resume_text, job_description):
    jd_words = set(job_description.split())
    resume_words = set(resume_text.split())
    missing = jd_words - resume_words
    return list(missing)[:10]  # top 10 missing keywords

def generate_summary(resume_text, job_description):
    similarity = SequenceMatcher(None, resume_text, job_description).ratio()
    if similarity > 0.75:
        return "Your resume is highly aligned with the job description!"
    elif similarity > 0.5:
        return "Your resume is moderately aligned. Add more relevant skills and experience."
    else:
        return "Your resume has low alignment. Tailor your content to match the job role."

def analyze_resume(file_path, job_description):
    resume_text = extract_text_from_resume(file_path)
    resume_text = clean_text(resume_text)
    jd_text = clean_text(job_description)

    match_score = get_match_score(resume_text, jd_text)
    missing_skills = get_missing_skills(resume_text, jd_text)
    summary = generate_summary(resume_text, jd_text)

    return {
        "match_score": match_score,
        "missing_skills": missing_skills,
        "summary": summary
    }
