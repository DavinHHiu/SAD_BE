from book.models import Book
from book.serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class BookListApiView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'author': request.data.get('author'),
            'publisher': request.data.get('publisher'),
            'publication_date': request.data.get('publication_date'),
            'price': request.data.get('price'),
            'description': request.data.get('description'),
            'image': request.data.get('image')
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailApiView(APIView):
    def get_object(self, book_id):
        try:
            return Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return None

    def get(self, request, book_id):
        book = self.get_object(book_id)
        if book is not None:
            serializer = BookSerializer(book, context={"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "Object with book_id does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )
