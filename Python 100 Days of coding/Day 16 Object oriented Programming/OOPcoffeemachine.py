# Coffee Machine but in OOP
# Importing all the provided files
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_mch = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice in options:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_mch.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    elif choice == "off":
        is_on = False
    elif choice == "report": 
        coffee_maker.report()
        money_mch.report()
    else: 
        print(f"Sorry, you did not enter a valid input. You can order {options}, request a report, or shut the machine off. Try again.")