from rest_framework.response import response
from rest_framework import status
from rest_framework.views import APIView
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.db.models import Q
class MenuItemByPriceRangeView(APIView):
    def get(self, request):
        try: 
            min_price = request.GET.get('min_price', None)
            max_price = request.GET.get('max_price', None)
        if min_price is None or max_price is None:
            return Response({"error": "Both min_price and max_price are required."}, status=status.HTTP_400_BAD_REQUEST)
            try:
                min_price = float(min_price)
                max_price = float(max_price)
            except ValueError:
                return Response({"error": "Invalid price values. prices must be numbers."}), status=status.HTTP_400_BAD_REQUEST)
                if min_price > max_price:
                    return Response({"error": "min_price cannot be greater than max_price."}), status=status.HTTP_400_BAD_REQUEST)
                    menu_items = MenuItem.objects.filter(price__gte=min_price, price_lte=max_price)
                    serializers = MenuItemSerializer(menu_items, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({"error": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)    