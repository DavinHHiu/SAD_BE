from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='book_covers/')

    def __str__(self):
        return self.title
