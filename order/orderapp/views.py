from orderapp.models import Order
from orderapp.serializers import OrderSerializer
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class PlaceOrderApiView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        order_item_ids = request.data.get("order_item_ids")
        user_id = request.data.get("user_id")
        order_id = request.data.get("order_id")
        total_price = request.data.get("total_price")

        if order_id:
            shipment = requests.post(
                "http://localhost:8009/api/shipment/",
                {
                    "action": "get",
                    "order_id": order_id,
                },
            )
            payment = requests.post(
                "http://localhost:8008/api/payment/",
                {
                    "action": "get",
                    "order_id": order_id,
                },
            )
            order = Order.objects.get(id=order_id)
            if total_price != None and order.total_price != total_price:
                order.total_price = total_price
                order.save()
        else:
            order = Order(user_id=user_id, total_price=total_price)
            order.save()

            shipment = requests.post(
                "http://localhost:8009/api/shipment/",
                {
                    "action": "add",
                    "order_id": order.id,
                },
            )

            payment = requests.post(
                "http://localhost:8008/api/payment/",
                {
                    "action": "add",
                    "order_id": order.id,
                    "total_price": order.total_price + shipment.json()["shipping_fee"],
                },
            )

        order_serializer = OrderSerializer(order)

        response = {
            "order": order_serializer.data,
            "shipment": shipment.json(),
            "payment": payment.json(),
        }

        return Response(response, status=status.HTTP_200_OK)
