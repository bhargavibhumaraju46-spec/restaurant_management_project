from django.db import models
class Restaurant(models.Model):
    def get_total_menu_items(self):
        return self.menuitem_set.count()
class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)                     