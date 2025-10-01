from rest_framework import serializers
from .models import Table
class TableSerializer(serializers.Modelserializer):
    class Meta:
        model = Table
        fields = ['table_number', 'capacity', 'is_available']
from rest_framework import generics
from .models import Table
from .serializers import TableSerializer
class AvailableTableAPIView(generics.ListAPIView):
    serializer_class = TableSerializer
    def get_queryset(self):
        return Table.objects.filter(is_available=True)
        from django.urls import path
        from .views import AvailableTableAPIView
  urlpatterns = [
    path('api/tables/available/', AvailableTableAPIView.as_view(), name='available_tables_api'),
    ]      