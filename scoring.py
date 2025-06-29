# scoring.py
def score_lead(title: str, industry: str, website: str) -> int:
    """
    Simple rule‑based lead scoring.
    Returns an integer 0‑100.
    """
    score = 0

    # Seniority/title
    senior_titles = ["ceo", "cto", "founder", "president"]
    mid_titles = ["vp", "head", "director", "manager"]
    low_titles = ["intern", "assistant"]

    t = (title or "").lower()
    if any(k in t for k in senior_titles):
        score += 40
    elif any(k in t for k in mid_titles):
        score += 25
    elif any(k in t for k in low_titles):
        score += 5
    else:
        score += 10

    # Industry match (tweak for Caprae’s focus)
    target_industries = ["saas", "ai", "software", "fintech", "healthcare"]
    if industry and industry.lower() in target_industries:
        score += 30

    # Tech‑forward domain hint
    if website and (website.endswith(".ai") or "tech" in website):
        score += 20

    return min(score, 100)
