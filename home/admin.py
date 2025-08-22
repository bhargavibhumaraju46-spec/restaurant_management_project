from django.db import models
class Chef(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='chefs/')
    def __str__(self):
        return self.name
from django.shortcuts import render
from .models import Chef
def about_chef(request):
    chef = Chef.objects.first()
    return render(request, 'about_chef.html', {'chef':chef})
from django.urls import path
from .views import about_chef
urlpatterns = [
    path('about-chef/', about_chef, name='about_chef'),
]            
    