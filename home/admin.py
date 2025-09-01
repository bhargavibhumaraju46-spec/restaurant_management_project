from django.shortcuts import  render
def contact(request):
    opening_hours = {
        "Monday": "9:00 AM - 10:00 PM",
        "Tuesday": "9:00 AM - 10:00 PM",
        "Wednesday": "9:00 AM - 10:00 PM",
        "Thursday": "9:00 AM - 10:00 PM",
        "Friday": "9:00 AM - 10:00 PM",
        "Saturday": "9:00 AM - 10:00 PM",
        "Sunday": "9:00 AM - 10:00 PM",
    }
      return render(request, "contact.html", {"opening_hours":opening_hours})
<!DOCTYPE html>
<html>
<head>
    <title>ontact Us</title>
    <style>
       body {font-family:Arial, sans-serif; text-align:center; margin:30px; }
              hours-box {
                display: inline-block;
                padding: 20px solid
                border-radius: 10px;
                background:
              }
              h2 {color:}
              u1 {list-style:none;
              padding: 0; }
              li {margin: 8px 0; }
              </style>
              </head>
              <body>
              <h1>contact Us</h1>
              <div class ="hours-box">
                <h2>Opening Hours</h2>
                <u1>
                {% for day, hours in opening_hours.items %}
                <li><strong>{{ day }}:</strong>
                {{ hours }}</li>
                     {% endfor %}
                      </ul>
                      </div>
                      </body>
                      </html>
from django.urls import path
from .import views
urlpatterns = [
    path('contact/', views.contact, name='contact'),
]                      