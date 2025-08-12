from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
from django.core.mail impor send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm
def contact_view(request):
    if request.method == 'POST'
    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message  = form.cleaned_data['message']
        send_mail(
            f"Message from {name}",
            message,
            email,
            ['restaurant_email@example.com'],
            fail_silently=False,
        )
        return HttpResponseRedirect('/thanks')
    else:
        form = ContactForm()
      return render(request, 'contact.html', {'form':form})      