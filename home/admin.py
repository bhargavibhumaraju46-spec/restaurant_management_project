from django.db import models
from .models import OrderStatus
class Order(models.Model):
    status = models.ForeignKey(OrderStatus, on_delete=model.SET_NULL, null=True)                   