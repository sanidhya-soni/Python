import random as rd
choice = ["Stone", "Paper", "Scissor"]
user_choice = int(input("Enter 1 for Stone, 2 for Paper, 3 for Scissor : "))
pc_choice = rd.randint(1, 3)
try:
    print(f"You Choose : {choice[user_choice - 1]}")
    print(f"Pc Choose : {choice[pc_choice - 1]}")
except IndexError:
    print("Enter Right Choice")
    exit()
if user_choice == 1:
    if pc_choice == 2:
        print("You Loose")
    elif pc_choice == 3:
        print("You Win..... Wooohhhoooo")
    else:
        print("Its a Tie..... Damn")
elif user_choice == 2:
    if pc_choice == 3:
        print("You Loose")
    elif pc_choice == 1:
        print("You Win..... Wooohhhoooo")
    else:
        print("Its a Tie..... Damn")
else:
    if pc_choice == 1:
        print("You Loose")
    elif pc_choice == 2:
        print("You Win..... Wooohhhoooo")
    else:
        print("Its a Tie..... Damn")
