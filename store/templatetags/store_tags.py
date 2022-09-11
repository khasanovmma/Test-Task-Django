from django import template

from store.bussines_logic.services import Basket


register = template.Library()

@register.simple_tag()
def get_product_count_basket(request) -> int:
    return len(Basket(request))
    
@register.simple_tag()
def is_product_in_basket(request, product) -> bool:
    return product in Basket(request)