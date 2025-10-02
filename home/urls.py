from django.db import models
class Order(models.Model):
    STATUS_CHOICESS = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICESS, default='pending')
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
    def post(self, request):
        order_id = request.data.get('order_id')
        new_status = request.data.get('status')
        try:
            order = Order.objects.get(id = order_id)
            except Order.DoesNotExist:
                return Response({"error": "Invalid order ID"}, status=status.HTTP_400_BAD_REQUEST)
                if new_status not in [choice[0] for choice inOrder.STATUS_CHOICESS]:
                    return Response({'error': 'Invalid status update'}, status=status.HTTP_400_BAD_REQUEST)
                    order.status = new_status
                    order.save()
                    serializer = OrderStatusSerializer(order)
                    return Response(serializer.data, status.HTTP_200_OK)
from django.urls import path
from .views import UpdateOrderStatusView
                    urlpatterns = [
                        path('update-order-status/', UpdateOrderStatusView.as_view(), name='update-order-status'),
]    

