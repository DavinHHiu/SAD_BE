from datetime import datetime, timedelta

from django.db import models


class Shipment(models.Model):
    shipping_details = {
        "Standard": {"name": "Standard", "fee": 2.99, "shipping_days": 3},
        "Express": {"name": "Express", "fee": 4.99, "shipping_days": 2},
        "Super Express": {"name": "Super Express", "fee": 6.99, "shipping_days": 1},
    }
    shipping_method_names = ["Standard", "Express", "Super Express"]
    shipping_choices = [
        (alias, details["name"]) for alias, details in shipping_details.items()
    ]
    shiping_status_choices = [
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("In transit", "In transit"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
        ("Returned", "Returned"),
    ]

    order_id = models.IntegerField()
    shipping_address = models.TextField(null=True, blank=True)
    shipping_method = models.CharField(
        max_length=255, choices=shipping_choices, default="Standard"
    )
    shipping_status = models.CharField(
        max_length=255, choices=shiping_status_choices, default="Processing"
    )
    estimated_delivery_date = models.DateField()
    shipping_fee = models.FloatField(default=2.99)
    create_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        details = self.shipping_details.get(self.shipping_method)
        if details:
            self.estimated_delivery_days = details.get("shipping_days", 3)
            self.estimated_delivery_date = (
                datetime.now() + timedelta(days=self.estimated_delivery_days)
            ).date()
            self.shipping_fee = details.get("fee", 2.99)
        super().save(*args, **kwargs)
