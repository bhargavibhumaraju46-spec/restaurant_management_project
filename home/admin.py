from django.shortcuts import render
from .models import RestaurantLocations
def homepage_view(request):
    try:
        restaurant = RestaurantLocation.objects.first()
    except RestaurantLocation.DoesNotExist:
        restaurant = None
    reurn render(request, 'homepage.html', {'restaurant': restaurant})
         