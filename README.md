# LeadRankerAI

A lightweight, AI-inspired lead scoring tool designed to help post-acquisition teams quickly prioritize high-value leads. Built in response to Caprae Capital’s AI-Readiness Challenge.

---

## Overview

**LeadRankerAI** takes a basic CSV of leads and assigns a 0–100 score based on:
- Title seniority
- Industry match
- AI/tech-forward domain hints (e.g., `.ai`, “tech”)
- Optional: company name metadata

This enables sales teams or acquisition analysts to:
- Filter promising leads
- Focus outreach efforts
- Minimize manual vetting

---

## Project Structure

```bash
├── app.py                  # Streamlit app
├── scoring.py              # Rule-based scoring logic
├── api.py                  # FastAPI endpoint for programmatic access
├── LeadRankerAI_demo.ipynb # Jupyter Notebook demo
├── sample_data.csv         # Sample input leads
├── requirements.txt
└── README.md
```

## How to Run
### 1. Streamlit UI
```bash
streamlit run app.py
```
Upload any .csv with columns like Title, Industry, Website, and get a downloadable scored file.

### 2. Notebook Demo
Open the notebook in Jupyter or VS Code:
```bash
jupyter notebook LeadRankerAI_demo.ipynb
```
- Walkthrough of input → scoring → visual output → export
- Ideal for experimentation or demo review

### 3. REST API
```bash
uvicorn api:app --reload
```
Then call the endpoint:
```bash
curl -X POST http://127.0.0.1:8000/score \
     -H "Content-Type: application/json" \
     -d '{"title":"CEO","industry":"FinTech","website":"fintechly.com","company":"Fintechly"}'
```
Returns:
```bash
{"lead_score": 70}
```
Or visit Swagger UI at http://127.0.0.1:8000/docs for interactive testing.

## Next Steps
This project is designed as a minimal but extensible base.

**Future additions might include:**

- ML-based scoring using historical conversion data
- API enrichment from Clearbit or Apollo
- Smart deduplication or CRM-ready exports
- Signals from job posts, LinkedIn, or intent data

## Submission Notes
- Name: Aameya Devansh
- Time constraint: Capped at ~5 hours of coding
- Approach: Quality-first — focused on scoring logic, multi-modal demos, and clean structure
- Tech stack: Python · Streamlit · FastAPI · Pandas




