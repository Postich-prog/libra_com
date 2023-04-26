from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'book'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # path('book/', views.book_list),
    # path('book/<pk>/', views.book_detail),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
