from django.db import models
class MenuItems(models.Model):
    name = models.harField(max_length=100)
    description = models.TextField()
    price = models.decimalField(max_digits=10, decimal_places=2)
python manage.py makemigrations
python manage.py migrate    
