from datetime import date
from django.db.models import Sum
from .models import Order
def get_daily_sales_total(date: date) -> float:
    total = Order.objects.filter(created_at_date=date).aggregate(total_sum=Sum('toal_price'))['total_sum'] or 0
    return total    