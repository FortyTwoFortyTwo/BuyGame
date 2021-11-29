from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Platform


def cart_contents(request):

    cart_items = []
    total = Decimal(0.0)
    product_count = 0
    cart = request.session.get("cart", {})

    for item_id, platforms in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        for platform_id, quantity in platforms.items():
            platform = get_object_or_404(Platform, pk=platform_id)

            total += quantity * product.get_price()
            product_count += quantity
            cart_items.append({
                "item_id": item_id,
                "platform": platform,
                "quantity": quantity,
                "product": product,
            })

    if total >= settings.SPECIAL_DISCOUNT_THRESHOLD:
        special_discount_save = int(total * Decimal(settings.SPECIAL_DISCOUNT_PERCENTAGE) * Decimal(100.0)) / Decimal(100.0)
        special_discount_delta = 0
    else:
        special_discount_save = 0
        special_discount_delta = Decimal(settings.SPECIAL_DISCOUNT_THRESHOLD) - total

    grand_total = total - special_discount_save

    context = {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count,
        "special_discount_save": special_discount_save,
        "special_discount_delta": special_discount_delta,
        "special_discount_threshold": settings.SPECIAL_DISCOUNT_THRESHOLD,
        "special_discount_percentage": settings.SPECIAL_DISCOUNT_PERCENTAGE * 100,
        "grand_total": grand_total,
    }

    return context
