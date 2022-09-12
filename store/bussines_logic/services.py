from shop.settings import BASKET_SESSION, STRIPE_SECRET_KEY
from store.models.product import Item

from django.db.models.query import QuerySet
from django.urls import reverse

import stripe


class Basket:
    def __init__(self, request) -> None:
        self.session = request.session
        basket = self.session.get(BASKET_SESSION)

        if not basket and not basket == {}:
            print(basket)
            self.session[basket] = {}
            basket = self.session[basket]
        self.basket = basket

    def add(self, product: QuerySet) -> None:
        product_id = str(product.id)

        if product_id not in self.basket:
            self.basket[product_id] = {
                "price": str(product.price),
            }

            self.save()

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.basket:
            del self.basket[product_id]

            self.save()

    def clear(self):
        self.basket = {}
        
        self.save()
    
    def save(self):
        self.session[BASKET_SESSION] = self.basket
        
        self.session.modified = True

    def __iter__(self):
        product_ids = self.basket.keys()

        products = Item.objects.filter(id__in=product_ids)

        for product in products:
            self.basket[str(product.id)]["product"] = product

            yield product

    def __len__(self) -> int:
        if self.basket:
            return len(self.basket.values())
        else:
            return 0

    def get_total_price(self) -> int:
        return sum(
            [int(item["price"]) for item in self.basket.values()]
        )


class StripeService:
    def __init__(self) -> None:
        self.stripe  = stripe
        
    
    def generate_line_item(self, product):
        return [
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": product.name,
                            "description": product.description,
                        },
                        "unit_amount": product.price * 100,
                    },
                    "quantity": 1,
                }
            ]

    def generate_line_items(self, products):
        line_items = []
        for product in products:
            line_items.append(
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": product.name,
                            "description": product.description,
                        },
                        "unit_amount": product.price * 100,
                    },
                    "quantity": 1,
                }
            )
        return line_items
    
    def checkout(self, request, products, multiple=False):
        if multiple:
            line_items = self.generate_line_items(products=products)
        else:
            line_items = self.generate_line_item(product=products)
        
        self.stripe.api_key = STRIPE_SECRET_KEY
        session = self.stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url=request.build_absolute_uri(reverse("basket"))
            + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=request.build_absolute_uri(reverse("basket")),
        )
        return session.id