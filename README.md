
# 🛡️ AI-Powered Phishing Detector

An advanced phishing and spam detection app built with **Streamlit**, **Transformers**, and **LangChain + Groq LLaMA3 70B**. This app analyzes text messages or emails, extracts URLs, checks for phishing patterns using heuristics, verifies links via the Google Safe Browsing API, and provides both a model prediction and an LLM explanation.

---

## 🚀 Features

- 📩 **Message Analysis**: Classifies input as *Safe*, *Spam*, or *Phishing*
- 🌐 **URL Extraction & Safety Check**: Detects and verifies embedded links
- 🧠 **LLM-Powered Explanation**: Generates human-like reasoning with LLaMA3 via Groq API
- ⚠️ **Heuristics Engine**: Flags suspicious patterns (e.g. urgency, shortened links)
- 📊 **Trust Score System**: Weighted scoring based on various detection layers

---

## 🗂️ Project Structure

```
Phishing_detector/
├── app/
│   ├── __init__.py
│   ├── ui.py                # Streamlit UI logic
│   ├── detector.py          # Core phishing detection engine
│   ├── heuristics.py        # Heuristic pattern detection
│   └── explain.py           # LangChain LLM explanation module
├── models/
│   ├── __init__.py
│   └── phishing_model.py    # RoBERTa-based spam/phishing classifier
├── .env                     # Environment variables (keys)
├── requirements.txt         # Python dependencies
├── run.py                   # App entry point
└── README.md                # You're reading it :)
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/codedavin/phishing-detector.git
cd phishing-detector
```

### 2. Install Dependencies
Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

Then install required packages:
```bash
pip install -r requirements.txt
```

### 3. Add API Keys to `.env`
Create a `.env` file in the root directory with the following:

```env
GROQ_API_KEY=your_groq_api_key_here
SAFE_BROWSING_API_KEY=your_google_safe_browsing_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run run.py
```

---

## 🧠 Tech Stack

- **Python 3.10+**
- [Streamlit](https://streamlit.io/) - UI framework
- [Transformers (Hugging Face)](https://huggingface.co/) - RoBERTa classification
- [LangChain](https://www.langchain.com/) + [Groq API](https://console.groq.com/) - LLaMA3 70B reasoning
- [Google Safe Browsing API](https://developers.google.com/safe-browsing) - URL threat detection

---

## 🔐 Security Note

- All API keys are loaded from environment variables using `.env` (never commit secrets!)
- Sensitive detection logic can be enhanced with HTTPS and additional rate limiting if deployed publicly.


## 📦 To-Do / Improvements

- ✅ Modular codebase for GitHub push
- [ ] Deploy to Hugging Face or Streamlit Cloud
- [ ] Chrome Extension integration
- [ ] Real-time SMS/Email parsing from connected inbox
- [ ] Support for attachments (PDF, DOC, etc.)

---

## 🧑‍💻 Author

**Davinder Singh** – [@codedavin](https://github.com/codedavin)


