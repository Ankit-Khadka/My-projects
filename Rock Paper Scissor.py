#Rock paper scissors game
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissor]
user_input = int(input("You are in the game of Rock Paper Scissors."
                       "Choose 0 for rock, 1 for paper and 2 for scissor. "))
print(game_images[user_input])
print(f"You chose!")
bot_choice = random.randint(0, 2)
print(game_images[bot_choice])
print(f"Computer chose!")

if user_input >= 3 or user_input < 0:
    print("You have chosen invalid option play again")
elif user_input == bot_choice:
    print("It was a draw")
elif user_input == 0 and bot_choice == 2:
    print("You win!")
elif bot_choice == 0 and user_input == 2:
    print("You lost!")
elif user_input > bot_choice:
    print("You win!")
elif user_input < bot_choice:
    print("You lost!")
    



