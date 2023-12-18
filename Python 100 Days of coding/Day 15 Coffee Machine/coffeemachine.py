# Coffee machine 

# Makes 3 Hot Flavors:
    # 1: espresso. $1.50, 50 ml water, 18g coffee
    # 2: latte. $2.50, 200ml water, 24g coffee, 150ml milk
    # 3 Cappuccino. $3.00, 250ml water, 24g coffee, 100ml milk
# Is also coin operated. 
    # Penny (1 cent), Nickel (5 cents), Dime (10 cents), Quarter (25 cents)
# Program Reqs:
    # TODO 1. Print report. What resources it has left
    # TODO 2. Check if resources sufficient to make drink
    # TODO 3. Process coins
    # TODO 4. Check transaction successful, that the money is enough
    # TODO 5. Make coffee

# Written in the form provided by the instructional videos. This is probably *not* the best way to write this code.
# Procedural Programming

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# To Do 2: Are resources sufficient?
def is_res_sufficient(order_ingredients):
    """Returns true if order can be made, false if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry... There is not enough {item}.")
            return False
    return True

# To Do 3: Process coins
def process_coins():
    """Returns the total calculated from the coins inserted by user"""
    print("Insert coins please.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# To do 4: is transaction successful?
def transaction_successful(money_rec, drink_cost):
    """Return true if payment is enough, false if payment is not enough"""
    if money_rec >= drink_cost:
        change = round(money_rec - drink_cost,2)
        print(f"Here is ${change} in change!")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry... that's not enough money. Money will be refunded.")
        return False

# To do 5: Make the coffee!!
def make_coffee(drink_name, order_ingredients):
    """Deduct req ingredients from resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}! Enjoy!")

is_on = True

# Code to loop the program
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice in ["espresso", "latte", "cappuccino"]:
        drink = MENU[choice]
        if is_res_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    elif choice == "report":
        # To Do 1, make report
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "off":
        print("Shutting the machine off. Have a nice day!")
        is_on = False
    else:
        print("Sorry, you did not enter a valid input. You can order an espresso, latte, or cappuccino, request a report, or shut the machine off. Try again.")