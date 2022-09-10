from django.urls import path

from .views import HomePageView, ProductDetailView, AddItem, RemoveItem, BasketView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("item/<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("cart/add/<int:pk>/", AddItem.as_view(), name="item_add"),
    path("cart/remove/<int:pk>/", RemoveItem.as_view(), name="item_remove"),
    path("basket/", BasketView.as_view(), name="basket"),
]
