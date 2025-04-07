import re
import requests

def extract_urls(text):
    return re.findall(r'(https?://\S+|www\.\S+)', text)

def check_url_safety(url, api_key):
    endpoint = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
    payload = {
        "client": {"clientId": "phishing-detector", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    try:
        res = requests.post(f"{endpoint}?key={api_key}", json=payload)
        return bool(res.json().get("matches"))
    except:
        return False
