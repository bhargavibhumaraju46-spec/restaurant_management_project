EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.TextArea)
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm 
def contact_view(request):
    if request.method == 'POST'
    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message'] 
      send_mail(
        'Contact Form Submission',
        f'Thank you for contacting us, {name}. we will get back to you.',
        'your-email@gamil.com',
        [email],
        fail_silently=False,
      )    
      return HttpResponseRedirect('/thanks/')
      else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
from django.urls import path
from .views import contact_view
urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('thanks/', lambda request:render(request, 'thanks.html')),
    ]
]       