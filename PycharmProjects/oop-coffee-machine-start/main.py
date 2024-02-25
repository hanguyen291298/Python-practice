from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_continue = True
menu = Menu()
resources = CoffeeMaker()
coin_insert = MoneyMachine()

while is_continue:
    all_products = menu.get_items()
    drink = input("What would you like? " + all_products)
    if drink == "off":
        is_continue = False
    elif drink == "report":
        resources.report()
        coin_insert.report()
    else:
        your_order = menu.find_drink(drink)
        if resources.is_resource_sufficient(your_order) and coin_insert.make_payment(your_order.cost):
            resources.make_coffee(your_order)

















