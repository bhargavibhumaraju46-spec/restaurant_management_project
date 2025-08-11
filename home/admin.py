from django.db import models
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
from django import forms
from .models import ContactSubmission
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email']
from django.shortcuts import render, redirect
from .forms import ContactForm
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_view')
        else:
            form = ContactForm()
            return render(request, 'contact.html', {'form': form})            