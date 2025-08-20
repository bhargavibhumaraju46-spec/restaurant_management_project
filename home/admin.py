class Form(forms.Form):
    name = forms.CharField(max_length=100)
    message = formsCharField(widget=forms.Textarea)
    email = forms.EmailField(label='Your email')
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
from django.shortcuts import render
from .forms import ContactForm
def contact_view(request):
    if request.method == 'POST':
        form =  ContactForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data['email']
      return render(request, 'contact/success.html')
     else:
        form =CharField()
      return render(request, 'contact.html', {'form': form})                 