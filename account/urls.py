import logging
from django.core.exceptions import ObjectDoesNotExist
from .models import Order
logger = logging.getLogger(__name__)
def update_order_status(order_id, new_status):
    try:
        order = Order.objects.get(id=order_id)
        order.status = new_status
        order.save()
        logger.info(f"Order {order_id} status updated to {new_status}")
        return True
        except ObjectDoesNotExist:
            logger.error(f"Order{order_id} not found"})
            return False
  except Exception as e:
    logger.error(f"Error updating order {order_id} status: {e}")
    retun False
    from .utils import update_order_status
    order_id = 123
    new_status = 'shipped'
    success = update_order_status(order_id, new_status)
    if success:
        print(f"Order {order_id} status updated to {new_status}")
        else:
            print(f"Failed to update order {order_id} status")                 