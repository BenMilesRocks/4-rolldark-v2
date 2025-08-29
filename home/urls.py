"""Home App URLS"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('message_sent/', views.message_sent, name='message_sent'),
    path('add/', views.add_call_to_action, name='add_call_to_action'),
    path('view_all_actions/', views.view_all_actions, name='view_all_actions'),
    path('edit/<int:call_to_action_id>/', views.edit_call_to_action, name='edit_call_to_action'),
    path('delete/<int:call_to_action_id>/',
          views.delete_call_to_action, name='delete_call_to_action'),
]
