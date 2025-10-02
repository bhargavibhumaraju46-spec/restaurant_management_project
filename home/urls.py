from django.db import models
from users.models import users
class Order(models.Model):
    STATUS_CHOICESS = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICESS, default='pending')
    user = modls.ForeignKey(User, )on_delete=models.CASCADE)
from rest_framework import Serializers
from .models import Order
class OrderStatusSerializer(Serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =['id', 'staus']
from rest_framework import status
from rest_framework.response import Response        
from rest_framework.views import APIView
from .models import Order
from .serializers import OrderStatusSerializer
class UpdateOrderStatusView(APIView):
    def put(self, request, order_id):
        try:
            order = Order.objects.get(id = order_id)
            except Order.DoesNotExist:
                return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
                new_status = request.data.get('status')
                if new_status not in ['pending', 'processing', 'completed']:
                    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
                    order.status = new_status
                    order.save()
                    serializer = OrderStatusSerializer(order)
                    return Response(serializer.data, status.HTTP_200_OK)
from django.urls import path
from .views import UpdateOrderStatusView
                    urlpatterns = [
                        path('order/<int:order_id>/status/', UpdateOrderStatusView.as_view(), name='update-order-status'),
]    

