from rest_framework import serializers

from cloth.models import Cloth

class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = '__all__'
    def get_image_url(self, product):
        request = self.context.get('request')
        image_url = product.image.url
        return request.build_absolute_uri(image_url)
