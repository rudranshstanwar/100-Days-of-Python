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
    "money" : 0,
}

penny = 0.01
dime = 0.10
nickel = 0.05
quarter = 0.25
change = 0 # To make sure it can be used in different cases inside and outside a function
money_in_machine = 0 # The money which is paid for coffee by the customer and left after giving the change
# Check if resources are enough
# If the coins the insufficient give a refund and tell them that you need to cough up some more money
# If coins are sufficient the transaction will be successful and machine will make the coffee
# Deduct the resources used


# A function to do all money related work
def money(instruction):
    global change

    print("Please insert coins.")
    c_q = int(input("how many quarters?: "))
    c_d = int(input("how many dimes?: "))
    c_n = int(input("how many nickles?: "))
    c_p = int(input("how many pennies?: "))

    # To know how much money has customer given
    money_received = round((quarter * c_q + dime * c_d + nickel * c_n + penny * c_p), 2)
    change = MENU[instruction]["cost"] - money_received
    # Applying condition for transaction success or not
    if change > 0:
        # If the money is not sufficient refund it.
        print("Sorry that's not enough money. Money refunded.")
    elif change == 0:
        print(f"Here is your {instruction}. Enjoy.")
    else:
        change = 0 - change # Correcting the error
        print(f"Here is ${change} in change")
        print(f"Here is your {instruction}. Enjoy.")

# A function for resources
def is_resource_sufficient(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            return False
    return True

work = True
while work:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        work = False

    elif order == "report":
        print( f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}gm")
        print(f"Money: ${resources["money"]}")

    elif order == "espresso" or order == "latte" or order == "cappuccino":
        for item in MENU[order]["ingredients"]:
            if MENU[order]["ingredients"][item] > resources[item]:
                print("Insufficient resources.")
                print("Please try again after adding new materials")
                work = False

        if work:
            money(order)
            if change >= 0:
                resources["water"] -= MENU[order]["ingredients"]["water"]
                resources["milk"] -= MENU[order]["ingredients"]["milk"]
                resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
                resources["money"] += MENU[order]["ingredients"]["coffee"]



