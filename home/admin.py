from django.shortcuts import render
def home(request):
    context = {
        'restaurant_name': 'Tasty Bites,
        'welcome_message': 'Enjoy your dining experience!',
    }
    return render(request, 'restaurant/home.html', context)
    from django.urls import path
    from . import views
    urlpatterns = [
        path('', views.home, name='home'),
    ]
    from django.contrib import admin
    from django.urls
    import include, path
    urlpatterns = [path('admin/', admin.site.urls),path('', include('restaurant.urls')),
    ]

