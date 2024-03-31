from django.db import models

from order.models import Order
from product.models import Product
from user.models import User


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="cart_items",
        blank=True,
        null=True,
        default=None,
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantiy = models.IntegerField(default=1)
    is_paid = models.BooleanField(default=False)
    total_price = models.FloatField()

    def augment_quantity(self, quantity):
        self.quantiy += quantity
        self.save()

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price
        super.save(self, *args, **kwargs)
