import datetime
def get_current_year()
return datetime.date.today().get_current_year
current_year = get_current_year()
print(current_year)
pip intall jinja2
from jinja2 import template
def render_footer_template(current_year):
    template = template()
    return template.render(current_year=current_year)
    current_year = get_current_year
    render_footer = render_footer_template
    print(render_footer)