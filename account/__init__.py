[10/10, 11:35 p Here's a basic implementation of the API endpoint using Django REST Framework to update the availability status of a menu item.

models.py
from django.db import models

class MenuItem(models.Model):
    # Other fields for MenuItem model
        is_available = models.BooleanField(default=True)
        serializers.py
        from rest_framework import serializers
        from .models import MenuItem

        class MenuItemAvailabilitySerializer(serializers.ModelSerializer):
            class Meta:
                    model = MenuItem
                            fields = ['id', 'is_available']
                            views.py
                            from rest_framework import status
                            from rest_framework.response import Response
                            from rest_framework.views import APIView
                            from .models import MenuItem
                            from .serializers import MenuItemAvailabilitySerializer

                            class UpdateMenuItemAvailability(APIView):
                                def patch(self, request, pk):
                                        try:
                                                    menu_item = MenuItem.objects.get(pk=pk)
                                                                serializer = MenuItemAvailabilitySerializer(menu_item, data=request.data, partial=True)
                                                                            if serializer.is_valid():
                                                                                            serializer.save()
                                                                                                            return Response({"message": "Menu item availability updated successfully"}, status=status.HTTP_200_OK)
                                                                                                                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                                                                                                                                except MenuItem.DoesNotExist:
                                                                                                                                            return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)
                                                                                                                                            urls.py
                                                                                                                                            from django.urls import path
                                                                                                                                            from .views import UpdateMenuItemAvailability

                                                                                                                                            urlpatterns = [
                                                                                                                                                path('menu-items/<int:pk>/availability/', UpdateMenuItemAvailability.as_view(), name='update-menu-item-availability'),
                                                                                                                                                ]
                                                                                                                                                Example Usage
                                                                                                                                                You can update the availability of a menu item by sending a `PATCH` request to `/menu-items/<menu_item_id>/availability/` with the JSON body:
                                                                                                                                                {
                                                                                                                                                    "is_available": true/false
                                                                                                                                                    }

                                                                                                                                                    This code assumes you have Django and Django REST Framework set up in your project. It creates an API endpoint to update the `is_available` field of a `
                                                                                                                                                    [10/10, 11:35 pm] Meta AI: Here's a basic implementation of the API endpoint using Django REST Framework to update the availability status of a menu item.

                                                                                                                                                    models.py
                                                                                                                                                    from django.db import models

                                                                                                                                                    class MenuItem(models.Model):
                                                                                                                                                        # Other fields for MenuItem model
                                                                                                                                                            is_available = models.BooleanField(default=True)
                                                                                                                                                            serializers.py
                                                                                                                                                            from rest_framework import serializers
                                                                                                                                                            from .models import MenuItem

                                                                                                                                                            class MenuItemAvailabilitySerializer(serializers.ModelSerializer):
                                                                                                                                                                class Meta:
                                                                                                                                                                        model = MenuItem
                                                                                                                                                                                fields = ['id', 'is_available']
                                                                                                                                                                                views.py
                                                                                                                                                                                from rest_framework import status
                                                                                                                                                                                from rest_framework.response import Response
                                                                                                                                                                                from rest_framework.views import APIView
                                                                                                                                                                                from .models import MenuItem
                                                                                                                                                                                from .serializers import MenuItemAvailabilitySerializer

                                                                                                                                                                                class UpdateMenuItemAvailability(APIView):
                                                                                                                                                                                    def patch(self, request, pk):
                                                                                                                                                                                            try:
                                                                                                                                                                                                        menu_item = MenuItem.objects.get(pk=pk)
                                                                                                                                                                                                                    serializer = MenuItemAvailabilitySerializer(menu_item, data=request.data, partial=True)
                                                                                                                                                                                                                                if serializer.is_valid():
                                                                                                                                                                                                                                                serializer.save()
                                                                                                                                                                                                                                                                return Response({"message": "Menu item availability updated successfully"}, status=status.HTTP_200_OK)
                                                                                                                                                                                                                                                                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                                                                                                                                                                                                                                                                                    except MenuItem.DoesNotExist:
                                                                                                                                                                                                                                                                                                return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)
                                                                                                                                                                                                                                                                                                urls.py
                                                                                                                                                                                                                                                                                                from django.urls import path
                                                                                                                                                                                                                                                                                                from .views import UpdateMenuItemAvailability

                                                                                                                                                                                                                                                                                                urlpatterns = [
                                                                                                                                                                                                                                                                                                    path('menu-items/<int:pk>/availability/', UpdateMenuItemAvailability.as_view(), name='update-menu-item-availability'),
                                                                                                                                                                                                                                                                                                    ]
                                                                                                                                                                                                                                                                                                    Example Usage
                                                                                                                                                                                                                                                                                                    You can update the availability of a menu item by sending a `PATCH` request to `/menu-items/<menu_item_id>/availability/` with the JSON body:
                                                                                                                                                                                                                                                                                                    {
                                                                                                                                                                                                                                                                                                        "is_available": true/false
                                                                                                                                                                                                                                                                                                        }

                                                                                                                                                                                                                                                                                                        This code assumes you have Django and Django REST Framework set up in your project. It creates an API endpoint to update the `is_available` field of a `MenuItem` using its ID. Error handling is included for cases like invalid input or if the menu item doesn't exist.