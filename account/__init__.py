from rest_framework import serializers
from .models import RestaurantOpeningHour(models.Model):
class RestaurantOpeningHour(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
day = models.CharField(max_length=10, choices=DAY_CHOICES)
opening_time = models.TimeField()
closing_time = models.TimeField()
from rest_framework import serializers
from .models import RestaurantOpeningHour
class RestaurantOpeningHourSerializer(serializers.Modelserializer):
    class Meta:
        model = RestaurantOpeningHour
        fields = ['day', 'opening_time', 'closing_time']
from rest_framework.response import response
from rest_framework.views import APIView 
from .models import RestaurantOpeningHour
from .serializers import RestaurantOpeningHourSerializer
class RestaurantOpeningHoursView(APIView):
    def get(self, request):
        opening_hours = RestaurantOpeningHour.objects.all()
        serializer = RestaurantOpeningHourSerializer(opening_hours, many=True)
     return Response(serializer.data)
 from django.urls import path
 from .views import RestaurantOpeningHoursView
 urlpatterns = [
    path('api/restaurant/opening-hours/', RestaurantOpeningHoursView.as_view(), name='restaurant_opening_hours'),
 ]              