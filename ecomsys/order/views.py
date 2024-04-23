from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.serializers import CartItemSerializer
from cart.utils import get_cart_items_by_ids
from order.models import Order
from order.serializers import OrderSerializer
from payment.models import Payment
from payment.serializers import PaymentSerializer
from shipment.models import Shipment
from shipment.serializers import ShipmentSerializer
from user.models import User


class PlaceOrderApiView(APIView):
    def post(self, request, *args, **kwargs):
        order_item_ids = request.data.get("order_item_ids")
        user_id = request.data.get("user_id")
        order_id = request.data.get("order_id")

        if order_id:
            order = Order.objects.get(id=order_id)
            shipment = Shipment.objects.filter(order=order).first()
            payment = Payment.objects.filter(order=order).first()
            cart_items = order.cart_items.filter(is_paid=False)
        else:
            user = User.objects.get(id=user_id)
            cart_items = get_cart_items_by_ids(user_id, order_item_ids)
            total_price = 0
            for cart_item in cart_items:
                total_price += cart_item.total_price
            order = Order(user=user, total_price=total_price)
            order.save()
            shipment = Shipment(order=order)
            shipment.save()
            payment = Payment(order=order)

            for cart_item in cart_items:
                cart_item.order = order
                cart_item.save()

        payment.total_price = order.total_price + shipment.shipping_fee
        payment.save()

        order_serializer = OrderSerializer(order)
        cart_items_serializer = CartItemSerializer(
            cart_items, many=True, context={"request": request}
        )
        shipment_serializer = ShipmentSerializer(shipment)
        payemnt_serilalizer = PaymentSerializer(payment)

        response_data = {
            "order": order_serializer.data,
            "cart_items": cart_items_serializer.data,
            "shipment": shipment_serializer.data,
            "payment": payemnt_serilalizer.data,
            "payment_methods": payment.payment_choices_list,
            "shipping_methods": shipment.shipping_method_names,
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def put(self, request):
        user_id = request.data.get("user_id")

        shipment_id = request.data.get("shipment_id")
        shipping_address = request.data.get("shipping_address")
        shipment = Shipment.objects.get(id=shipment_id)
        shipment.shipping_address = shipping_address
        shipment.save()

        payment_id = request.data.get("payment_id")
        total_price = request.data.get("total_price")
        payment = Payment.objects.get(id=payment_id)
        payment.total_price = total_price
        payment.save()

        order_item_ids = request.data.get("order_item_ids")
        order_items = get_cart_items_by_ids(user_id, order_item_ids)

        for order_item in order_items:
            order_item.is_paid = True
            order_item.save()
