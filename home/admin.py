import datetime
class Restaurantpage:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.template = None
        self.navigation_link = None
def create_template(self, template_name):
    self.template = template_name
    print(f"template '{template_name}'created.")
def add_navigation_link(self, link_text, link_url):
    self.navigation_link = (link_text, link_url)
    print(f"navigation link '{link_text}' added with URL '{link_url}'. ")
def create_page(self):
    print(f"page '{self.title}' created with description: {self.description}")
    print(f"template: {self.template}")
    print(f"navigation link: {self.navigation_link[0]} - {self.navigation_link[1]}")
    def main():
        task_title = "our story"
        task_description = "a imple text description of the restaurant's history"
        task_due_date = datetime.date(2025, 8, 29)
        page = Restaurantpage(task_title, task_description)
        template_name = "our_story_template"
        page.create_template(template_name)
        link_text = "our story"
        link_url = "/our-story"
        page.add_navigation_link(link_text, link_url)
        page.create_page()
        today = date.time.date.today()
        if today == task_due_date:
            print("task is due today.ensuring all details are complete.")
       else:
        print("task is not due today.")
  if __name__ == "__main__":
    main()           

