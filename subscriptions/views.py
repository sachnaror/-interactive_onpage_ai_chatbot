import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import SubscriptionDocument
from .services.gpt_intent_parser import parse_intent
from .services.guardrails import is_allowed
from .services.response_builder import build_response

def documents_page(request):
    docs = SubscriptionDocument.objects.all()
    return render(request, "subscriptions/documents.html", {"docs": docs})

def chatbot_api(request):
    payload = json.loads(request.body)
    user_message = payload.get("message", "")

    ai_result = parse_intent(user_message)

    if not is_allowed(ai_result):
        return JsonResponse({"reply": "Sorry, I can’t help with that request."})

    reply = build_response(ai_result)
    return JsonResponse({"reply": reply})
