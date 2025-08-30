'''Contact app urls.py'''

from django.urls import path

from .views import SuccessView, ContactView

urlpatterns = [
    path("", ContactView.as_view(), name="contact_us"),
    path("success/", SuccessView.as_view(), name="success"),
]
