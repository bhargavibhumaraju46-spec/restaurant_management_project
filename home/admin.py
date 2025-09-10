from django.db import model
class MenuItem(models.Model):
    name = models.CharField(max_length=255)   
    description = models.TextField()
from django.shortcuts import render
from .models import MenuItem
from django.db.models import Q
def menu(request):
    query = request.GET.get('q')
    if query:
        menu_items = MenuItem.objects.filter(Q(name__icontains=query))
    else:
        menu_items = MenuItem.objects.all()
        return render(request, 'menu/menu.html', {'menu_item':menu_items})
from django.urls import path
from .views import menu
urlpatterns = [
    path('',menu, name='menu'),
]           