"""Home App URLS"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_call_to_action, name='add_call_to_action'),
]
