import random

number = random.randint(1, 100)
difficuilty = input("Choose a difficuilty. Type 'easy' or 'hard': ")
if(difficuilty == 'easy'):
    attempts = 10
elif(difficuilty == 'hard'):
    attempts = 5

while(attempts > 0):
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input('Make a guess: '))
    if(guess == number):
        print("You Won!")
        break
    elif(guess < number):
        print("Too Low!")
    elif(guess > number):
        print("Too High!")
    attempts -= 1
if(attempts == 0 and guess != number):
    print("Out of Attempts, You Lose!")