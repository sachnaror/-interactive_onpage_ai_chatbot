ALLOWED_INTENTS = {"VIEW", "DOWNLOAD", "STATUS"}

def is_allowed(ai_result):
    return ai_result.get("intent") in ALLOWED_INTENTS and ai_result.get("confidence", 0) >= 0.5
