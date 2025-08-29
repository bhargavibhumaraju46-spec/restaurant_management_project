class MenuItem
def __init__(self, name, description, price):
    self.name = name
    self.description = description
    self.price = price
    class Menu:
        def __init__(self):
            self.items = []
            def add_item(self, item):
                self.items.append(item)
                def search(self, query):
                    return [item for item in self.items if query.lower() in item.name.lower()]
                    def main():
              menu = Menu()
              menu.add_item(MenuItem("Burger", "a juicy beef burger", 150))
              menu.add_item(MenuItem("pizza", "a delicious italian pizza", 200))
              menu.add_item(MenuItem("salad", "a fresh mix of greens and vegetables", 100))          
              print("menu:")
              for i, item in enumerate(menu.items, start=1):
                print(f"{i}, {item.name} - {item.description} - {item.price}")
                while True:
                    query = input("enter a search query(or 'quit' to exit): ")
                if query.lower() == 'quit':
                    break
                    results = menu.search(query)
                    if results:
                        print("search results:")
                    for i, item in enumerate(results, start=1):
                        print(f"{i}. {item.name} - {item.description} - {item.price}")
                        else:
                             print("no results found.")
                     if __name__ == "__main__":
                        main()                