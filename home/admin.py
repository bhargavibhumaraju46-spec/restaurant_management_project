from rest_framework.views.import APIView
from rest_framework.response import response
from rest_framework import serializer
menu_items = [
    {"dish_name": "Pasta Carbonara", "Classic creamy pasta with pancetta", "price": 12.99},
    {"dish_name": "Margherita Pizza", "description": "Tomato, mozzarella, and basil", "price":10.50},
]
class MenuAPIView(APIView):
    def get(self, request):
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)
from django.urls import path
from .views import MenuAPIView
urlpatterns = [
    path('menu/', MenuAPIView.as_view(), name='menu_api'),
]
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('menu_app.urls')),
]