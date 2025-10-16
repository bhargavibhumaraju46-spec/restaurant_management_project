from django.db import models
class Order(models.Model):
    def get_total_item_count(self):
        total_count = sum(item.quantity for item imn self.items.all())
        return total_count
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='item', on_delete=models.CASCADE)
    quantity = models.IntegerField()                                     