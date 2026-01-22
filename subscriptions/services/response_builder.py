from subscriptions.models import SubscriptionDocument

def build_response(ai):
    qs = SubscriptionDocument.objects.all()

    if ai.get("offering"):
        qs = qs.filter(offering_name__icontains=ai["offering"])

    if not qs.exists():
        return "I couldn’t find any documents for that selection."

    doc = qs.first()

    if ai["intent"] == "DOWNLOAD":
        if doc.download_url:
            return f"Your document was signed on {doc.executed_on}. Download here: {doc.download_url}"
        return "The document is signed but download is not available yet."

    return f"{doc.document_name} is currently marked as {doc.status}."
