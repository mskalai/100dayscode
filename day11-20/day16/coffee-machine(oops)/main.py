from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
mn=Menu()
cm=CoffeeMaker()
mon=MoneyMachine()
con=True
while(con):
    options=mn.get_items()
    inp=input(f"Which drink do you want {options} :")
    if inp=='report':
        cm.report()
        mon.report()
    elif inp=='off':
        con=False
    else:
        drink = mn.find_drink(inp)

        is_enough_ingredients = cm.is_resource_sufficient(drink)

        is_payment_successful = mon.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            cm.make_coffee(drink)






