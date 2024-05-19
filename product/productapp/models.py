from django.db import models
from datetime import datetime
import os

def upload_to(instance, filename):
    return os.path.join("images", instance.type, filename);

class Product(models.Model):
    id = models.CharField(max_length=255, blank=True, primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    type = models.CharField(
        max_length=50,
        choices=[
            ("book", "book"),
            ("cloth", "cloth"),
            ("mobile", "mobile"),
        ],
    )
    image = models.ImageField(upload_to=upload_to)

    def save(self, *args, **kwargs):
        timestamp = int(datetime.now().timestamp())
        self.id = f'product_{timestamp}'
        super().save(*args, **kwargs)
