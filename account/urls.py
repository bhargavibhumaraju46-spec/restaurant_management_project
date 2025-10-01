from datetime import datetim, time
def is_restaurant_open():
    opening_hours = {
        "Monday": (time(9, 0), time(22, 0)),
        "Tuesday": (time(9,0), time(22, 0)),
        "Wednesday": (time(9, 0), time(22, 0)),
        "Thursday": (time(9, 0)), time(22, 0)),
        "Friday": (time(9, 0)), time(22, 0)),
        "Saturday": (time(9, 0)), time(22, 0)),
        "Sunday": (time(9, 0)), time(22, 0)),
       }
       now  = datetime.now()
       current_day = now.strftime("%A")
       current_time = now.time()
       open_time, close_time = opening_hours[current_day]
       return open_time <= current_time <= close_time
       from home.utils impport is_restaurant_open
       print(is_restaurant_open)