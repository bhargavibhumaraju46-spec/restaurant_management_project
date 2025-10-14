from django.db import models
class Restaurant(models.Model):
    opening_hours = models.CharField(max_length=50, dafault="11:00 AM - 11:00 PM (EST)")
from rest_framework.response import response
from rest_framework.views import APIView
from .models import Restaurant
class RestaurantHourView(APIView):
    def get(self, request):
        restaurant = Restaurant.objects.first()
        if restaurant:
            return Response({"opening_hours": restaurant.opening_hours})
        else:
            return Response({"error": "No restaurant found"},status=404)
from django.urls import path
from .views import RestaurantHourView
urlpatterns = [
    path('restaurant/hours/', RestaurantHourView.as_view(), name='restaurant-hours'),
]                