from django.db import models
class MenuItem(models.Model):
    category = models.CharField(max_length=255)
from rest_framework import serializers
from .models import MenuItem
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.response import Response  
class MenuItemByCategoryView(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = MenuItem.objects.filter(category=category)
            else:
                queryset = MenuItem.objects.none()
                return queryset
from .django.urls import path
from .views import MenuItemByCategoryView
urlpatterns = [
    path('menu-items/by-category/', MenuItemByCategoryView.as_view(), name='menu-items-by-category'),
]        