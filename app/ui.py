import streamlit as st
from app.detector import analyze_message
from app.explain import explain_with_llm
from dotenv import load_dotenv
import os

def run_app():
    load_dotenv()
    api_key = os.getenv("SAFE_BROWSING_API_KEY")

    st.set_page_config(page_title="Phishing Detector", page_icon="🛡️")
    st.title("🛡️ AI-Powered Phishing Detector")
    st.markdown("Detect phishing, scams, or spam messages using AI + heuristics + URL safety.")

    user_input = st.text_area("✉️ Enter Message", height=200)

    if st.button("Analyze"):
        if not user_input.strip():
            st.warning("Please enter a message to analyze.")
        else:
            result = analyze_message(user_input, api_key)
            explanation = explain_with_llm(user_input, result)

            st.subheader(result["verdict"])
            st.metric("📊 Confidence", result["phishing_confidence"])
            st.metric("🔐 Trust Score", result["trust_score"])

            st.markdown("### ⚠️ Heuristics")
            for flag in result["heuristic_flags"]:
                st.warning(flag)

            st.markdown("### 🌐 URLs")
            for url in result["urls_found"]:
                st.write(f"- {url}")

            st.markdown("### 🚫 Dangerous URLs")
            for url in result["dangerous_urls"]:
                st.error(f"- {url}")

            st.markdown("### 💡 Explanation")
            st.info(explanation)
