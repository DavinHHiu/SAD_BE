from product.serializers import ProductSerializer
from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    product = ProductSerializer()
