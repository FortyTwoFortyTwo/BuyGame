from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product, Platorm

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to cart """

    platorm_id = request.POST.get('platorm')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    product = get_object_or_404(Product, pk=item_id)
    platorm = get_object_or_404(Platorm, pk=platorm_id)

    if item_id not in list(cart.keys()):
        cart[item_id] = {}

    if platorm_id in list(cart[item_id].keys()):
        cart[item_id][platorm_id] += quantity
        messages.success(request, f'Updated {product.name} for {platorm.friendly_name} quantity to {cart[item_id][platorm_id]}')
    else:
        cart[item_id][platorm_id] = quantity
        messages.success(request, f'Added {product.name} for {platorm.friendly_name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    platorm_id = request.POST.get('platorm')
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    product = get_object_or_404(Product, pk=item_id)
    platorm = get_object_or_404(Platorm, pk=platorm_id)

    if quantity > 0:
        cart[item_id][platorm_id] = quantity
        messages.success(request, f'Updated {product.name} for {platorm.friendly_name} quantity to {cart[item_id][platorm_id]}')
    else:
        messages.success(request, f'Removed {product.name} for {platorm.friendly_name} from your cart')
        del cart[item_id][platorm_id]
        if not cart[item_id]:
            del cart[item_id]
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping cart """

    try:
        platorm_id = request.POST['platorm']
        cart = request.session.get('cart', {})

        del cart[item_id][platorm_id]
        if not cart[item_id]:
            del cart[item_id]

        product = get_object_or_404(Product, pk=item_id)
        platorm = get_object_or_404(Platorm, pk=platorm_id)
        messages.success(request, f'Removed {product.name} for {platorm.friendly_name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
