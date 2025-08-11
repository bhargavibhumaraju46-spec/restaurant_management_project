from django.db import models
class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_lenth=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)