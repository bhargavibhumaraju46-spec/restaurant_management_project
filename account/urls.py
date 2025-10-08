from rest_framework import serializers
from .models import UserReview
class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = ['id', 'menu_item', 'rating', 'comment']
        extra_kwargs = {
            'menu_item': {'required': True},
            'rating': {'required':True, 'min_value': 1, 'max_value': 5}
        }                  
from rest_framework import generics
from .models import UserReview
from serializers import UserReviewSerializer
class UserReviewCreateAPIView(generics.CreateAPIView):
    queryset = UserReview.objects.all()
    serializers_class = UserReviewSerializer
    def get_queryset(self):
        menu_item_id = self.kwargs.get('menu_item_id')
        return UserReview.objects.filter(menu_item_id=menu_item_id)
from djngo.urls import path
from .views import UserReviewCreateAPIView, UserReviewListByMenuItemAPIView
urlpatterns = [
    path('reviews/', UserReviewCreateAPIView.as_view(), name='create-review'),
    peth('reviews/menu-item/<int:menu_item_id>/' UserReviewListByMenuItemAPIView.as_view(), name='list-review-by-menu-item'),
    ]        