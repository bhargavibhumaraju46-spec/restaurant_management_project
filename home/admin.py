from django.db import models
class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    description = models.TextField(blank=True)
 def __str__(self):
    return self.address 
from django.shortcuts import render
from .models import RestaurantLocation.objects.first()
context = {'location': location}
return render(request, 'locations.html', context) 
from django.urls import path
from .import views
urlpatterns = [
    path('locations/', views.locations, name='locations'),
]     
from django.contrib import admin
from .models import RestaurantLocation
admin.site.register(RestaurantLocation
)