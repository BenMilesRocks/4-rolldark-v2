'''Contact app urls.py'''

from django.urls import path

from .views import SuccessView, ContactView

urlpatterns = [
    path("contact_us/", ContactView.as_view(), name="contact_us"),
    path("message_sent/", SuccessView.as_view(), name="message_sent"),
]
