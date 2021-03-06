from django.contrib import admin
from .models import Product, Category, Platform

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """Admin model to manage products"""

    list_display = (
        "name",
        "category",
        "price",
        "rating",
        "new",
        "discount",
    )

    ordering = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    """Admin model to manage categories"""

    list_display = (
        "friendly_name",
        "name",
    )


class PlatformAdmin(admin.ModelAdmin):
    """Admin model to manage platforms"""

    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Platform, PlatformAdmin)
