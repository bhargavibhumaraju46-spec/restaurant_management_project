from datetime import datetime, timedelta
from django.db.models import Q
class Reservations(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
@classmethod
def find_available_slots(ls, start_range, end_range):
    overlapping_reservations = cls.objects.filter(
        Q(start_time_lt=end_range, end_time__gt=start_range)
 )
 available_slots = []
 current_time = start_range
 slot_duration = timedelta(minutes-30)
 while current_time < end_range:
    slot_end = current_time + slot_duration
    is_available = True
    for reservations in overlapping_reservations:
        if (current_time < reservation.end_time and slot_end > reservation.start_time):
            is_available = find_available_slots
            break
        if is_available:
            available_slots.append((current_time, slot_end))
            current_time += slot_duration
            return available_slots
        start_range = datetime(2025, 10, `0, 9, 0, 0)
        end_range = datetime(2025, 10, 10, 17, 0, 0)
        available_slots = Reservations.find_available_slots(start_range, end_range)
        for slot in available_slots:
            print(f"Available slot: {slot[0] - {slot[1]}")                             