from django.db import models
from product.models import Product

class Book(models.Model):
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField()
    image = models.ImageField(upload_to='book_covers/')
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

