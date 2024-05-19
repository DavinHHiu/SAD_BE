from bookapp.models import Author, Book, Category, Publisher
from productapp.serializers import ProductSerializer
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    category = CategorySerializer()
    product = ProductSerializer()

    class Meta:
        model = Book
        fields = "__all__"

    def get_image_url(self, product):
        request = self.context.get("request")
        image_url = product.image.url
        return request.build_absolute_uri(image_url)
