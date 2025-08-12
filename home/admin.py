from django.shortcuts import render
from .models import MenuItem
def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})
from django.urls import path
from .views import menu_view 
urlpatterns = [
    path('menu/', menu_view, name='menu'),
]      