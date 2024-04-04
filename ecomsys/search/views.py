from book.models import Book
from cloth.models import Cloth
from django.forms.models import model_to_dict
from mobilephone.models import MobilePhone
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SearchApiView(APIView):
    def get(self, request, keyword=""):
        print(keyword)
        products = Product.objects.filter(name__icontains=keyword)
        serializer = ProductSerializer(products, many=True)
        response = {}
        return Response(serializer.data, status=status.HTTP_200_OK)
