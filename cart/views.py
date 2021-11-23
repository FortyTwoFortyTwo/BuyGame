from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product, Platform

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to cart """

    platform_id = request.POST.get('platform')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    product = get_object_or_404(Product, pk=item_id)
    platform = get_object_or_404(Platform, pk=platform_id)

    if item_id not in list(cart.keys()):
        cart[item_id] = {}

    if platform_id in list(cart[item_id].keys()):
        cart[item_id][platform_id] += quantity
        messages.success(request, f'Updated {product.name} for '
                         f'{platform.friendly_name} quantity to '
                         f'{cart[item_id][platform_id]}')
    else:
        cart[item_id][platform_id] = quantity
        messages.success(request, f'Added {product.name} for '
                         f'{platform.friendly_name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """

    platform_id = request.POST.get('platform')
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    product = get_object_or_404(Product, pk=item_id)
    platform = get_object_or_404(Platform, pk=platform_id)

    if quantity > 0:
        cart[item_id][platform_id] = quantity
        messages.success(request, f'Updated {product.name} for '
                         f'{platform.friendly_name} quantity to '
                         f'{cart[item_id][platform_id]}')
    else:
        messages.success(request, f'Removed {product.name} for '
                         f'{platform.friendly_name} from your cart')
        del cart[item_id][platform_id]
        if not cart[item_id]:
            del cart[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping cart """

    try:
        platform_id = request.POST['platform']
        cart = request.session.get('cart', {})

        del cart[item_id][platform_id]
        if not cart[item_id]:
            del cart[item_id]

        product = get_object_or_404(Product, pk=item_id)
        platform = get_object_or_404(Platform, pk=platform_id)
        messages.success(request, f'Removed {product.name} for '
                         f'{platform.friendly_name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
