# Generated by Django 3.2.18 on 2023-04-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(related_name='genres', to='book.Genre', verbose_name='Жанр'),
        ),
    ]
