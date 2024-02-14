from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep


coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

ordering = True

while ordering:
    order = input("What would you like to do (menu, order, report, turn off): ")
    if order == "order":
        coffee = input("What would you like? ")
        machine_order = menu.find_drink(coffee)
        if coffee_machine.is_resource_sufficient(machine_order) is True:
            if money_machine.make_payment(machine_order.cost) is True:
                coffee_machine.make_coffee(machine_order)
            else:
                print("Order something else.")
        else:
            print("You'll have to order something else")

    elif order == "menu":
        print(menu.get_items())

    elif order == "report":
        coffee_machine.report()
        money_machine.report()

    else:
        quit()