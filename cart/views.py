from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to cart """

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

    request.session['cart'] = cart
    return redirect(redirect_url)
