import random
import time

# from folder 'gears' run player and class "Player"
from gears.player import Player
from gears.insect import Insect
from gears.weapon import Weapon


def main():
    # Create an instance of the Player class
    player = Player("John")
    player.self_describe()

    # Create an instance of the Insect class
    insect = Insect()
    insect.self_describe()

    # Create weapons
    sword = Weapon("Sword", durability=50, damage=15)
    axe = Weapon("Axe", durability=40, damage=20)
    bow = Weapon("Bow", durability=30, damage=25)

    # Player selects a weapon and adds it to the inventory
    chosen_weapon = None
    while chosen_weapon is None:
        print("Choose a weapon to add to your inventory:")
        print("1. Sword")
        print("2. Axe")
        print("3. Bow")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            chosen_weapon = sword
        elif choice == "2":
            chosen_weapon = axe
        elif choice == "3":
            chosen_weapon = bow
        else:
            print("Invalid choice. Try again.")

    player.add_to_inventory(chosen_weapon)

    print(f"{player.name} has selected {chosen_weapon.name} as their weapon.")

    # Simulate a simple combat scenario
    while player.health > 0 and insect.health > 0:
        # Player attacks insect
        player.attack(insect)

        # If the insect is still alive, it attacks the player
        if insect.health > 0:
            insect.attack(player)

    # Check who won the combat
    if player.health <= 0:
        print("Game Over. The insect has defeated you!")
    else:
        print("Congratulations! You have defeated the insect!")

if __name__ == "__main__":
    main()
