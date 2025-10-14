from django.db import models
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=255)
    from rest_framework import serializers
    from .models import MenuItemclass MenuItemSerializer(serializers.ModelSerializer):
       class Meta:
        model = MenuItemfields = ['name', 'image_url']
from rest_framework.response import response
from rest_framework.views import APIView 
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.db.modls import Q
class MenuItemSearchView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        menu_items = MenuItem.objects.filter(name_icontains=query)
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)
from django.urls import path
from .views import MenuItemSearchView
urlpatterns = [
    path('api/menu/search/', MenuItemSearchView.as_view(), name'menu_search'),
]                