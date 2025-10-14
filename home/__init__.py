from django.db import models
from django.contrib.auth.models import User
from restaurants.models import restaurants
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.pagination import PageNumberPagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50
class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        restaurant_id = self.kwargs.get('restaurant_id')
        if restaurant_id:
            return Review.objects.filter(restaurant_id=restaurant_id).order_by('-created_at') 
           return Review.objects.all().order_by('-created_at')
from rest_framework import serializers
from .models import Review                
from django.contrib auth.models import User
from restaurants.serializers import RestaurantSerializer
class ReviewSerializer(serializer.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)
class Meta:
    model = Review
    fields = ['id', 'user', 'restaurant', 'review_text', 'rating', 'created_at']