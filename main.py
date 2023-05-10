from player import Player
from weapon import Weapon
from consumable import Consumable
from insect import Insect

# Create a new player
player_name = input("Enter your name: ")
player = Player(player_name)

# Create some weapons
sword = Weapon("Sword", 10, 10)
axe = Weapon("Axe", 8, 12)
dagger = Weapon("Dagger", 6, 8)

# Let the player choose a weapon
print("Choose a weapon:")
print("1. Sword")
print("2. Axe")
print("3. Dagger")
weapon_choice = input("Enter the number of the weapon you want to choose: ")
if weapon_choice == "1":
    player.get_weapon(sword)
elif weapon_choice == "2":
    player.get_weapon(axe)
elif weapon_choice == "3":
    player.get_weapon(dagger)
else:
    print("Invalid choice. No weapon equipped.")

# Create some consumables
apple = Consumable("Apple", 10)
potion = Consumable("Potion", 25)

# Let the player use a consumable
print("Use a consumable:")
print("1. Apple (+10 health)")
print("2. Potion (+25 health)")
consumable_choice = input("Enter the number of the consumable you want to use, or enter 0 to skip: ")
if consumable_choice == "1":
    player.use_consumable(apple)
elif consumable_choice == "2":
    player.use_consumable(potion)
else:
    print("No consumable used.")

# Start the battle with an insect
insect = Insect("Insect")
print(f"A wild {insect.name} appears!")

# Loop until the player or insect is defeated or the player runs away
while player.health > 0 and insect.health > 0:
    # Prompt the player to attack or use a consumable
    print("Choose an action:")
    print("1. Attack")
    print("2. Use a consumable")
    action_choice = input("Enter the number of the action you want to take: ")
    if action_choice == "1":
        player.attack(insect)
    elif action_choice == "2":
        print("Use a consumable:")
        print("1. Apple (+10 health)")
        print("2. Potion (+25 health)")
        consumable_choice = input("Enter the number of the consumable you want to use: ")
        if consumable_choice == "1":
            player.use_consumable(apple)
        elif consumable_choice == "2":
            player.use_consumable(potion)
        else:
            print("Invalid choice. Turn skipped.")
    else:
        print("Invalid choice. Turn skipped.")
        
    # Check if the insect is defeated
    if insect.health <= 0:
        print(f"{insect.name} has been defeated!")
        break
        
    # Insect attacks
    insect.attack(player)
    
    # Check if the player is defeated
    if player.health <= 0:
        print(f"{player.name} has been defeated!")
        break
