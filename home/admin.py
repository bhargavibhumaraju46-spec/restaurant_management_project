from rest_framework import generics
from .models import MenuCategory
from .serializers import MenuCategorySerializer
from rest_framework import serializers
from .models import MenuCategory
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['name']
from rest_framework import generics
from .models import MenuCategory
from .serializers import MenuCategorySerializer
class MenuCategoryList(generics.ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
from django.urls import path
from .views import MenuCategoryList
urlpatterns = [
    path('menu-categories/', MenuCategoryList.as_view(), name='menu-categories'),
]                    