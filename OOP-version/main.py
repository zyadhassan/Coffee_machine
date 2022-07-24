from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu=Menu()
Coffee_Maker=CoffeeMaker()
Money_Machine=MoneyMachine()


Machine_on=True

while Machine_on:
    order=str(input("What do you like? (espresso/latte/cappuccino) :")).lower()
    if order=='off':
        Machine_on=False
    elif order=='report':
        Coffee_Maker.report()
        Money_Machine.report()
    else:
        item=Menu.find_drink(order)
        if Coffee_Maker.is_resource_sufficient(item):
            if Money_Machine.make_payment(item.cost):
                Coffee_Maker.make_coffee(item)




