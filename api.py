from fastapi import FastAPI, Request
from pydantic import BaseModel
from scoring import score_lead

app = FastAPI()

class Lead(BaseModel):
    title: str
    industry: str
    website: str
    company: str

@app.post("/score")
def get_score(lead: Lead):
    score = score_lead(
        lead.title,
        lead.industry,
        lead.website
    )
    return {"lead_score": score}
