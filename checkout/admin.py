from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInLine(admin.TabularInline):
    """ Tabular inline for admin order line item """
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    """ Order model for admin to manage """
    
    inlines = (OrderLineItemAdminInLine,)

    readonly_fields = ("order_number", "date",
                       "discount_cost", "order_total",
                       "grand_total", "original_cart",
                       "stripe_pid")

    fields = (
        "order_number",
        "user_profile",
        "date",
        "full_name",
        "email",
        "phone_number",
        "country",
        "postcode",
        "town_or_city",
        "street_address1",
        "street_address2",
        "county",
        "discount_cost",
        "order_total",
        "grand_total",
        "original_cart",
        "stripe_pid",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "discount_cost",
        "grand_total",
    )

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
