from django.core import serializers
from django.http import HttpResponse
from products.models import Product, Category, Platform


def raw_products(request):
    """ Return JSON of all products """

    products = Product.objects.all()
    raw = serializers.serialize("json", products)
    return HttpResponse(raw, content_type="text/json-comment-filtered")


def raw_categories(request):
    """ Return JSON of all categories """

    categories = Category.objects.all()
    raw = serializers.serialize("json", categories)
    return HttpResponse(raw, content_type="text/json-comment-filtered")


def raw_platforms(request):
    """ Return JSON of all platforms """

    platforms = Platform.objects.all()
    raw = serializers.serialize("json", platforms)
    return HttpResponse(raw, content_type="text/json-comment-filtered")
