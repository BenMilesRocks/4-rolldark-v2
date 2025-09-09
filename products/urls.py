"""URL configuration for Products app"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.disabled_products, name='products'),
    path('dice', views.dice, name='dice'),
    path('games', views.games, name='games'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
