from django.db import models


class Order(models.Model):
    status_choices = [
        ("Processing", "Processing"),
        ("Pending", "Pending"),
        ("Delivered", "Delivered"),
        ("Completed", "Completed"),
        ("Refunded", "Refunded"),
        ("Cancel", "Cancel"),
    ]

    user_id = models.IntegerField()
    status = models.CharField(
        max_length=50, choices=status_choices, default="Processing"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
