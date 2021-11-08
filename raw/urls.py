from django.urls import path
from . import views

urlpatterns = [
    path('products', views.raw_products, name='raw_products'),
    path('categories', views.raw_categories, name='raw_categories'),
]