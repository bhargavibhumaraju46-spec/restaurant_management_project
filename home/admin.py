from django.db import models
class Subscriber(models.Model):
     email = models.Emailbield(unique=True)
     date_subscribed = models.DateTimeField(auto_now_add=True)
     def __str__(self):
        return self.email
from django import forms
from .models import Subscriber
class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
from django.shortcuts import render, redirect
from .forms import NewsletterSignupForm
def newsletter_Signup(request):
    if request.method = 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')
        else:
            form = NewsletterSignupForm()
            return render(request, 'newsletter_app/signup_form.html', {'form': form}) 
        def signup_success(request):
            return render(request, 'newsletter_app/signup_success.html')                       
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsletter/', include('newsletter_app.urls')),
]
from django.urls import path
from .import views
urlpatterns = [
    path('', views.newsletter_signup, name='newsletter_signup'),
    path('success/', views.signup_success, neme='signup_success'),
    ]