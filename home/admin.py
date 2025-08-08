from django.db import models
from django.contrib.auth.models import user
class userProfile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)   





