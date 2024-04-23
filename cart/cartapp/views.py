from cartapp.models import CartItem
from cartapp.serializers import CartItemSerializer

# from cartapp.utils import (
#     add_to_cart,
#     get_cart_items,
#     remove_cart_item,
#     update_cart_item,
# )
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CartListApiView(APIView):
    def get(self, request, *args, **kwargs):
        cartitems = CartItem.objects.all()
        serializer = CartItemSerializer(cartitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     action = request.data.get("action")
    #     user_id = request.data.get("user_id")

    #     if action == "add":
    #         product_id = request.data.get("product_id")
    #         add_to_cart(user_id, product_id)

    #     elif action == "update":
    #         cart_item_id = request.data.get("cart_item_id")
    #         quantity = request.data.get("quantity")
    #         update_cart_item(cart_item_id, quantity)

    #     elif action == "delete":
    #         cart_item_id = request.data.get("cart_item_id")
    #         remove_cart_item(cart_item_id)

    #     cart_items = get_cart_items(user_id)
    #     serializer = CartItemSerializer(
    #         cart_items, many=True, context={"request": request}
    #     )
    #     response_data = {"cart-items": serializer.data}
    #     return Response(response_data, status=status.HTTP_200_OK)
