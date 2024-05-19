from django.apps import apps
from productapp.models import Product
from productapp.serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from bookapp.serializers import BookSerializer
from clothapp.serializers import ClothSerializer
from mobilephoneapp.serializers import MobilePhoneSerializer


class ProductListApiView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(
            products, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        action = request.data.get("action")
        if action == "listByIds":
            product_ids = request.data.getlist("product_ids")
            products = Product.objects.filter(id__in=product_ids)
            serializer = ProductSerializer(
                products, many=True, context={"request": request}
            )
            return Response(serializer.data, status=status.HTTP_200_OK)


class ProductApiView(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def get(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailApiView(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def get(self, request, product_id):
        product = self.get_object(product_id)
        if product is not None:
            type = product.type
            if type == "book":
                Book = apps.get_model("bookapp", "Book")
                book = Book.objects.filter(product=product).first()
                serializer = BookSerializer(book, context={"request": request})
                productdetail = serializer.data
            if type == "cloth":
                Cloth = apps.get_model("clothapp", "Cloth")
                cloth = Cloth.objects.filter(product=product).first()
                serializer = ClothSerializer(cloth, context={"request": request})
                productdetail = serializer.data
            if type == "mobile":
                MobilePhone = apps.get_model("mobilephoneapp", "MobilePhone")
                mobile = MobilePhone.objects.filter(product=product).first()
                serializer = MobilePhoneSerializer(mobile, context={"request": request})
                productdetail = serializer.data

        return Response(productdetail, status=status.HTTP_200_OK)
