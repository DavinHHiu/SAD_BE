from django.db import models
import requests


class CartItem(models.Model):
    user_id = models.CharField(max_length=255)
    order_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default=None,
    )
    product_id = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    is_paid = models.BooleanField(default=False)
    total_price = models.FloatField()

    def augment_quantity(self, quantity):
        self.quantiy += quantity
        self.save()
