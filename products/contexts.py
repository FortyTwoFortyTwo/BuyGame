from .models import Category, Platform


def products_contents(request):
    """
    Return all categories and platforms to display in nav bar
    """

    context = {
        "categories": Category.objects.all(),
        "platforms": Platform.objects.all(),
    }

    return context