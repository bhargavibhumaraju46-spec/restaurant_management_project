from django.db import models
class Reservation(models.Model):
    name = models.CharField(max_length=254)
    date = models.DateTimeField()
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Reservation
def homepage(request):
    context = {
        'reservations_url': reverse_lazy('make_reservation'),
        'description': 'Book your spot easily with our reservation system.'
    }
    return render(request, 'homepage.html', context)
from django.urls import path
from .import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('make-reservation/', views.make_reservation, name='make_reservation'),
]
def make(request):
    return render(request, 'reservation.html')  