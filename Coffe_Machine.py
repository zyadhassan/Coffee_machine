#☕☕☕☕
from Menu import MENU
Machine_on=True
resources={
    'Water':300,'Milk':200,'Coffee':100,'Money':0
}


def report():
    print(f"Water : {resources['Water']}ml")
    print(f"Milk : {resources['Milk']}ml")
    print(f"Coffee : {resources['Coffee']}g")
    print(f"Money : ${resources['Money']}")


def order(item,coin):
    ordered=False
    change=0
    if item =="latte":
        if resources['Water']>=200 :

            if resources['Milk']>=150:

                if resources['Coffee']>=24:
                    if coin>=2.5:

                        resources['Water']-=200
                        resources['Milk']-=150
                        resources['Coffee']-=24
                        resources['Money']+=2.5
                        change=coin-2.5
                        ordered=True
                    else:
                        print("Sorry, You did not pay enough money ")
                else:
                    print("Sorry, Not enough Coffee")
            else:
                print("Sorry, Not enough Milk")
        else:
            print('Sorry, Not enough Water')
    elif item=='cappuccino':
        if resources['Water'] >= 250:

            if resources['Milk'] >= 100:

                if resources['Coffee'] >= 24:

                    if coin >= 3:
                        resources['Water'] -= 250
                        resources['Milk'] -= 100
                        resources['Coffee'] -= 24
                        resources['Money'] += 3
                        change=coin-3
                        ordered = True
                    else:
                        print("Sorry, You did not pay enough money ")
                else:
                    print("Sorry, Not enough Coffee")
            else:
                print("Sorry, Not enough Milk")
        else:
            print('Sorry, Not enough Water')
    else:
        if resources['Water'] >= 50:

            if resources['Coffee'] >= 18:
                if coin >= 1.5:
                    resources['Water'] -= 50
                    resources['Coffee'] -= 18
                    resources['Money'] += 1.5
                    change=coin-1.5
                    ordered = True
                else:
                    print("Sorry, You did not pay enough money ")
            else:
                print("Sorry, Not enough Coffee")
        else:
            print('Sorry, Not enough Water')
    return ordered,change


def count_coin():
    quarters=float(input("How many quarters? :"))
    dimes=float(input("How many dimes? :"))
    nickels=float(input("How many nickel? :"))
    pennies=float(input("How many pennies? :"))
    coin=(dimes*0.1)+(quarters*0.25)+(nickels*0.05)+(pennies*0.01)
    return coin


while Machine_on:
    orders=str(input("What do you like? (espresso/latte/cappuccino) :")).lower()
    if orders=='off':
        Machine_on=False
    elif orders=='report':
        report()
    else:
        coin=count_coin()
        ordered,change=order(orders,coin)
        if ordered:
            print(f'Here is ${round(change,2)} in change ')
            print(f"Here is your {orders} ☕☕☕")
