from django.db import models
class Restaurant(models.Model):
    address = models.TextField()
    def __str__(self):
        return "Reataurant Details"
from django.shortcuts import render
from .models import Restaurant
def contact_us(request):
    try:
        restaurant = Restaurant.objects.first()
        address = restaurant.address
    except AttributeError:
        address = "Address not set."
    return render(request, 'contact_us.html', {'address': address})
    from django.urls import path
    from .views import contact_us
    urlpatterns = [
        path('contact-us/', contact_us, name='contact_us'),
    ]
