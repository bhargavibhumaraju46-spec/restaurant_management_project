from django.shortcuts import render
from django.utils import timezone
def homepage(request):
    current_time = timezone.now()
    return render(request, 'homepage.html', {'current_time': current_time})          

