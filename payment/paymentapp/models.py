from django.db import models


class Payment(models.Model):
    order = models.IntegerField()
    payment_choices = [
        ("Mono", "Mono"),
        ("Card", "Card"),
        ("Online Banking", "Online Banking"),
        ("COD", "COD"),
    ]
    payment_choices_list = [item[0] for item in payment_choices]
    status_choices = [
        ("Processing", "Processing"),
        ("Cancelled", "Cancelled"),
        ("Completed", "Completed"),
        ("Failed", "Failed"),
        ("Refunded", "Refunded"),
    ]
    payment_method = models.CharField(
        max_length=255, choices=payment_choices, default="COD"
    )
    status = models.CharField(
        max_length=255, choices=status_choices, default="Processing"
    )
    total_price = models.FloatField()
