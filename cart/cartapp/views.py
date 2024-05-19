import requests
from cartapp.models import CartItem
from cartapp.serializers import CartItemSerializer

from cartapp.utils import (
    add_to_cart,
    get_cart_item,
    get_cart_items,
    remove_cart_item,
    update_cart_item,
    get_cart_items_by_ids,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CartListApiView(APIView):
    def get(self, request, *args, **kwargs):
        cartitems = CartItem.objects.all()
        serializer = CartItemSerializer(cartitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        action = request.data.get("action")
        user_id = request.data.get("user_id")
        cart_items = get_cart_items(user_id)

        if action == "add":
            product_id = request.data.get("product_id")
            product_price = request.data.get("product_price")
            add_to_cart(user_id, product_id, product_price)
            return Response("OK", status=status.HTTP_200_OK)

        elif action == "update":
            cart_item_id = request.data.get("cart_item_id")
            quantity = request.data.get("quantity")
            update_cart_item(cart_item_id, quantity)

        elif action == "delete":
            cart_item_id = request.data.get("cart_item_id")
            remove_cart_item(cart_item_id)

        elif action == "listByIds":
            order_item_ids = request.data.get("order_item_ids")
            cart_items = get_cart_items_by_ids(order_item_ids)

        product_ids = [items.product_id for items in cart_items]
        if len(cart_items) > 0:
            response = requests.post(
                "http://localhost:8001/api/products/",
                {
                    "action": "listByIds",
                    "product_ids": product_ids,
                },
            )
            products = response.json()
            for cart_item, product in zip(cart_items, products):
                cart_item.product_name = product["name"]
                cart_item.product_type = product["type"]
                cart_item.product_price = product["price"]
                cart_item.product_image = product["image"]
        serializer = CartItemSerializer(cart_items, many=True)
        response_data = {"cart_items": serializer.data}
        return Response(response_data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        action = request.data.get("action")
        cart_item_ids = request.data.get("cart_item_ids")
        order_id = request.data.get("order_id")
        print(cart_item_ids)
        cart_items = get_cart_items_by_ids(cart_item_ids)
        if action == "paid":
            for cart_item in cart_items:
                cart_item.order_id = order_id
                cart_item.is_paid = True
                cart_item.save()
        return Response("OK", status=status.HTTP_200_OK)
