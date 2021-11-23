from django.urls import path
from . import views

urlpatterns = [
    path('products', views.raw_products, name='raw_products'),
    path('categories', views.raw_categories, name='raw_categories'),
    path('platforms', views.raw_platforms, name='raw_platforms'),
]
