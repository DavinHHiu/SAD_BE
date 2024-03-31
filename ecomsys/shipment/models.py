from django.db import models

from order.models import Order


class Shipment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    shipping_address = models.TextField()
    shipping_method = models.CharField(max_length=255)
    shipping_status = models.CharField(max_length=255)
    shipping_days = models.IntegerField()
    estimated_delivery_date = models.DateField()
    shipping_fee = models.FloatField()
    create_at = models.DateField(auto_now_add=True)
