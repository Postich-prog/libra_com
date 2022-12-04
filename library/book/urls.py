from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('book/', views.book_list),
    path('book/<pk>/', views.book_detail),
]
