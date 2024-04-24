from productapp.models import Product
from productapp.serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductListApiView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)
