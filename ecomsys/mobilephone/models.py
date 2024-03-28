from django.db import models


class MobilePhone(models.Model):
    brand = models.CharField(max_length=50)
    release_date = models.DateField()
    image = models.ImageField(upload_to="mobile_phone_images/")
