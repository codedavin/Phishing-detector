def run_heuristics(text, urls):
    flags = []
    risky_words = ["verify", "urgent", "click", "login", "reset"]
    shorteners = ["bit.ly", "tinyurl", "t.co"]

    for word in risky_words:
        if word in text.lower():
            flags.append(f"Suspicious keyword: {word}")

    for url in urls:
        if any(short in url for short in shorteners):
            flags.append("Shortened URL: " + url)

    return flags
