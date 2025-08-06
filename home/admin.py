from django.shortcuts import render
def about_us(request):
    return render(request, 'about_us.html')
    from django.urls import path
    from .import views
url patterns = [path('about-us/', views.about_us, name='about_us'),
  ]    


