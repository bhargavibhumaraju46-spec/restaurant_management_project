from django.db import models
class RestaurantInfo(models.Model):
    address = models.CharField(max_length=255)
 def __str__(self):
    return self.address 
from django.shortcuts import render
from .models import RestaurantInfo
def homepage(request):
    try:
        restaurant_info = RestaurantInfo.objects.get(id=1)

    except RestaurantInfo.DoesNotExist:
        restaurant_info = RestaurantInfo.objects.create(address="Default Address if needed")    
return render(request, 'home/homepage.html', {'address': restaurant_info.address}) 
from django.contrib import admin
from .models import RestaurantInfo
admin.site.register(RestaurantInfo)