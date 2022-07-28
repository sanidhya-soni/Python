import random
from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(users_score, computer_score):
    if users_score == computer_score:
        print("Draw!")
    elif computer_score == 0:
        print("Lose, Opponent has blackjack!")
    elif users_score == 0:
        print("Win with a blackjack!")
    elif users_score > 21:
        print("You went over, You Lose!")
    elif computer_score > 21:
        print("Opponent went over, You Win!")
    elif users_score > computer_score:
        print("You Win!")
    else:
        print("You Lose!")


def play_game():
    is_game_over = False
    user_cards = []
    computer_cards = []
    computer_score = user_score = 0

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer's First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, Final Score: {user_score}")
    print(f"Computers final hand: {computer_cards}, Final Score: {computer_score}")
    compare(user_score, computer_score)


while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
