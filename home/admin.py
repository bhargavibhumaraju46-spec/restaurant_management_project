from django.db import models
class Restaurant(models.Model):
    email = models.EmailField(max_length=254, blank=True, null=True)
from django.shortcuts import render
from .models import Restaurant
def contact_us(request):
    restaurant = Restaurant.objects.first()
    return render(request,'contact_us.html', {'restaurant':restaurant})