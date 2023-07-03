from player import Player
from weapon import Weapon
from insect import Insect

# create a player with high health
player_name = input("Enter your name: ")
player = Player(player_name, 100)

# create a list of available weapons
available_weapons = [
    Weapon("Sword", 15, 10),
    Weapon("Axe", 20, 8),
    Weapon("Mace", 10, 12),
    Weapon("Bow", 12, 15)
]

# prompt the player to choose a weapon
print("Available weapons:")
for i, weapon in enumerate(available_weapons):
    print(f"{i+1}. {weapon.name} ({weapon.damage} strength, {weapon.durability} durability)")
weapon_choice = int(input("Choose a weapon (1-4): "))
player.get_weapon(available_weapons[weapon_choice-1])
print(f"You have chosen {player.weapon.name} as your weapon.")

# simulate an endless wave of insect attacks
insect_wave = 1
insect_count = 5
score = 0
while True:
    print(f"\nInsect wave {insect_wave} - {insect_count} insects remaining.")
    # create a list of insects for this wave
    insects = [Insect(f"Insect {i+1}") for i in range(insect_count)]
    # attack each insect until it'ys defeated or the player dies
    for insect in insects:
        print(f"\n{insect.name} appears!")
        while insect.health > 0 and player.health > 0:
            print(f"\nYour health: {player.health}  {insect.name} health: {insect.health}")
            attack_choice = input("Do you want to attack? (y/n): ")
            if attack_choice.lower() == 'y':
                damage = player.weapon.damage
                insect.take_damage(damage)
                print(f"You hit {insect.name} for {damage} damage!")
                if insect.health <= 0:
                    insect_count -= 1
                    score += 1
                    print(f"You defeated {insect.name}!")
                    break
                damage = insect.attack(player)
                player.take_damage(damage)
                print(f"{insect.name} hit you for {damage} damage!")
            else:
                print("You chose not to attack.")
        if player.health <= 0:
            break
    # increase the strength of the insects for the next wave
    insect_wave += 1
    insect_count += 2
    for insect in insects:
        insect.health += 10
    # check if the player is defeated
    if player.health <= 0:
        print("\nYou have been defeated!")
        break
    # check if the player has defeated 5 waves and end the game
    if score >= 5:
        print("\nYou have defeated 5 waves of insects and survived!")
        break

# display the final score
print(f"\nYour final score is {score}.")
n