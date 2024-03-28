from django.urls import path
from cart.views import CartItemSerializer

urlpatterns = [
    path("/cart", CartItemSerializer.as_view())
]