drink = 0
cost = 0
money_in = 0
profit = 0
change = 0
water = 300
milk = 200
coffee = 100
running = True
drinks = [
    {"drink": "espresso", "water": 50, "milk": 0, "coffee": 18, "cost": 1.50},
    {"drink": "latte", "water": 200, "milk": 150, "coffee": 24, "cost": 2.50},
    {"drink": "cappuccino", "water": 250, "milk": 100, "coffee": 24, "cost": 3.0}]
while running:
    input_drink = input("What number would you like order?\n1 : espresso | 2 : latte | 3 : cappuccino: ")
    if input_drink == "off":
        print("Machine is now off")
        running = False
    elif input_drink == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Profit: £{profit}")
        continue
    elif drinks[int(input_drink) - 1]["water"] > water:
        print("Sorry no enough water left")
    elif drinks[int(input_drink) - 1]["milk"] > milk:
        print("Sorry no enough milk left")
    elif drinks[int(input_drink) - 1]["coffee"] > coffee:
        print("Sorry no enough coffee left")
    else:
        print("Please insert coins.")
        pounds = int(input("How many pounds? £"))
        pennies = int(input("How many pennies? £0."))
        money_in = pounds + (pennies * 0.01)
        print(f"xxxxxxxxxxxxxxxxxxxxxxx {type(money_in)} ,,, {type(drinks[int(input_drink) - 1]['cost'])}")
        if money_in < drinks[int(input_drink) - 1]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = money_in - drinks[int(input_drink) - 1]["cost"]
            water -= drinks[int(input_drink) - 1]["water"]
            milk -= drinks[int(input_drink) - 1]["milk"]
            coffee -= drinks[int(input_drink) - 1]["coffee"]
            profit += drinks[int(input_drink) - 1]["cost"]
            print(f"Here is £{change} in change.")
            print(f"Here is your {drinks[int(input_drink) - 1]['drink']} ☕️. Enjoy!")
