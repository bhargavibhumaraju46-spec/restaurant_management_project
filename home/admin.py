restaurant_hours = {
    "Monday": "9:00 AM - 10:00 PM", 
    "Tuesday": "9:00 AM - 10:00 PM",
    "Wednesday": "9:00 AM - 10:00 PM",
    "Thursday": "10:00 AM - 10:00 PM",
    "Friday": "10:00 AM - 10:00 PM",
    "Saturday": "10:00 AM - 10:00 PM",
    "Sunday": "10:00 AM - 10:00 PM",
 }
 def display_opening_hours(hours):
    print("--- Restaurant Opening Hours --- ")   
    for day, time in hours.items():
        print(f"{day}: {time}")
    print("----------------")
display_opening_hours(restaurant_hours)        