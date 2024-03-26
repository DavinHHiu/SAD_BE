from rest_framework import serializers

from mobilephone.models import MobilePhone


class MobilePhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePhone
        fields = "__all__"
    def get_image_url(self, product):
        request = self.context.get('request')
        image_url = product.image.url
        return request.build_absolute_uri(image_url)