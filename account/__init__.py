from django.db import models
class MenuItem(models.Model):
    cuisine = models.CharField(max_length=255)
    @classthod
    def get_by_cuisine(cls, cuisine_type):
        return cls.objects.filter(cuisine=cuisine_type)
from yourapp.models import MenuItemmenu_items = MenuItem.get_by_cuisine('Indian')
for item in menu_items:
    print(item)                             