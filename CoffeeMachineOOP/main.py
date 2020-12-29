from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
from click import clear

menu = Menu()
barista = CoffeeMaker()
cashier = MoneyMachine()


def main():
    print(logo)
    continue_loop = True
    while continue_loop:
        user_choice = input(f"What would you like? ({menu.get_item()}) ").lower()
        if user_choice == "off":
            continue_loop = False
        elif user_choice == "report":
            barista.report()
            cashier.report()
        else:
            beverage = menu.find_drink(user_choice)
            if barista.is_resource_sufficient(beverage):
                if cashier.make_payment(beverage.cost):
                    barista.make_coffee(beverage)
            another = input("Would you like to continue? Type 'y' for yes, or 'n' for no.").lower()
            if another == 'y':
                clear()
                print(logo)
            else:
                continue_loop = False


main()
