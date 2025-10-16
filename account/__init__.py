from rest_framework.response import Response
from response import status
from rest_framework.views import APIView
from .models import  MenuItem
from .serializers import MenuItemAvailabilitySerializer
class MenuItemAvailabilityView(APIView):
    def get(self, request, item_id):
        try:
            menu_item = MenuItem.objects.get(id=item_id)
            serializer = MenuItemAvailabilitySerializer({'available': menu_item.is_available})
            return Response(serializer.data)
        except MenuItem.DoesNotExist:
            return Response({'error': 'Menu item not found'}, status=status.HTTP_404_NOT_FOUND) 
from rest_framework import serializers
class MenuItemAvailabilitySerializer(serializers.Serializer):
    available = serializers.BooleanField()
from django.urls import path
from .views import MenuItemAvailabilityView
urlpatterns = [
    path('menu-items/<int:item_id>/availibility/', MenuItemAvailabilityView.as_view(), name='menu-item-availibility'),
]                  
