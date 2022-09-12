from typing import Any


from django.views.generic import ListView, DetailView, TemplateView, View
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .models.product import Item
from .bussines_logic.services import Basket, StripeService
from .models import order
from .bussines_logic.selectors import get_product_by_pk, get_current_page, create_order
from shop.settings import STRIPE_PUBLISHABLE_KEY


class HomePageView(ListView):
    model = Item
    template_name: str = "store/index.html"
    context_object_name: str = "products"
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Item
    template_name: str = "store/detail.html"
    context_object_name: str = "product"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        session_id = self.request.GET.get("session_id")

        if session_id:

            order_detail, created = order.Order.objects.get_or_create(
                session_id=session_id
            )
            if created:
                messages.success(self.request, "Successfully paid")
                stripe_service = StripeService()
                name, email = stripe_service.get_detail_by_session_id(
                    session_id=session_id
                )
                order_detail.ordered_by = name
                order_detail.email = email
                order_detail.items.add(context["product"].id)
                order_detail.save()

        context["stripe_publishable_key"] = STRIPE_PUBLISHABLE_KEY
        return context


class AddItem(TemplateView):
    def get(self, request, *args, **kwargs):
        basket = Basket(request)

        product = get_product_by_pk(pk=kwargs["pk"])
        basket.add(product=product)

        return HttpResponseRedirect(get_current_page(request=request))


class RemoveItem(TemplateView):
    def get(self, request, *args, **kwargs):
        basket = Basket(request)

        product = get_product_by_pk(pk=kwargs["pk"])
        basket.remove(product=product)

        return HttpResponseRedirect(get_current_page(request=request))


class BasketView(TemplateView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> render:
        basket = Basket(request)
        session_id = request.GET.get("session_id")
        if request.GET.get("session_id"):

            order_detail, created = order.Order.objects.get_or_create(
                session_id=session_id
            )
            if created:
                messages.success(self.request, "Successfully paid")
                stripe_service = StripeService()
                name, email = stripe_service.get_detail_by_session_id(
                    session_id=session_id
                )
                print(name, email)
                create_order(
                    order_detail=order_detail,
                    name=name,
                    email=email,
                    products=basket,
                )
                basket.clear()

        context = {"basket": basket, "stripe_publishable_key": STRIPE_PUBLISHABLE_KEY}

        return render(request, "store/cart.html", context=context)


@method_decorator(csrf_exempt, name="dispatch")
class BuyItem(View):
    def get(self, request, pk):
        product = get_product_by_pk(pk=pk)
        stripe_service = StripeService()
        session_id = stripe_service.checkout(request=request, products=product)
        return JsonResponse({"id": session_id})


@method_decorator(csrf_exempt, name="dispatch")
class BuyItems(View):
    def get(self, request):
        products = Basket(request)
        stripe_service = StripeService()
        session_id = stripe_service.checkout(
            request=request, products=products, multiple=True
        )

        return JsonResponse({"id": session_id})
