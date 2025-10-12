
from django.db import models
class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
        def __str__(self):
    from rest_framework import serializers
    from .models import MenuCategory
    
    class MenuCategorySerializer(serializers.ModelSerializer):
        class Meta:
                model = MenuCategory
                        fields = ['id', 'name']            return self.name
                        from rest_framework.generics import ListAPIView
                        from .models import MenuCategory
                        from .serializers import MenuCategorySerializer

                        class MenuCategoryListAPIView(ListAPIView):
                            queryset = MenuCategory.objects.all()
                                serializer_class = MenuCategorySerializer
                                from django.urls import path
                                from .views import MenuCategoryListAPIView

                                urlpatterns = [
                                    path('menu-categories/', MenuCategoryListAPIView.as_view(), name='menu-category-list'),
                                    ]