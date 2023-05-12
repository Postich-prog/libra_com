from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'book'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # path('book/', views.book_list),
    path('books/<int:book_id>/', views.post_detail, name='book_detail'),
    path(
        'books/<int:book_id>/comment/',
        views.add_comment,
        name='add_comment'
    ),
    path(
        'books/<int:book_id>/favorite/',
        views.add_to_favorite,
        name='add_to_favorite'
    ),
    path(
        'books/<int:book_id>/unfavorite/',
        views.delete_from_favorite,
        name='delete_from_favorite'
    ),
    path(
        '/favorites/',
        views.favorites,
        name='favorites'
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
