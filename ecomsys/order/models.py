from django.db import models

class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
