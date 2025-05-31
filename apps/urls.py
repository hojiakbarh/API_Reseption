from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from apps.views import register_api_view, login_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register/', register_api_view, name='register'),
    path('auth/login/', login_api_view, name='login'),
]