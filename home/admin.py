from django. import render
from .models import Menu
def homepage(request):
    menu_items = Menu.objects.all()
    return render(request, 'homepage.html', {'menu_items': menu_items})  





