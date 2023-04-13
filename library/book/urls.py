from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('about/', views.author),
    #path('book/', views.book_list),
    #path('book/<pk>/', views.book_detail),
]
