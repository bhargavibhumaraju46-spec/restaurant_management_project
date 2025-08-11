RESTAURANT_NAME = 'My Restaurant'
from django.db import models
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
from django.shortcuts import render
from .models import Restaurant
def homepage_view(request):
    restaurant = Restaurant.objects.first()
    return rende(request, 'homepage.html', {'reataurant': restaurant})    