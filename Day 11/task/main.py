cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random

def blackjack():
    yes_or_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if yes_or_no == "y":
        print("\n"*20)
        print(r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
        your_cards = [random.choice(cards), random.choice(cards)]
        your_sum = int()
        for card in your_cards:
            your_sum += card

        print(f"Your cards: {your_cards}, current_score = {your_sum}")
        computer_cards = [random.choice(cards)]
        computer_sum = int()
        sums = int()

        for card in computer_cards:
            sums += card
        computer_cards.append(random.choice(cards))
        for card in computer_cards:
            computer_sum += card
        print(f"Computer's first card: {sums}")

        true_or_not = True
        while your_sum < 21 and true_or_not:
            yes_or_no = input("Type 'y' for another card, type 'n' to pass: ").lower()
            if yes_or_no == "y":
                your_cards.append(random.choice(cards))
                your_sum = 0
                computer_sum = 0
                for card in your_cards:
                    your_sum += card
                print(f"Your cards: {your_cards}, current_score = {your_sum}")
                computer_cards.append(random.choice(cards))
                for card in computer_cards:
                    computer_sum += card
                print(f"Computer's first card: {sums}")
            elif yes_or_no == "n":
                print(f"Your final hand: {your_cards}, final score: {your_sum}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")
                if your_sum > computer_sum:
                    print("You win")
                else:
                    print("You lose")
                true_or_not = False
                if computer_sum > 21:
                    print(f"Your final hand: {your_cards}, final score: {your_sum}")
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")
                    print("Opponent went over you win.")

        if your_sum >= 21:
            print(f"Your final hand: {your_cards}, final score: {your_sum}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")
            if  your_sum > 21 and computer_sum > 21:
                print("Both went over. A draw")
            elif your_sum > 21:
                print("You went over. You lose")
            elif computer_sum > 21:
                print("Opponent went over. You win")
            else:
                if your_sum > computer_sum:
                    print("You win")
                else:
                    print("You lose")
    blackjack()
blackjack()