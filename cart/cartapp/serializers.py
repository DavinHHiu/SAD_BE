from cartapp.models import CartItem
from rest_framework import serializers
import requests


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=255)
    product_type = serializers.CharField(max_length=255)
    product_price = serializers.FloatField()
    product_image = serializers.CharField(max_length=255)

    class Meta:
        model = CartItem
        fields = "__all__"
