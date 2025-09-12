from django.urls import path
from .import views
urlpattern = [
    path('cart/', views.cart_view, name='view_cart'),
]
from django.shortcuts import render
from .models import Cart
def cart_views(request):
    cart_items = Cart.objects.filter(User=request.user)
    return render(request, 'cart.html', {'cart_item': cart_items})