from django.shortcuts import render
def tom_404(request, exception):
    return render(request, '404.html', status=404)
    handler404 = 'your_app.views.custom_404'

