from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from products.models import Product, Category, Platform


def raw_products(request):
    products = Product.objects.all()
    raw = serializers.serialize('json', products)
    return HttpResponse(raw, content_type="text/json-comment-filtered")


def raw_categories(request):
    categories = Category.objects.all()
    raw = serializers.serialize('json', categories)
    return HttpResponse(raw, content_type="text/json-comment-filtered")


def raw_platforms(request):
    platforms = Platform.objects.all()
    raw = serializers.serialize('json', platforms)
    return HttpResponse(raw, content_type="text/json-comment-filtered")
