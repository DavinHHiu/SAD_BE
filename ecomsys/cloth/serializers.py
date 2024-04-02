from cloth.models import Cloth
from product.serializers import ProductSerializer
from rest_framework import serializers


class ClothSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cloth
        fields = "__all__"

    def get_image_url(self, product):
        request = self.context.get("request")
        image_url = product.image.url
        return request.build_absolute_uri(image_url)
