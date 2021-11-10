from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to cart """

    product = Product.objects.get(pk=item_id)
    platorm = int(request.POST.get('platorm'))
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id not in list(cart.keys()):
        cart[item_id] = {}

    if platorm in list(cart[item_id].keys()):
        cart[item_id][platorm] += quantity
    else:
        cart[item_id][platorm] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    platorm = request.POST.get('platorm')
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id][platorm] = quantity
    else:
        del cart[item_id][platorm]
        if not cart[item_id]:
            del cart[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        platorm = request.POST['platorm']
        cart = request.session.get('cart', {})

        del cart[item_id][platorm]
        if not cart[item_id]:
            del cart[item_id]

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
