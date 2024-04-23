from django.db import models


class Cloth(models.Model):
    product_id = models.IntegerField()
    brand = models.CharField(max_length=255)
    size = models.CharField(max_length=10)
    image = models.ImageField(upload_to="cloth_images/")

    class Meta:
        verbose_name_plural = "Clothes"
