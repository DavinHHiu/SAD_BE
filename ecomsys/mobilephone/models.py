from django.db import models

class MobilePhone(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='mobile_phone_images/')
