from shop.settings import BASKET_SESSION
from store.models.product import Item

from django.db.models.query import QuerySet


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
        self.session[BASKET_SESSION] = {}

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
            return sum(int(item["price"]) for item in self.basket.values())
        else:
            return 0

    # def get_total_price(self) -> int:
    #     return sum(
    #         [int(item["price"]) * item["quantity"] for item in self.basket.values()]
    #     )
