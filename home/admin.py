from django.db import models
class Restaurants(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
 RESTAURANT_NAME = 'Your Restaurant Name'
 from django.shortcuts import render
 from .models import Restaurant
def homepage(request):
    try:
        restaurant = Restaurant.objects.first()
        return render(request, 'homepage.html', {'restaurant_name': restaurant.name})
     except Restaurant.DoesNotExist:
        return render(request, 'homepage.html', {'restaurant_name':'Default Name'}) 
from django.shortcuts import render
from django.conf import settings
def homepage(request, 'homepage.html', {'restaurant_name: settings.RESTAURANT_NAME'})
from django .urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    ]

