rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
the_best_game = [rock, paper, scissors]
Input = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors \n"))
Computer = random.randint(0, 2)
print(the_best_game[int(Input)])
print(the_best_game[Computer])
if Input == 0 and Computer == 2:
    print("You Win")
elif Input == 2 and Computer == 0:
    print("You Lose")
elif Input > Computer and Input != 2 and Computer != 0:
    print("You Win")
elif Input < Computer and input != 0 and Computer != 2:
    print("You Lose")
elif Input == 0 and Computer == 2:
    print("You Win")
elif Input > Computer:
    print("You Win")
else:
    print("It's a Draw")

