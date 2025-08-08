from django.uts import render
def reservations(request):
    reutn render(request, 'reservations.html')
from django.urls import path
from .import views
urlpatterns = [path('reservations/', views.reservations, name='reservations'),
]    