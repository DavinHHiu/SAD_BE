from django.db import models


class Product(models.Model):
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
    image = models.ImageField(upload_to=f'images/{type}')
