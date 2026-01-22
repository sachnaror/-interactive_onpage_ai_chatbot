import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
You are an intent classifier for an investor portal.
Allowed intents:
- VIEW
- DOWNLOAD
- STATUS

Return JSON with:
intent, offering, profile, confidence (0-1)
"""

def parse_intent(user_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text},
        ],
    )

    try:
        return json.loads(response.choices[0].message["content"])
    except Exception:
        return {"intent": "UNKNOWN", "confidence": 0.0}
