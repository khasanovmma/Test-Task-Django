from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from store.models.product import Item


def get_all_products():
    return Item.objects.all()

def get_product_by_pk(*, pk: int):
    return get_object_or_404(Item, pk=pk)

def get_current_page(*, request: HttpRequest):
    return request.META.get("HTTP_REFERER")