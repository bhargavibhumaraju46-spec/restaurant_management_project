from rest_framework import generics
from .models import Table
from .serializers import TableSerializer
class TableDetailView(generics.RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    lookup_field = 'pk'
from django.urls import path
from .views import TableDetailView
urlpattern = [
    path('api/tables/<ink:pk>/', TableDetailView.as_view(), name='table-detail'),
]    