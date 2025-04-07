from models.phishing_model import classify_message
from app.url_utils import extract_urls, check_url_safety
from app.heuristics import run_heuristics

def analyze_message(text, api_key):
    urls = extract_urls(text)
    dangerous = [url for url in urls if check_url_safety(url, api_key)]
    heuristic_flags = run_heuristics(text, urls)

    label, confidence = classify_message(text)

    trust = 100
    if label == "spam" and confidence > 0.6:
        trust -= 30
    if dangerous:
        trust -= 40
    if heuristic_flags:
        trust -= len(heuristic_flags) * 10

    return {
        "verdict": "⚠️ Potential Phishing!" if trust <= 70 else "✅ Safe Message",
        "phishing_confidence": round(confidence, 2),
        "trust_score": trust,
        "heuristic_flags": heuristic_flags,
        "urls_found": urls,
        "dangerous_urls": dangerous,
    }
