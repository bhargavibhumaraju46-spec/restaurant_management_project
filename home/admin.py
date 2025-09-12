from django.urls import path
from .import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('manu/', views.menu, name='menu'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),        
    ]
from django.shortcuts import render
def homepage(request):
    return render(request, 'homepage.html')
def menu(request):
    return render(request, 'menu.html')
def about_us(request):
    return render(request, 'about_us.html')
def contact_us(request):
    return render(request, 'contact_us.html')            