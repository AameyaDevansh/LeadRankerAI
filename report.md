# LeadRankerAI – Caprae AI-Readiness Challenge Report

## Approach
I took a quality-first approach by focusing on replicating and improving the **lead scoring** logic within the 5-hour time constraint. Rather than building another scraper, I built a lightweight tool to **analyze and rank leads**, helping teams prioritize sales or acquisition outreach based on meaningful signals.

## Model Selection
The core of the tool uses a **rule-based scoring function** instead of a machine learning model. This was chosen for speed, transparency, and interpretability — critical when business users need to understand why a lead is ranked highly. The scoring logic weights features like title seniority, industry fit, and AI-readiness signals (e.g., `.ai` domains or “tech” mentions).

## Data Preprocessing
The tool assumes a basic CSV format with fields such as `Title`, `Industry`, and `Website`. These are normalized (e.g., lowercased) and scored using defined heuristics. Missing fields are handled gracefully. The scoring logic is isolated in `scoring.py` and used across the Streamlit app, API, and notebook demo.

## Performance and Testing
While not using ML, the tool is designed for **speed, extensibility, and integration**. The lead scoring runs instantly on thousands of rows. A REST API was added for programmatic access, and a Jupyter notebook allows transparent step-by-step analysis. These features simulate how a real business might integrate the tool into post-acquisition workflows.

## Rationale
Caprae emphasizes **practical AI for post-acquisition growth**. LeadRankerAI reflects that philosophy: it’s usable, testable, and immediately impactful for sales teams or sourcing analysts. In future iterations, this could evolve into a machine learning system trained on real conversion data or enriched via third-party APIs like Apollo or Clearbit.
