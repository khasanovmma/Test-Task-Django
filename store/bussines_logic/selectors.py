from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from store.models.product import Item


def get_all_products():
    return Item.objects.all()


def get_product_by_pk(*, pk: int):
    return get_object_or_404(Item, pk=pk)


def get_current_page(*, request: HttpRequest):
    return request.META.get("HTTP_REFERER")


def create_order(*, order_detail, name, email, products):
    order_detail.ordered_by = name
    order_detail.email = email
    for product in products:
        order_detail.items.add(product)
    order_detail.save()
