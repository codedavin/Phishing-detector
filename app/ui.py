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
            try:
                result = analyze_message(user_input, api_key)
            except Exception as e:
                st.error(f"❗ Error while analyzing message: {str(e)}")
                return

            try:
                explanation = explain_with_llm(user_input, result)
            except Exception as e:
                explanation = "❗ Unable to generate AI explanation at the moment."
                st.warning(f"LLM explanation error: {str(e)}")
                st.markdown("### 💡 Explanation")
                st.info(explanation)
            try:
                st.subheader(result.get("verdict", "No Verdict"))
                st.metric("📊 Confidence", result.get("phishing_confidence", "N/A"))
                st.metric("🔐 Trust Score", result.get("trust_score", "N/A"))

                st.markdown("### ⚠️ Heuristics")
                if result.get("heuristic_flags"):
                    for flag in result["heuristic_flags"]:
                        st.warning(flag)
                else:
                    st.success("✅ No heuristic flags found.")

                st.markdown("### 🌐 URLs Found")
                if result.get("urls_found"):
                    for url in result["urls_found"]:
                        st.write(f"- {url}")
                else:
                    st.info("ℹ️ No URLs found in the message.")

                st.markdown("### 🚫 Dangerous URLs")
                if result.get("dangerous_urls"):
                    for url in result["dangerous_urls"]:
                        st.error(f"- {url}")
                else:
                    st.success("✅ No dangerous URLs detected.")

                st.markdown("### 💡 Explanation")
                st.info(explanation)

            except Exception as e:
                st.error(f"❗ Error displaying results: {str(e)}")
