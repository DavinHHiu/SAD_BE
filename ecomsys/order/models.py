from django.db import models
from user.models import User


class Order(models.Model):
    status_choices = [
        ("Processing", "Processing"),
        ("Pending", "Pending"),
        ("Delivered", "Delivered"),
        ("Completed", "Completed"),
        ("Refunded", "Refunded"),
        ("Cancel", "Cancel"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50, choices=status_choices, default="Processing"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
