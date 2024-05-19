from django.db import models
from datetime import datetime


class MobilePhone(models.Model):
    id = models.CharField(max_length=255, blank=True, primary_key=True)
    product = models.ForeignKey("productapp.Product", on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    release_date = models.DateField()
    
    def save(self, *args, **kwargs):
        timestamp = int(datetime.now().timestamp())
        self.id = f'mobile_{timestamp}'
        super().save(self, *args, **kwargs)
