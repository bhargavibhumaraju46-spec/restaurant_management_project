from django.db import models
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status    
from .models import Order
from .serializers import OrderSerializer
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def cancel_order(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
            order.status = 'Cancelled'
            order.save()
            return Response({"message": "Order cancelled"}, status=status.HTTP_200_OK)
          except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
from django.urls import path
form rest_framework import routers
from .views import OrderViewSet
router = routers.DefaultRouter()
router.register(r'order', OrderViewSet, basename='orders')
urlpatterns = [
    path('orders/<int:pk>/cancel/', OrderViewSet.as_view({'delete': 'cancel_order'}), name='cancel-order'),
] + router.urls               