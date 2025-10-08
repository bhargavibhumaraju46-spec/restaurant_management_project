from django.db import models
class MenuCategory(models.Model):
    name = models. CharField(max_length=255)
    def __str__(self):
        return self.name
from rest_framework import serializers
from .models import MenuCategory
class MenuCategorySerializer(serializers.MenuCategorySerializer):
    class Meta:
        models = MenuCategory
        fields = ['id', 'name']
from rest_framework import viewsets
from .models import MenuCategory
from .serializers import MenuCategory
class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
from django.urls import path, include
from rest_framework import routers
from .views import MenuCategoryViewSet
router = routers.DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
]                    
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/home/', include('home.urls')),
]