from django.shortcuts import render
def contact_us(request):
    return request, 'contact_us.html')
from django.urls import path
fron .import views
urlpatterns = [path('contact-us/', views.contact_us, name='contact_us'),
]
