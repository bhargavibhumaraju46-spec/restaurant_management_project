from django.db import models
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
from django import forms
from .models import ContactSubmission
class contactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email']
from django.shortuts import render, redirect
from .forms import ContactForm
def homepage(request):
    if request.method == 'POST'
    form  = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('homepage')
        else:
            form = ContactForm()
        return render(request, 'homepage.html', {'form': form})       

