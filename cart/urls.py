"""URL configuration for cart app"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add_product/<item_id>/', views.add_product_to_cart, name='add_product_to_cart'),
    path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart')
]
