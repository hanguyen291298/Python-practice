MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 25,
            "coffee": 20
        },
        "cost": 2.5
    },
    "latte": {
        "ingredients": {
            "water": 75,
            "milk": 20,
            "coffee": 25
        },
        "cost": 3.0
    },
    "cappuccino": {
        "ingredients": {
            "water": 50,
            "milk": 20,
            "coffee": 15
        },
        "cost": 2.0
    }
}
profit = 0
Resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def play_game():
    global profit
    is_on = True
    while is_on:
        your_drink = input("What would you like to drink? (espresso/latte/cappuccino): ")
        if your_drink == 'off':
            is_on = False
        elif your_drink == 'report':
            print(f"Water: {Resources['water']}\nMilk: {Resources['milk']}\nCoffee: {Resources['coffee']}\nProfit: {profit}")
        else:
            for each_ingredient in MENU[your_drink]['ingredients']:
                if Resources[each_ingredient] > MENU[your_drink]['ingredients'][each_ingredient]:
                    print("Please insert coin")
                    quarter = float(input("How many quarter? ")) * 0.25
                    dimes = float(input("How many dimes? ")) * 0.1
                    nickle = float(input("How many nickles? ")) * 0.05
                    pennies = float(input("How many pennies? ")) * 0.01
                    total = quarter + dimes + nickle + pennies
                    if total >= MENU[your_drink]["cost"]:
                        change = total - MENU[your_drink]["cost"]
                        for ingredient in MENU[your_drink]['ingredients']:
                            Resources[ingredient] -= MENU[your_drink]['ingredients'][ingredient]
                        profit += MENU[your_drink]['cost']
                        print(f"Here is your change: {change}$")
                        print("Enjoy your coffee!")
                    else:
                        is_on = False
                        print(f"Sorry. There is not enough {each_ingredient}")
                    play_game()

play_game()