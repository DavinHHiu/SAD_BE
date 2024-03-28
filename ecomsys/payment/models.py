from django.db import models

class Payment(models.Model):
    payment_method = models.CharField()
    card_no = models.CharField(max_length=255)
