from replit import clear
import Data


def make_espresso():
    resources["water"] -= Data.MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] -= Data.MENU["espresso"]["ingredients"]["coffee"]
    print("Your Espresso is Ready, Enjoy !")


def make_latte():
    resources["water"] -= Data.MENU["latte"]["ingredients"]["water"]
    resources["milk"] -= Data.MENU["latte"]["ingredients"]["milk"]
    resources["coffee"] -= Data.MENU["latte"]["ingredients"]["coffee"]
    print("Your Latte is Ready, Enjoy !")


def make_cappuccino():
    resources["water"] -= Data.MENU["cappuccino"]["ingredients"]["water"]
    resources["milk"] -= Data.MENU["cappuccino"]["ingredients"]["milk"]
    resources["coffee"] -= Data.MENU["cappuccino"]["ingredients"]["coffee"]
    print("Your Cappuccino is Ready, Enjoy !")


def check_resources():
    if choice == 1:
        return Data.MENU["espresso"]["ingredients"]["water"] <= resources["water"] and Data.MENU["espresso"]["ingredients"][
            "coffee"] <= resources["coffee"]
    if choice == 2:
        return Data.MENU["latte"]["ingredients"]["water"] <= resources["water"] and Data.MENU["latte"]["ingredients"][
            "milk"] <= resources["milk"] and Data.MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"]
    if choice == 3:
        return Data.MENU["cappuccino"]["ingredients"]["water"] <= resources["water"] and Data.MENU["cappuccino"]["ingredients"][
            "milk"] <= resources["milk"] and Data.MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"]


def process_coins(price):
    print(f"Start Putting the Coins to Enter an amount of Rs.{price}")
    one = int(input("Enter Coins of RS.1 : "))
    two = int(input("Enter Coins of RS.2 : "))
    five = int(input("Enter Coins of RS.5 : "))
    ten = int(input("Enter Coins of RS.10 : "))
    total = one + (two * 2) + (five * 5) + (ten * 10)
    if total - price >= 0:
        print(f"Amount Entered = {total}")
        print(f"Change = {total - price}")
        return True
    else:
        print(f"Less Amount Entered. Amount Returned = total")
        return False


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


choice = 0

while choice != 9:
    print(f"Resources Left = {resources}")
    choice = int(input("1. for Espresso\n2. for Latte\n3. for Cappuccino\n9. To Turn off the Machine\nEnter Your "
                       "Choice: "))
    if choice == 1:
        if check_resources():
            print("You Selected an Espresso")
            if process_coins(Data.MENU["espresso"]["cost"]):
                print("Payment was Successful!")
                make_espresso()
            else:
                print("Payment was Unsuccessful, Please Try Again !")
        else:
            print("Sorry!, Not Enough Ingredients")
            continue
    elif choice == 2:
        if check_resources():
            print("You Selected a Latte")
            if process_coins(Data.MENU["latte"]["cost"]):
                print("Payment was Successful!")
                make_latte()
            else:
                print("Payment was Unsuccessful, Please Try Again !")
        else:
            print("Sorry!, Not Enough Ingredients")
            continue
    elif choice == 3:
        if check_resources():
            print("You Selected a Cappuccino ")
            if process_coins(Data.MENU["cappuccino"]["cost"]):
                print("Payment was Successful!")
                make_cappuccino()
            else:
                print("Payment was Unsuccessful, Please Try Again !")
        else:
            print("Sorry!, Not Enough Ingredients")
            continue

print("Machine Turned Off!")
