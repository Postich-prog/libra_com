from django.contrib import admin

from .models import Book, Genre, Comment

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Comment)
