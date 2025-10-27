# AI-Resume-Job-Match-Analyzer

This project is a Streamlit-based web application that analyzes a candidate’s resume and a job description to calculate their compatibility score using text similarity techniques. It provides insights into how well a resume aligns with a job role and highlights areas of improvement for better job targeting.

🚀 **Features**
- Resume Upload: Accepts resumes in .docx format.
- Job Description Upload: Allows job description upload or manual input.
- Automated Matching: Uses TF-IDF vectorization and cosine similarity to compute a match score.
- Instant Results: Provides overall match percentage, skills overlap, and recommendations.
- Simple UI: Minimal, responsive Streamlit interface for easy interaction.

🧠 **Tech Stack**
- Frontend: Streamlit
- Backend: Python
- Libraries Used:
- streamlit – Web interface
- scikit-learn – TF-IDF Vectorizer & Cosine Similarity
- python-docx – Resume content extraction
- re – Text cleaning & preprocessing

⚙️ **Installation**

1. Clone this repository:
```
git clone https://github.com/<your-username>/resume-job-matcher.git
cd resume-job-matcher
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the app:
```
streamlit run app.py
```
4. Access locally at:
```
http://localhost:8501
```

📊 **Output Example**
- After uploading your resume and job description, the app instantly provides:
- Match Score: 0–100% alignment based on text similarity.
- Skill Overlap: Key matching skills between resume and job description.
- Suggestions: Specific missing keywords to add for better relevance.

🧭 **Future Improvements**
- Support for PDF resumes.
- Integration with NLP models like BERT for semantic understanding.
- Keyword-based resume optimization tips.
- Option to export report as PDF.

🧑‍💼 **Ideal For**
Job seekers looking to tailor their resumes for specific job descriptions.
Recruiters aiming for quick candidate-job fit assessment.
Career portals enhancing AI-driven resume screening.
