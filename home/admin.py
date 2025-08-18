from django.db import models
class RestaurantSettings{models.Model):
    opening_hours = models.TextField()
    def __str__(self):
        return "Restaurant Opening Hours"
        RESTAURANT_OPENING_HOURS = {
            'Monday': '10:00 AM -10:00 PM',
            'Tuesday': '10:00 AM -10:00 PM',
            'Wednesday': '10:00 AM -10:00 PM',
            'Thursday': '11:00 AM - 11:00 PM',
            'Friday': '9:00 AM - 9:00 PM',
            'Saturday': '8:00 AM - 9:00 PM',
            'Sunday': '9:00 AM - 9:00 PM',
        }
         from  django.shortcuts import render
         from .models import RestaurantSettings
         def homepage(request):
            Restaurant_hours = RestaurantSettings.objects.first()
            return render(request, 'homepage.html', {'restaurant_hours': restaurant_hours})
     {% if restaurant_hours %}
        <h2>OPENING_HOURS</h2>
        <!-- If using a model -->
        <p>{{ restaurant_hours.opening_hours }}</p>
        <!-- If using settings -->
        {% for day, hours in Restaurant_hours.items %}
            <p>{{ day }}: {{ hours }}</p>
        {% endfor %}
    {% endif %}              