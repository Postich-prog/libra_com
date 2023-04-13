from book.models import Book, Genre
from rest_framework import filters, permissions, viewsets
from .serializers import BookSerializer, GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
