from go.db import models
class RestaurantInfo(models.Model):
    opening_hours = models.TextField()
    def __str__(self):
        return "Restaurant Info"
from .models import RestaurantInfo
def opening_hours(request):
    try:
        info = RestaurantInfo.objects.first()
        return {'opening_hours': info.opening_hours}
    except AttributeError:
        return {'opening_hours': 'Mon-Sat 10am-10pm, Sun 10am-8pm'}
      TEMPLATES = [
        {
            'OPTIONS': {
                'context_processors':[
                    'your_app.context.opening_hours',
                ],
            },
        },
    ]
                                   