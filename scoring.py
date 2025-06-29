from typing import List
from fuzzywuzzy import fuzz  

# -------------- configurable lists ------------------
SENIOR = ["chief", "ceo", "cto", "cmo", "cfo", "coo", "president", "founder"]
VP     = ["vp", "vice president"]
DIRECTOR = ["director", "head"]
IC_NEG = ["intern", "assistant", "junior", "student"]

FUNC_RELEVANT = ["product", "engineering", "operations", "finance", "growth", "strategy"]

INDUSTRIES = [
    "saas", "software", "fintech", "finance", "ai", "artificial intelligence",
    "machine learning", "healthtech", "healthcare", "medtech", "data"
]

MODERN_TLDS = [".ai", ".io", ".cloud", ".tech"]

FREE_EMAIL_DOMAINS = ["gmail.com", "outlook.com", "yahoo.com", "hotmail.com"]

# ----------------------------------------------------

def _title_matches(title: str, keywords: List[str]) -> bool:
    t = title.lower()
    return any(k in t for k in keywords)

def _fuzzy_match(term: str, vocab: List[str], threshold: int = 85) -> bool:
    return any(fuzz.token_set_ratio(term.lower(), v) >= threshold for v in vocab)

def score_lead(title: str = "", industry: str = "", website: str = "", company: str = "") -> int:
    """
    Multi‑factor rule‑based lead scoring (0‑100).
    """
    score = 0
    t = (title or "").lower()

    # 1️⃣ Seniority
    if _title_matches(t, SENIOR):
        score += 40
    elif _title_matches(t, VP):
        score += 30
    elif _title_matches(t, DIRECTOR):
        score += 15
    elif _title_matches(t, IC_NEG):
        score -= 10
    else:
        score += 5

    # 2️⃣ Function relevance
    if _title_matches(t, FUNC_RELEVANT):
        score += 10

    # 3️⃣ Industry fit (fuzzy)
    if industry and _fuzzy_match(industry, INDUSTRIES):
        score += 30

    # 4️⃣ Domain / TLD heuristics
    if website:
        site = website.lower()
        if any(site.endswith(tld) for tld in MODERN_TLDS):
            score += 10
        if any(free in site for free in FREE_EMAIL_DOMAINS):
            score -= 20

    # 5️⃣ AI / ML keyword boost
    site_or_company = f"{website} {company}".lower()
    if any(k in site_or_company for k in [" ai", " ml", "data", "analytics"]):
        score += 10

    return max(0, min(score, 100))
