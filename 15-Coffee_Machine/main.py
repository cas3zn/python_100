import sys

# Monetary value in coins

QUARTERS = 0.25
DIMES = 0.10
NICKELS = 0.05
PENNIES = 0.01

# Menu and resources dictionaries
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(coffee_type):
    if coffee_type == 'espresso':
        if resources['water'] >= MENU['espresso']['ingredients']['water'] and \
                resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
            return True
        else:
            return False
    elif coffee_type == 'latte':
        if resources['water'] >= MENU['latte']['ingredients']['water'] and \
                resources['milk'] >= MENU['latte']['ingredients']['milk'] \
                and resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
            return True
        else:
            return False
    elif coffee_type == 'cappuccino':
        if resources['water'] >= MENU['cappuccino']['ingredients']['water'] and \
                resources['milk'] >= MENU['cappuccino']['ingredients']['milk'] \
                and resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
            return True
        else:
            return False


def coins(q, d, n, p):
    total_coins = (q * QUARTERS) + (d * DIMES) + (n * NICKELS) + (p * PENNIES)
    return total_coins


def main():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    print('Please insert coins.')
    user_quarters = int(input("How many quarters? : "))
    user_dimes = int(input("How many dimes? : "))
    user_nickels = int(input("How many nickels? : "))
    user_pennies = int(input("How many pennies? : "))
    value = coins(user_quarters, user_dimes, user_nickels, user_pennies)

    if user_input == 'espresso':
        available = check_resources(user_input)
        if available:
            if value >= MENU[user_input]['cost']:
                resources['water'] -= MENU[user_input]['ingredients']['water']
                resources['coffee'] -= MENU[user_input]['ingredients']['coffee']
                rem = round(float(value - MENU[user_input]['cost']), 2)
                print(f'Here is ${rem} in change.')
                print(f'Here is your {user_input}. Enjoy!')
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif user_input == 'latte':
        available = check_resources(user_input)
        if available:
            if value >= MENU[user_input]['cost']:
                resources['water'] -= MENU[user_input]['ingredients']['water']
                resources['milk'] -= MENU[user_input]['ingredients']['milk']
                resources['coffee'] -= MENU[user_input]['ingredients']['coffee']
                rem = round(float(value - MENU[user_input]['cost']), 2)
                print(f'Here is ${rem} in change.')
                print(f'Here is your {user_input}. Enjoy!')
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif user_input == 'cappuccino':
        available = check_resources(user_input)
        if available:
            if value >= MENU[user_input]['cost']:
                resources['water'] -= MENU[user_input]['ingredients']['water']
                resources['milk'] -= MENU[user_input]['ingredients']['milk']
                resources['coffee'] -= MENU[user_input]['ingredients']['coffee']
                rem = round(float(value - MENU[user_input]['cost']), 2)
                print(f'Here is ${rem} in change.')
                print(f'Here is your {user_input}. Enjoy!')
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif user_input == 'report':
        print(f'Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}')
    elif user_input == 'off':
      sys.exit(0)
    else:
        print('Please choose between the three options or keywords "report" and/or "off"')
    main()

main()