from django.contrib import admin

from .models import order, product


@admin.register(product.Item)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(order.Order)
class OrderAdmin(admin.ModelAdmin):
    pass
