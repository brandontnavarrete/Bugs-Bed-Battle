import random
import time

# from folder 'gears' run player and class "Player"
from gears.player import Player
from gears.insect import Insect

# Create an instance of the Player class
player = Player("John")

# Create an instance of the Insect class
insect = Insect("Bug")

# Attack the player
insect.attack(player)

while player.health > 0:
  # Get the player's choice
  answer = input("Enter 0 to attack or 1 to defend: ")
  answer = int(answer)  # Convert the input to an integer

  # Perform the chosen action
  if answer == 0:
      player.attack(insect)
  elif answer == 1:
     player.defend()
  else:
      print("Invalid choice. Please enter 0 or 1.")

  # Attack the player again
  insect.attack(player)

print('dead')

