from transformers import pipeline

model = pipeline("text-classification", model="roberta-base", top_k=None)

def classify_message(text):
    result = model(text)[0][0]
    return result["label"].lower(), result["score"]
