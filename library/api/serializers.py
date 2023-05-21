from book.models import Book, Comment, Genre
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)


class BookReadSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Book


class BookWriteSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        fields = '__all__'
        model = Book


class CommentSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = ('book', 'author', 'text',)
        model = Comment
