from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from shipment.models import Shipment


class ShippingDetailsApiView(APIView):
    def get(self, request, *args, **kwargs):
        response = {
            "shipping_details": Shipment.shipping_details,
        }
        return Response(response, status=status.HTTP_200_OK)
