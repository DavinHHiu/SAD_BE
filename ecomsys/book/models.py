from django.db import models
from product.models import Product


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    email = models.EmailField()


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()


class Category(models.Model):
    category_choices = [
        ("Fiction", "Fiction"),
        ("Non-Fiction", "Non-Fiction"),
        ("Children's", "Children's"),
        (
            "Science and Technology",
            "Science and Technology",
        ),
        ("Travel", "Travel"),
        ("Cooking", "Cooking"),
    ]

    category = models.CharField(max_length=255, choices=category_choices)

    class Meta:
        verbose_name_plural = "Categories"


class Book(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    publication_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="book_covers/")
