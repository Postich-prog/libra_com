from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
        unique=True
    )
    slug = models.SlugField('Слаг', unique=True, default="slug")

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',
    )
    author = models.TextField('Автор')
    genres = models.ManyToManyField(
        Genre,
        verbose_name='Жанр'
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('title',)

    def __str__(self):
        return self.name
