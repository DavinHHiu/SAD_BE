from bookapp.views import BookDetailApiView, BookListApiView
from django.urls import path

urlpatterns = [
    path("books/", BookListApiView.as_view(), name="book-list"),
    path("books/<int:book_id>", BookDetailApiView.as_view(), name="book-detail"),
]
