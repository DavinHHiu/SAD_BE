from django.db import models
from datetime import datetime


class Cloth(models.Model):
    id = models.CharField(max_length=255, blank=True, primary_key=True)
    product = models.ForeignKey("productapp.Product", on_delete=models.CASCADE)
    brand = models.CharField(max_length=255)
    size = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Clothes"

    def save(self, *args, **kwargs):
        timestamp = int(datetime.now().timestamp())
        self.id = f'cloth_{timestamp}'
        super().save(args, **kwargs)
