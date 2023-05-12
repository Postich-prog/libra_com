from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, CommentViewSet, GenreViewSet

app_name = 'api'

router = DefaultRouter()

router.register('books', BookViewSet)
router.register('genres', GenreViewSet)
router.register(r'books/(?P<book_id>\d+)/', BookViewSet)
router.register(
    r'books/(?P<book_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
]
