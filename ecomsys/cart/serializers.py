from cart.models import CartItem
from product.serializers import ProductSerializer
from rest_framework import serializers


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = "__all__"
