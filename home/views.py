from django.shortcuts import render
from products.models import Category, Platorm

# Create your views here.

def index(request):
    """ A view to return the index page """

    context = {
        'categories': Category.objects.all(),
        'platorms': Platorm.objects.all(),
    }

    return render(request, 'home/index.html', context)
