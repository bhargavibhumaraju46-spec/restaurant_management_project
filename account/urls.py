#orders/models.py
from django.db import models
class ordermanager(models.mamager):
    def pending_orders(self):
        return self.filter(status='pending')
        def shipped_orders(self):
            return self.filter(status='shipped')
            def by_status(self,status):
                return self.filter(status=status)