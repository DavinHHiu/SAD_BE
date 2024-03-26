from django.db import models


class Cloth(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="cloth_images/")

    class Meta:
        verbose_name_plural = "Clothes"
