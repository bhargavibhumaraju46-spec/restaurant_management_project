from django.db import models
class Restaurant(models.Model):
    description = models.TextField()
from django import forms
from .models import Restaurant
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['description']
from django.shortcuts import render, redirect
from .forms import RestaurantForm
def add_description(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about_us')
        else:
            form = RestaurantForm()
         return render(request, 'add_description.html', {'form': form})
  from django.shortcuts import rende
  rfrom .models import Restaurant 
  def about_us(request):
    description = Restaurant.objects.first()
    return render(request, 'about_us.html', {'description': description})
