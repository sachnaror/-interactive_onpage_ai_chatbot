from django.urls import path
from .views import documents_page, chatbot_api

urlpatterns = [
    path("", documents_page, name="documents"),
    path("chat/", chatbot_api, name="chatbot_api"),
]
