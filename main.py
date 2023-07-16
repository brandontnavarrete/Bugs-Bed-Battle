import random
import time

# from folder 'gears' run player and class "Player"
from gears.player import Player
from gears.insect import Insect

# Create an instance of the Player class
player = Player("John")
player.self_describe()
# Create an instance of the 0Insect class
insect = Insect()

# Attack the player
insect.attack(player)

while player.is_alive():
  # Check if the insect is defeated
  if insect.health <= 0:
    print(f"{insect.name} has been defeated!")
    insect = Insect()  # Spawn a new insect

  # Get the player's choice
  valid_choice = False
  while not valid_choice:
    answer = input("Enter 0 to attack or 1 to defend: ")
    if answer == '0' or answer == '1':
      valid_choice = True
    else:
      print("Invalid choice. Please enter 0 or 1.")

  answer = int(answer)  # Convert the input to an integer

  # Perform the chosen action
  if answer == 0:
    player.attack(insect)
  elif answer == 1:
    player.defend()

  # Attack the player
  insect.attack(player)

player.self_describe()
print('Player is defeated. Game over!')
