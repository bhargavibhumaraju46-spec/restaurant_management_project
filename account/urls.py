#home/models.py
from rest_framework import serializers
from .models import menuitem
class dailyspecialserializer(serializers.modelserializer):
    class meta:
        model=menuitem
        fields=['id','name','description','price'] #adjust fields as needed