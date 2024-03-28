from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import CartItem
from cart.serializers import CartItemSerializer
from product.models import Product
from user.models import User


class CartListApiView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get("user_id")
        cart_items = get_cart_items(user_id)
        serializer = CartItemSerializer(
            cart_items, many=True, context={"request": request}
        )
        response_data = {"cart_items": serializer.data}
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")
        user_id = request.POST.get("user_id")

        if action == "add":
            product_id = request.POST.get("product_id")
            add_to_cart(user_id, product_id)

        elif action == "update":
            cart_item_id = request.POST.get("cart_item_id")
            quantity = request.POST.get("quantity")
            update_cart_item(cart_item_id, quantity)

        else:
            cart_item_id = request.POST.get("cart_item_id")
            remove_cart_item(cart_item_id)

        cart_items = get_cart_items(user_id)
        serializer = CartItemSerializer(
            cart_items, many=True, context={"request": request}
        )
        response_data = {"cart-items": serializer.data}
        return Response(response_data, status=status.HTTP_200_OK)


def get_cart_items(user_id):
    user = User.objects.get(id=user_id)
    # cart_items = CartItem.objects.filter(user=user, order__isnull=True)
    cart_items = user.cart_items.filter(is_paid=False)
    return cart_items


def add_to_cart(user_id, product_id):
    product = Product.objects.get(id=product_id)
    cart_items = get_cart_items(user_id)

    for cart_item in cart_items:
        if cart_item.product == product:
            return

    new_cart_item = CartItem()
    new_cart_item.user = User.objects.get(id=user_id)
    new_cart_item.product = product
    new_cart_item.quantiy = 1
    new_cart_item.save()


def get_cart_item(cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    return cart_item


def update_cart_item(cart_item_id, quantity):
    cartitem = get_cart_item(cart_item_id)

    if cartitem:
        if int(quantity) > 0:
            cartitem.quantiy = int(quantity)
            cartitem.save()


def remove_cart_item(cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    if cart_item:
        cart_item.remove()
