from django.shortcuts import render
def home(request):
    images = [
        "/static/images/img1.jpg",
        "/static/images/img2.jpg",
        "/static/images/img3.jpg",
    ]
    return render(request,
    "home.html", {"images": images})
<!DOCTYPE html>
<html>
<head>
    <title>Image Carousel</title>
    <style>
    carousel {
        width: 500px;
        height: 400px;
        margin: auto;
        overflow: hidden;
        position: relative;
    }   
    slides {
        display: flex;
        width: 100%;
        animation: slide 12s
 infinite;   
    }
    slides img {
        width: 600px;
        height: 400px;
    }
    @keyframes slide {
        0% {transform:
        translateX(0); }
        33% {transform:
        translateX(-600px); }
        66% {transform:
        translateX(-1200px); }
        100% {transform:
        translateX(0);}
    }
    </style>
    </head>
    <body>
    <h1
style="text-align:center;">Restaurant
Image Carousel</h1>
<div class="carousel">
<div class="slides">
{%for img in images %}
<img src="{{ img }}"
alt="carousel image">
{% endfor %}
</div>
</div>
</body>
</html>
from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    ]
