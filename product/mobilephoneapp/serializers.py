from mobilephoneapp.models import MobilePhone
from rest_framework import serializers
from productapp.serializers import ProductSerializer


class MobilePhoneSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = MobilePhone
        fields = "__all__"

    def get_image_url(self, product):
        request = self.context.get("request")
        image_url = product.image.url
        return request.build_absolute_uri(image_url)
