from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SearchApiView(APIView):
    def get(self, request, keyword=""):
        # books = Book.objects.filter(product__name__icontains=keyword)
        # clothes = Cloth.objects.filter(product__name__icontains=keyword)
        # mobile_phones = MobilePhone.objects.filter(product__name__icontains=keyword)

        # book_serializers = BookSerializer(
        #     books, many=True, context={"request": request}
        # )
        # cloth_serializers = ClothSerializer(
        #     clothes, many=True, context={"request": request}
        # )
        # mobile_phone_serializers = MobilePhoneSerializer(
        #     mobile_phones, many=True, context={"request": request}
        # )

        # response = {
        #     "books": book_serializers.data,
        #     "clothes": cloth_serializers.data,
        #     "mobile_phones": mobile_phone_serializers.data,
        # }

        response = {
            "books": 1,
            "clothes": 2,
            "mobile_phones": 3,
        }

        return Response(response, status=status.HTTP_200_OK)
