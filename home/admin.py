from django.db import models
class SocialMediaLink(models.Model):
    platform = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    url = models.URLField()
    def __str__(self):
        return self.platform
from django.contrib import admin
from .models import SocialMediaLink
admin.site.register(SocialMediaLink)
from django.shortcuts import render
from .models import SocialMediaLink
def homepage(request):
    social_links = SocialMediaLink.objects.all()
    return render(request, 'homepage.html', {'social_links': social_links})        