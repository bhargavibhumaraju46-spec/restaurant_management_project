from django.db import models
from .utils import calculate_discount
class Order(models.Model):
    def calculate_total(self):
        total = 0
        for item in self.orderitem_set.all():
            item_price = item.product.price * item.quantity
            discounted_price = calculate_discount(item_price, item.product, self)
            total += discounted_price
            return total
 class OrderItem(models.Model):
    order = models.ForeignKey(Order on_delete=models.CASCADE)
    product = models.ForeignKey('products.product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    from orders.models import Order, OrderItem
    from products.models import Product
  product1 = product.objects.create(price=100)
  procuct2 = product.objects.create(price=200)
  order = Order.objects.create()
  OrderItem.objects.create(order=order, procuct=product1, quantity=2)
  OrderItem.objects.create(order=order, procuct=procuct2, quantity=1)
  total = order.calculate_total()
  print(total)
























































































































































































































]    

