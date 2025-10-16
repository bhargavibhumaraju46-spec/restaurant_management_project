from django.db import models
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    opening_hours = models.CharField(max_length=200, default="11:00 AM - 11:00 PM (EST)")
    def __str__(self):
        return self.name
from rest_framework import generics
from rest_framework import serializer
from .models import Restaurant
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['opening_hours']
   class OpeningHoursView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    def get_queryset(self):
        return Restaurant.objects.all()[:1]
from django.urls import path
from .views import OpeningHoursView
urlpatterns = [
    path('restaurant-hours/', OpeningHoursView.as_view(), name='restaurant-hours'),
]                        