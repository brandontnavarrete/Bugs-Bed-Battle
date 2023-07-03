import random


class Insect:

  def __init__(self, name=None):
    if name is None:
      self.name = random.choice(['Ant', 'Spider', 'Slug'])
    else:
      self.name = name
    self.health = random.randint(1, 100)

  def attack(self, player):
    """
      Attacks the player, reducing their health by a random amount between 1 and 5.

      Args:
        player (Player): The player to attack.
      """
    damage = random.randint(1, 5)
    actual_damage = player.take_damage(damage)
    print(f"{self.name} attacks {player.name} for {actual_damage} damage!")
    print(f"{player.name}'s health: {player.health}")

    return damage

  def take_damage(self, damage, player):
    """
        Takes the specified amount of damage, reducing the insect's health.

        Args:
            damage (int): The amount of damage to take.
        """
    self.health -= damage
    if self.health <= 0:
      print(f"{self.name} has been defeated!")
      print(f"{player.name} has scored!")
      player.score += 1

  def run_away(self):
    """
        Randomly determines whether the insect will run away from the player.
        """
    if random.random() < 0.5:
      print(f"{self.name} runs away!")
      return True
    return False

  def self_describe(self):
    """
        Prints information about the player, including their name, health, and weapon (if they have one).
        """
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
