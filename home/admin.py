from django.db import models
class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
from django import forms
class ContactForm(forms.Form):
    email = forms.EmailField(label='Your Email', required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must end with @example.com") 
            return email
from django.shortcuts import render, redirect
from .forms import Contact
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f"Email: {email}, Message: {message}")
            return redirect('success_url')
       else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

