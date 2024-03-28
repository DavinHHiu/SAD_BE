from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.views import get_cart_items
from user.models import User
from order.models import Order


class PlaceOrderApiView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.POST.get("user_id")

        shipping_address = request.POST.get("shipping_address")
        shipping_method = request.POST.get("shipping_method")

        payment_method = request.POST.get("payment_method")
        card_no = request.POST.get("card_no")
        expired_date = request.POST.get("expired_date")

        # process
        user = User.objects.get(id=user_id)
        cart_items = get_cart_items(user_id)
        total_price = 0
        for cart_item in cart_items:
            total_price += cart_item.total_price

        # create order
        order = Order(user=user, address=shipping_address, total_price=total_price)
        order.save()

        response_data = {
            "created_status": "Successfully"
        }

        return Response(response_data, status=status.HTTP_200_OK)