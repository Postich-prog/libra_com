from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import BookViewSet, GenreViewSet

app_name = 'api'

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('genres', GenreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
