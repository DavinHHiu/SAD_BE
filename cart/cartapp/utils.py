from cartapp.models import CartItem


def get_cart_items(user_id):
    cart_items = CartItem.objects.filter(user_id=user_id, order_id__isnull=True)
    return cart_items


def get_cart_items_by_ids(cart_item_ids):
    cart_items = CartItem.objects.filter(id__in=cart_item_ids)
    return cart_items


def add_to_cart(user_id, product_id, product_price):
    cart_items = get_cart_items(user_id)

    for cart_item in cart_items:
        if cart_item.product_id == product_id and cart_item.is_paid == 0:
            return

    new_cart_item = CartItem(
        user_id=user_id, product_id=product_id, total_price=product_price
    )
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
    if cart_item:
        cart_item.delete()
