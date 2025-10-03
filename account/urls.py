#orders/models.py
from django.db import models
class ordermanager(models.mamager):
    def pending_order(self):
        return self.filer(status='pending')
        class order(models.model):
            status_choices=[
                ('pending','pending'),
                ('shipped','shipped'),
                ('delivered','delivered'),
                ]
                status=models.charfield(max_length=10, choices=status_choices,default='pending')