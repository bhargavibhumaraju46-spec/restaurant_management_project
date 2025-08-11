from django.db import models
from django.contrib.auth.models import User
from .models import Menu
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(Menu)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, choices=[
        ('pending', 'pending'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled')
    ], default='pending')  





