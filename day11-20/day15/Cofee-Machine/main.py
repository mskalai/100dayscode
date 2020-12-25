from report import MENU, resources
from logo import logo
def amount(item,cost,price):
    print("Please insert coins")
    qt=int(input("How many quarters? :"))
    dm=int(input('How many dimes? :'))
    nk=int(input('How many nickles? :'))
    pn=int(input("How many pennies? :"))
    amt=qt*0.25+dm*0.10+nk*0.05+pn*0.01
    if(amt<MENU[item][cost]):
        print("Sorry that's not enough money! Money refunded")
    elif(amt>MENU[item][cost]) :
        ret=amt-MENU[item][cost]
        resources['money']+=price
        print(f"Here is your ${round(ret,2)} change!")
        print(f"Here is your {item} ☕,Enjoy 😊")
    elif(amt==MENU[item][cost]):
        resources['money'] += price
        print(f"Here is your {item}☕, Enjoy 😊")

def espresso():
    if(MENU['espresso']['ingredients']['water']<=resources['water']) and (MENU['espresso']['ingredients']['coffee']<=resources['coffee']):
        amount('espresso', 'cost', 1.5)
        resources['water']-=MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
    elif(MENU['espresso']['ingredients']['water']>resources['water']):
        print("Sorry water is not enough")
    elif (MENU['espresso']['ingredients']['coffee'] > resources['coffee']):
        print("Sorry coffee is not enough")
    else:
        print("Sorry water and cofee not available")
def latte():
    if (MENU['latte']['ingredients']['water']<=resources['water']) and MENU['latte']['ingredients']['milk']<=resources['milk'] and MENU['latte']['ingredients']['coffee']<=resources['coffee']:
        amount('latte','cost',2.5)
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
    elif (MENU['latte']['ingredients']['water'] > resources['water']):
        print("Sorry water is not enough")
    elif (MENU['latte']['ingredients']['coffee'] > resources['coffee']):
        print("Sorry coffee is not enough")
    elif (MENU['latte']['ingredients']['milk'] > resources['milk']):
        print("Sorry milk is not enough")
    else:
        print("Sorry water, coffee and milk are not available")
def capuccino():
    if (MENU['cappuccino']['ingredients']['water'] <= resources['water']) and MENU['cappuccino']['ingredients']['milk'] <=resources['milk'] and MENU['cappuccino']['ingredients']['coffee'] <= resources['coffee']:
        amount('cappuccino', 'cost', 3.0)
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
    elif (MENU['cappuccino']['ingredients']['water'] > resources['water']):
        print("Sorry water is not enough")
    elif (MENU['cappuccino']['ingredients']['coffee'] > resources['coffee']):
        print("Sorry coffee is not enough")
    elif (MENU['cappuccino']['ingredients']['milk'] > resources['milk']):
        print("Sorry milk is not enough")
    else:
        print("Sorry water, coffee and milk are not available")

con=True
print(logo)
while(con):
    inp=input("What would you like? (espresso/latte/cappuccino) :").lower()
    if inp=="report":
        print(f" Water   : {resources['water']}ml\n Milk    : {resources['milk']}ml\n Coffee  : {resources['coffee']}g\n Money   : ${resources['money']}")
    elif inp=="espresso":
        espresso()
    elif inp=='latte':
        latte()
    elif inp=='cappuccino':
        capuccino()
    elif inp=='off':
        con=False
