from django.contrib import admin

from .models import Book, Comment, Genre

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Comment)
