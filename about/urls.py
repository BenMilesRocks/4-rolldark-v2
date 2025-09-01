"""About App URLS"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('add_gm/', views.add_gm, name='add_gm'),
    path('edit_gm/<int:gm_id>/', views.edit_gm, name='edit_gm'),
]
