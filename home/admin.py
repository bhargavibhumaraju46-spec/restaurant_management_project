from django.db import models
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='restaurant_logos/')
from django.shortcuts import render
from .models import Restaurant
def homepage(request):
    restaurant = Reataurant.objects.first()
    return render(request, 'homepage.html',{'restaurant':restaurant})
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def homepage():
    logo_path = 'path_to_logo.jpg'
    return render_template('homepage.html', logo_path=logo_path)
<img src="{{ url_for('static', filename=logo_path) }}" alt="Restaurant Logo">    
