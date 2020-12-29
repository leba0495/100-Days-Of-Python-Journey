class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints report of resources available."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        sufficient_resource = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                sufficient_resource = False
                print(f"Sorry not enough {item}")
        return sufficient_resource

    def make_coffee(self, order):
        """Deducts the required ingredients from resources"""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕. Enjoy!️")
