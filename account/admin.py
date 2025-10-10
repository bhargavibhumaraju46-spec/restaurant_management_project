from django.contri

# Register your models here.
Here's how you can implement a Django REST Framework API endpoint to retrieve restaurant informatio
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
        address = models.TextField()
            phone_number = models.CharField(max_length=20)
                opening_hours = models.TextField()
                    # Add any other important details as needed

                        def __str__(self):
                                return self.name
                                Step 2: Create a Serializer for Restaurant
                                In your `serializers.py`:
                                from rest_framework import serializers
                                from .models import Restaurant

                                class RestaurantSerializer(serializers.ModelSerializer):
                                    class Meta:
                                            model = Restaurant
                                                    fields = ['name', 'address', 'phone_number', 'opening_hours']
                                                    Step 3: Create the API View
                                                    In your `views.py`:
                                                    from rest_framework import generics
                                                    from .models import Restaurant
                                                    from .serializers import RestaurantSerializer

                                                    class RestaurantDetail(generics.ListAPIView):
                                                        queryset = Restaurant.objects.all()
                                                            serializer_class = RestaurantSerializer
                                                            Step 4: Define the URL for the API Endpoint
                                                            In your `urls.py`:
                                                            from django.urls import path
                                                            from .views import RestaurantDetail

                                                            urlpatterns = [
                                                                path('api/restaurant/', RestaurantDetail.as_view(), name='restaurant_detail'),
                                                                ]
                                                                Testing
                                                                You can test this API endpoint using tools like Postman or curl. Send a GET request to `/api/restaurant/`. You'll get a JSON response with the restaurant(s) data.

                                                                Example JSON response if you have a restaurant in the database:
                                                                [
                                                                    {
                                                                            "name": "My Restaurant",
                                                                                    "address": "123 Street, City",
                                                                                            "phone_number": "1234567890",
                                                                                                    "opening_hours": "10 AM - 10 PM"
                                                                                                        }
                                                                                                        ]

                                                                                                        Let me know if you need further help or if you'd like me to adjust anything! 😊