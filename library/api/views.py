from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets

from book.models import Book, Comment, Genre

from .serializers import (BookReadSerializer, BookWriteSerializer,
                          CommentSerializer, GenreSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = None

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return BookReadSerializer
        return BookWriteSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def get_queryset(self):
        book = get_object_or_404(
            Book,
            id=self.kwargs.get('book_id')
        )
        return book.comments.all()

    def perform_create(self, serializer):
        book = get_object_or_404(
            Book, pk=self.kwargs.get('book_id')
        )
        serializer.save(author=self.request.user, book=book)
