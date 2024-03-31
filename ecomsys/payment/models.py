from django.db import models


class Payment(models.Model):
    payment_method = models.CharField(max_length=255)
    card_no = models.CharField(max_length=255)
