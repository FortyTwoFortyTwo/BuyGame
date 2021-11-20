from django.shortcuts import render
from products.models import Category, Platform

# Create your views here.

def index(request):
    """ A view to return the index page """

    context = {
        'categories': Category.objects.all(),
        'platforms': Platform.objects.all(),
    }

    return render(request, 'home/index.html', context)
