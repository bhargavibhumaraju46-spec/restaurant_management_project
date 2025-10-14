from django.db import models
class MenuCategory(models.Models):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
      def __str_(self):
        return self.name
from rest_framework import serializers
from .models import MenuItem
class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = MenuItem
        fields  = ['name', 'price', 'description', 'category']
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
class MenuItemListAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemListAPIView
from django.urls import path
from .views import MenuItemListAPIView
urlpatterns = [
    path('menu-items/', MenuItemListAPIView.as_view(), name='menu-items'),
]                              