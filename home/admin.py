from django.shortcuts import render
def menu_view(request):
    menu_items = [
        {'name': 'Item 1', 'price':10.99},
        {'name': 'Item 2', 'price': 8.9},
        {'name': 'Item 3', 'price':7.9},
    ]
       return render(request,'menu.html', {'menu_items': menu_items})
from django.urls import path
from .import views
urlpatterns = [
    path('menu/', views.menu_view, name='menu_view'),
]       


