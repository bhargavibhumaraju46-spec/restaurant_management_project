from django.shortcuts import render
RESTAURANT_PHONE_NUMBER = '+91-1234567890'
from django.db import models
class Restaurant(models.Model):
    phone_number = models.CharField(max_length=20)
    from django.shortcuts import render
    from django.conf import settings
def homepage(request):
    return render(request, 'homepage.html', {'phone_number': settings.RESTAURANT_PHONE_NUMBER})
from django.shortcuts import render
from .models import Restaurant
def homepage(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'homepage.html', {'phone_number': restaurant.phone_number})    