from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from shipmentapp.models import Shipment
from shipmentapp.serializers import ShipmentSerializer


class ShippingDetailsApiView(APIView):
    def get(self, request, *args, **kwargs):
        response = {
            "shipping_details": Shipment.shipping_details,
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        action = request.data.get("action")
        order_id = request.data.get("order_id")

        if action == "add":
            shipment = Shipment(order_id=order_id)
            shipment.save()
        elif action == "get":
            shipment = Shipment.objects.filter(order_id=order_id).first()

        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        shipment_id = request.data.get("shipment_id")
        shipping_method = request.data.get("shipping_method")
        shipping_address = request.data.get("shipping_address")

        shipment = Shipment.objects.get(id=shipment_id)
        if shipping_method:
            shipment.shipping_method = shipping_method
        if shipping_address:
            shipment.shipping_address = shipping_address
        shipment.save()

        serializer = ShipmentSerializer(shipment)

        return Response(serializer.data, status=status.HTTP_200_OK)
