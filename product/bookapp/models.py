from django.db import models
from datetime import datetime


class Author(models.Model):
    id = models.CharField(max_length=255, blank=True, primary_key=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    email = models.EmailField()

    def save(self, *args, **kwargs):
        timstamp = int(datetime.now().timestamp())
        self.id = f'author_{timstamp}'
        super().save(self, *args, **kwargs)



class Publisher(models.Model):
    id = models.CharField(max_length=255, blank=True, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()

    def save(self, *args, **kwargs):
        timestamp = int(datetime.now().timestamp())
        self.id = f'publisher_{timestamp}'
        super().save(self, *args, **kwargs)


class Category(models.Model):
    id = models.CharField(max_length=255, blank=True, primary_key=True)
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

    def save(self, *args, **kwargs):
        timestamp = int(datetime.now().timestamp())
        self.id = f'category_{timestamp}'
        super().save(self, *args, **kwargs)


class Book(models.Model):
    id = models.CharField(max_length=255, blank=True, primary_key=True)
    product = models.ForeignKey("productapp.Product", on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    publication_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        timestamp = int(datetime.now().timestamp())
        self.id = f'book_{timestamp}'
        super().save(self, *args, **kwargs)