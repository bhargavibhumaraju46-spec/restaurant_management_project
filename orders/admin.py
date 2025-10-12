from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        rating = models.IntegerField()
            text = models.TextField()

            from rest_framework import serializers
            from .models import Review

            class ReviewSerializer(serializers.ModelSerializer):
                class Meta:
                        model = Review
                                fields = ['user', 'rating', 'text']
                                from rest_framework.response import Response
                                from rest_framework import status
                                from rest_framework.views import APIView
                                from .models import Review
                                from .serializers import ReviewSerializer

                                class ReviewCreateAPIView(APIView):
                                    def post(self, request):
                                            serializer = ReviewSerializer(data=request.data)
                                                    if serializer.is_valid():
                                                                serializer.save()
                                                                            return Response(serializer.data, status=status.HTTP_201_CREATED)
                                                                                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                                                                                    from django.urls import path
                                                                                    from .views import ReviewCreateAPIView

                                                                                    urlpatterns = [
                                                                                        path('reviews/', ReviewCreateAPIView.as_view(), name='create_review'),
                                                                                        ]