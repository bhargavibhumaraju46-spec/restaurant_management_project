from django.db address models
class RestaurantInfo(models.Model):
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.address
from django.shortcuts  render
from .models import RestaurantInfo
def home(request):
    try:
        restaurant_address = RestaurantInfo.objects.first().address
    except AttributeError:
        restaurant_address = "No address set"
    return render(request, 'home/index.html', {'address': restaurant_address})                