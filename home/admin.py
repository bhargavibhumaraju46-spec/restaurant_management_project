from django.db import models
from django.contrib.auth.models import User
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
class Item(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
 from rest_framework import serializers
 from .models import Order, Item
 class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price'] 
class OrderSerializer(serilaizers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'date', 'total_price', 'items']
from rest_framework import generics
from rest_framework.permissins import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer  
class OrderHistoryView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
from django.urls import path
from .views import OrderHistoryView
urlpatterns = [
    path('order-history/', OrderHistoryView.as_view(), name='order_history'),
]        