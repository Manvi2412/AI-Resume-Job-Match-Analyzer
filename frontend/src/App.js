import React, { useState } from "react";
import "./App.css";

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!resumeFile || !jobDescription) {
      alert("Please upload a resume and enter a job description!");
      return;
    }

    const formData = new FormData();
    formData.append("resume", resumeFile);
    formData.append("job_description", jobDescription);

    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:8000/analyze_resume", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
      alert("Error analyzing resume.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>AI-Powered Resume & Job Match Analyzer</h1>
      <form onSubmit={handleSubmit}>
        <label>Upload Resume (.pdf/.docx):</label>
        <input
          type="file"
          accept=".pdf,.docx"
          onChange={(e) => setResumeFile(e.target.files[0])}
        />

        <label>Paste Job Description:</label>
        <textarea
          placeholder="Paste the job description here..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        />

        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </form>

      {result && (
        <div className="results">
          <h2>Results:</h2>
          <p>
            <strong>Match Score:</strong> {result.match_score}%
          </p>
          <p>
            <strong>Missing Keywords:</strong>{" "}
            {result.missing_skills.join(", ") || "None 🎉"}
          </p>
          <p>
            <strong>Summary:</strong> {result.summary}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
