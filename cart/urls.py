from django.urls import path

from .views import CartItemAddView, CartItemRemoveView, CartItemView, InfosView, CheckOut

urlpatterns = [
    path('cart/', CartItemView.as_view(), name="cart-view"),
    path('cart/add/<int:movie_id>/', CartItemAddView.as_view(), name="cart-add"),
    path('cart/remove/<int:movie_id>/', CartItemRemoveView.as_view(), name="cart-remove"),
    path('cart/checkout/', CheckOut.as_view(), name="checkout"),
    path('cart/checkout/infos/', InfosView.as_view(), name="infos")
]
