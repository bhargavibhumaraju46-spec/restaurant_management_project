from django import template
register = template.Library()
@register.filter('coming_soon')
def coming_soon(item):
    if not item.available:
        return "Coming Soon"
     return item.name
{% load menu_filters %}
{% for item in menu_items %}
   {{ item|coming_soon }} 
{% endfor %}     

    
    
    
    
    