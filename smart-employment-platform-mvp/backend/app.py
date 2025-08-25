
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- Mock Data ---
SAMPLE_JOBS = [
    {"id": 1, "title": "Data Analyst", "city": "Riyadh", "skills": ["SQL", "Excel", "Python"], "sector": "Tech"},
    {"id": 2, "title": "HR Specialist", "city": "Jeddah", "skills": ["Communication", "ATS", "Excel"], "sector": "HR"},
    {"id": 3, "title": "Frontend Developer", "city": "Khobar", "skills": ["JavaScript", "React", "HTML", "CSS"], "sector": "Tech"}
]

INSIGHTS = {
    "top_sectors": [{"name": "Tech", "demand_index": 88}, {"name": "Healthcare", "demand_index": 75}, {"name": "Logistics", "demand_index": 62}],
    "top_cities": [{"name": "Riyadh", "jobs": 1200}, {"name": "Jeddah", "jobs": 800}, {"name": "Khobar", "jobs": 450}],
    "future_skills": ["AI Literacy", "Data Analysis", "Cloud Basics", "Cybersecurity Awareness"]
}

@app.route("/api/score_cv", methods=["POST"])
def score_cv():
    data = request.get_json(force=True, silent=True) or {}
    text = (data.get("text") or "")[:10000]
    # Toy scoring: length/keywords
    keywords = ["project", "experience", "achievements", "python", "excel", "react"]
    score = min(100, 40 + len(text)//200 + sum(k in text.lower() for k in keywords)*8)
    tips = [
        "Add measurable achievements (numbers, %, KPIs).",
        "Use standard section titles: Summary, Experience, Education, Skills.",
        "Include keywords from the job description to improve ATS matching."
    ]
    return jsonify({"score": int(score), "tips": tips})

@app.route("/api/recommend_jobs", methods=["POST"])
def recommend_jobs():
    data = request.get_json(force=True, silent=True) or {}
    skills = set([s.strip() for s in data.get("skills", []) if s])
    results = []
    for job in SAMPLE_JOBS:
        overlap = len(skills.intersection(set(job["skills"])))
        match = int( (overlap / max(1, len(job["skills"])) ) * 100 )
        results.append({**job, "match": match})
    results.sort(key=lambda x: x["match"], reverse=True)
    return jsonify({"jobs": results[:5]})

@app.route("/api/insights", methods=["GET"])
def insights():
    return jsonify(INSIGHTS)

@app.route("/api/match_candidates", methods=["POST"])
def match_candidates():
    data = request.get_json(force=True, silent=True) or {}
    requirements = set([s.strip() for s in data.get("requirements", []) if s])
    # Mocked candidates
    candidates = [
        {"name": "Aisha", "skills": ["SQL", "Excel", "Python"], "city": "Riyadh"},
        {"name": "Mzoon", "skills": ["Communication", "ATS", "Excel"], "city": "Jeddah"},
        {"name": "Raghad", "skills": ["JavaScript", "React", "HTML", "CSS"], "city": "Khobar"},
    ]
    for c in candidates:
        overlap = len(requirements.intersection(set(c["skills"])))
        c["match"] = int( (overlap / max(1, len(requirements))) * 100 )
    candidates.sort(key=lambda x: x["match"], reverse=True)
    return jsonify({"candidates": candidates})

if __name__ == "__main__":
    app.run(port=5001, debug=True)
