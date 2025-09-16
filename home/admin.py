from django.db import models
class OrderStatus(model.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
        PENDING = 'pending'
        PROCESSING = 'processing'
        COMPLETED = 'completed'
        CANCELLED = 'cancelled'                   