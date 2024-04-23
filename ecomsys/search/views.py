from book.models import Book
from book.serializers import BookSerializer
from cloth.models import Cloth
from cloth.serializers import ClothSerializer
from django.forms.models import model_to_dict
from mobilephone.models import MobilePhone
from mobilephone.serializers import MobilePhoneSerializer
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SearchApiView(APIView):
    def get(self, request, keyword=""):
        books = Book.objects.filter(product__name__icontains=keyword)
        clothes = Cloth.objects.filter(product__name__icontains=keyword)
        mobile_phones = MobilePhone.objects.filter(product__name__icontains=keyword)

        book_serializers = BookSerializer(
            books, many=True, context={"request": request}
        )
        cloth_serializers = ClothSerializer(
            clothes, many=True, context={"request": request}
        )
        mobile_phone_serializers = MobilePhoneSerializer(
            mobile_phones, many=True, context={"request": request}
        )

        response = {
            "books": book_serializers.data,
            "clothes": cloth_serializers.data,
            "mobile_phones": mobile_phone_serializers.data,
        }

        return Response(response, status=status.HTTP_200_OK)
