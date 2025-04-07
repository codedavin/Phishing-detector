import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key=groq_api_key,
)

template = """
You're a cybersecurity assistant. Given the message and detection result, explain why it is safe or phishing.

Message: {text}
Result: {verdict}
Trust Score: {trust_score}
Heuristics: {heuristics}
Dangerous URLs: {urls}

Explain it simply.
"""

prompt = ChatPromptTemplate.from_template(template)

def explain_with_llm(text, result):
    return (prompt | llm).invoke({
        "text": text,
        "verdict": result["verdict"],
        "trust_score": result["trust_score"],
        "heuristics": ", ".join(result["heuristic_flags"]),
        "urls": ", ".join(result["dangerous_urls"]),
    }).content
