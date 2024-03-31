from django.db import models

from product.models import Product


class MobilePhone(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    release_date = models.DateField()
    image = models.ImageField(upload_to="mobile_phone_images/")
