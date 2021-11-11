from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51JrPi7KUmXAfzsQtzsV9heX1cSGKBWaD6mXyIi1H6zhpMzkNyb7NBg4NQgABnkOd00xJ5Pl2CgShrPhRzbCeNafI00ECggdRxk',
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)