from bookapp.models import Author, Book, Category, Publisher
from django.contrib import admin

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)
