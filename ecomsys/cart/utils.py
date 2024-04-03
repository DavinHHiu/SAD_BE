from book.models import Book
from cart.models import CartItem
from cloth.models import Cloth
from mobilephone.models import MobilePhone
from product.models import Product
from user.models import User


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
            print(cart_item.product.name, product.name)
            return

    new_cart_item = CartItem()
    new_cart_item.user = User.objects.get(id=user_id)
    new_cart_item.product = product
    if product.type == "book":
        new_cart_item.image = Book.objects.get(product=product).image
    elif product.type == "cloth":
        new_cart_item.image = Cloth.objects.get(product=product).image
    elif product.type == "mobile":
        new_cart_item.image = MobilePhone.objects.get(product=product).image
    print(product.id)
    new_cart_item.save()


def get_cart_item(cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    return cart_item


def update_cart_item(cart_item_id, quantity):
    cartitem = get_cart_item(cart_item_id)

    if cartitem:
        if int(quantity) > 0:
            cartitem.quantity = int(quantity)
            cartitem.save()


def remove_cart_item(cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    print(cart_item_id)
    if cart_item:
        cart_item.delete()
