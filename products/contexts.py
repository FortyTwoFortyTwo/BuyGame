from .models import Category, Platform


def products_contents(request):

    context = {
        "categories": Category.objects.all(),
        "platforms": Platform.objects.all(),
    }

    return context