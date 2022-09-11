from django.urls import path

from .views import (
    HomePageView,
    ProductDetailView,
    AddItem,
    RemoveItem,
    BasketView,
    BuyItem,
    BuyItems,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("item/<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("basket/add/<int:pk>/", AddItem.as_view(), name="item_add"),
    path("basket/remove/<int:pk>/", RemoveItem.as_view(), name="item_remove"),
    path("basket/", BasketView.as_view(), name="basket"),
    path("buy/<int:pk>/", BuyItem.as_view()),
    path("buy/items/", BuyItems.as_view()),
]
