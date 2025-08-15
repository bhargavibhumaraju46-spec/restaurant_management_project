from django.contrib.auth import view as auth_views
from django.urls import path, include
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]