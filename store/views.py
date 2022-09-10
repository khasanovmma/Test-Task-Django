from typing import Any

from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.http import HttpRequest, HttpResponse

from .models.product import Item
from .bussines_logic.services import Basket
from .models import product
from .bussines_logic.selectors import get_all_products


class HomePageView(ListView):
    model = Item
    template_name: str = "store/index.html"
    context_object_name: str = "products"
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Item
    template_name: str = "store/detail.html"
    context_object_name: str = "product"


class AddItem(TemplateView):
    def get(self, request, *args, **kwargs):
        basket = Basket(request)

        current_page = request.META.get("HTTP_REFERER")
        item = product.Item.objects.get(pk=kwargs["pk"])

        basket.add(product=item)

        return HttpResponseRedirect(current_page)


class RemoveItem(TemplateView):
    def get(self, request, *args, **kwargs):
        basket = Basket(request)

        current_page = request.META.get("HTTP_REFERER")
        item = get_object_or_404(product.Item, pk=kwargs["pk"])

        basket.remove(item)

        return HttpResponseRedirect(current_page)


class BasketView(TemplateView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> render:
        basket = Basket(request)

        context = {"basket": basket}

        return render(request, "store/cart.html", context=context)
