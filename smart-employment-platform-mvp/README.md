
# Smart Employment Platform (MVP)

A minimal prototype for **Nizam Al-Tawtheef Al-Thaki** — an AI-guided employment and future-skills platform.

## Structure
```
smart-employment-platform/
├── backend/            # Flask API (Python)
├── frontend/           # Static web (HTML/JS/CSS)
├── data/               # Sample data
├── .gitignore
├── LICENSE
└── README.md
```

## Quickstart (Local)

### 1) Backend (Flask)
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
By default the API runs on: `http://127.0.0.1:5001`

### 2) Frontend (Static)
Open `frontend/index.html` directly in your browser, or serve it via any static server.

## GitHub: How to Create & Push
1. Create a new repo on GitHub (no files necessary).
2. Locally:
```bash
git init
git remote add origin https://github.com/USER/REPO.git
git add .
git commit -m "Initial MVP"
git branch -M main
git push -u origin main
```
Replace `USER/REPO` with your GitHub path.

## API Endpoints (Mocked)
- `POST /api/score_cv` → returns a fake ATS score and improvement tips.
- `POST /api/recommend_jobs` → returns job matches based on skills.
- `GET /api/insights` → government-style mock insights.
- `POST /api/match_candidates` → employer view of matched candidates.

> These are mocked to help you demo the UX now. You can later connect real models & data.
