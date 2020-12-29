class MenuItem:
    """Models or specifies each menu item's attributes"""

    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:
    """Models the Menu with each item available"""

    def __init__(self):
        self.menu = [
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0),
        ]

    def get_item(self):
        """Returns the items available in the menu"""
        beverages = ""
        for item in self.menu:
            item = f"{item.name}/"
            beverages += item
        return beverages

    def find_drink(self, order_name):
        """Searches the menu for a ordered drink by name. Returns a MenuItem object if it exists,
        otherwise returns none"""
        for drink in self.menu:
            if drink.name == order_name:
                return drink
        print("Sorry that item is not available.")
