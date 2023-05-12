from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include('book.urls')),
    path('about/', include('about.urls', namespace='about')),
    path('auth/', include('users.urls')),
    # Если какой-то URL не обнаружится в приложении users —
    # Django пойдёт искать его в django.contrib.auth
    path('auth/', include('django.contrib.auth.urls')),
]
