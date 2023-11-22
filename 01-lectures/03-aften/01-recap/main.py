"""
Recap from 2nd night lecture:
- object methods
- objects in objects
"""


class GroceryList:
    groceries = []

    def __init__(self, list_name, max_items=10):
        self.list_name = list_name
        self.max_items = max_items

    def add_item(self, item):
        if len(self.groceries) < self.max_items:
            self.groceries.append(item)

    def print_header(self):
        print(f"\n*** {self.list_name} ***\n".upper())

    def print_grocery_items(self):
        for item in self.groceries:
            print(item)
        print()

    def print_total_cost(self):
        cost = 0
        for item in self.groceries:
            cost += item.get_price()
        print(f"TOTAL:\t {cost}")

    def print_groceries_list(self):
        self.print_header()
        self.print_grocery_items()
        self.print_total_cost()


class Item:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self) -> str:
        return f"{self.item}:\t {self.price}"


my_groceries = GroceryList("My awesome groceries list")

stuff_to_buy = [
    Item("Milk", 10),
    Item("Coffee", 40),
    Item("Butter", 20),
    Item("Beer", 12),
]

for el in stuff_to_buy:
    my_groceries.add_item(el)

my_groceries.print_groceries_list()
