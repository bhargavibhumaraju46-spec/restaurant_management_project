from rest_framework.decorators import api_view
from rest_framework.response import response
from rest_framework import status
from .models import Order
@api_view(['GET'])
def get_order_status(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        return Response({'order_id': order.id, 'status': order.satus})
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
from django.urls import path
from .views import get_order_status
urlpatterns = [
    path('order/<int:order_id>/status/', get_order_status, name='get_order_status'),
]                         