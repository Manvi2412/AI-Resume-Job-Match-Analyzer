from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from model_utils import analyze_resume
import shutil
import os

app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze_resume")
async def analyze_resume_endpoint(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    temp_path = f"temp_{resume.filename}"

    # Save uploaded resume temporarily
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    try:
        result = analyze_resume(temp_path, job_description)
    except Exception as e:
        return {"error": str(e)}
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return result


@app.get("/")
def home():
    return {"message": "Backend is running successfully!"}
