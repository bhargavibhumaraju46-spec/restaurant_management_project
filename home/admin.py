from django.shortcuts import render
from django.db import DatabaseError
def my_view(request):
    try:
        data = MyModel.objects.all()
        return render(request, 'template.html', {'data': data})
    except DatabaseError as e:
        return render(request, 'error.html', {'error': str(e)})       





