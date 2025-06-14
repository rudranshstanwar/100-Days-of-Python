from art import logo
from art import vs
from game_data import data
import random

# To print the game logo and collect the score
print(logo)
score = 0

#To take random data from the list data
number_1 = random.randint(0, 49)
name_1 = data[number_1]['name']
a = data[number_1]['follower_count']
description_1 = data[number_1]['description']
country_1 = data[number_1]['country']
print(f"Compare A: {name_1}, a {description_1}, from {country_1}")

# For game to continue if the answer is right
continue_game = True
while continue_game: # Using while loop for game to continue.
    print(vs)

    number_2 = random.randint(0, 49)
    name_2 = data[number_2]['name']
    b = data[number_2]['follower_count']
    description_2 = data[number_2]['description']
    country_2 = data[number_2]['country']
    print(f"Against B: {name_2}, a {description_2}, from {country_2}")

    # For game to not stop if both are same
    if name_1 == name_2:
        number_2 = random.randint(0, 49)
        name_2 = data[number_2]['name']
        b = data[number_2]['follower_count']
        description_2 = data[number_2]['description']
        country_2 = data[number_2]['country']

    # To compare between A and B
    compare = input("Who has more followers? Type 'A' or 'b': ").lower()

    if a > b:
        if compare == "a":
            score += 1
            print("\n"*20)
            print(logo) # The name is required as it makes game more interactive.
            print(f"You're right! current score: {score}")
            print(f"Compare A: {name_2}, a {description_2}, from {country_2}")

        elif compare == "b":
            print("\n" * 20)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False # As the answer is wrong the game should end.
    elif b > a:
        if compare == "b":
            score += 1
            print("\n"*20)
            print(logo)
            print(f"You're right! current score: {score}")
            print(f"Compare A: {name_2}, a {description_2}, from {country_2}")

        elif compare == "a":
            print("\n" * 20)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False
    if compare == "":
        continue_game = False