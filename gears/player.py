class Player:
  """
    A class representing a player in the game.
    """

  def __init__(self, name, health=100):
    """
        Initializes the player object with a name, health, and no weapon.
        Args:
            name (str): The name of the player.
        """
    self.name = name
    self.health = health
    self.weapon = None
    self.defense = 1.0  # Initial defense attribute
    self.score = 0
    self.inventory = []

# INVENTORY

  def add_to_inventory(self, item):
    """
        Add an item to the player's inventory.

        Args:
            item: The item to add to the inventory.
        """
    self.inventory.append(item)
    print(f"{item.name} added to your inventory.")

  def show_inventory(self):
    """
        Display the contents of the player's inventory.
        """
    print("Your Inventory:")
    if not self.inventory:
      print("No items in your inventory.")
    else:
      for item in self.inventory:
        print(f"- {item.name}")

# ATTACK

  def attack(self, enemy):
    """
    
        Attacks an enemy with the player's current weapon, or a default damage of 5 if no weapon is equipped.
        Args:
            enemy (Enemy): The enemy to attack.
        """
    if self.weapon:
      enemy.take_damage(self.weapon.damage)
      print(
        f"{self.name} attacks {enemy.name} for {self.weapon.damage} damage!")
    else:
      enemy.take_damage(5, self)
      print(f"{self.name} attacks {enemy.name} for 5 damage!")
      print(f"{enemy.name}'s health: {enemy.health}")
# ATTACK

# DEFEND

  def defend(self):
    """
        Increases the player's defense for the current turn, reducing the damage taken from the enemy's attack.
        """
    defense_multiplier = 0.3  # Assume defense multiplies incoming damage by 0.5 (50% reduction)
    self.defense *= defense_multiplier
    print(f"{self.name} defends and increases defense!")

  def reset_defense(self):
    """
        Resets the player's defense attribute to its original value.
        """
    self.defense = 1.0


# DEFEND

  def get_weapon(self, weapon):
    """
      Sets the player's current weapon to the specified weapon.

      Args:
        weapon (Weapon): The weapon to give to the player.
      """
    self.weapon = weapon
    print(f"{self.name} equips {weapon.name}!")
    return weapon  # add this line to return the weapon object

  def take_damage(self, damage):
    """
    Reduces the player's health by the amount of damage taken, considering the defense attribute.
    Args:
        damage (int): The amount of damage taken.
    """
    actual_damage = int(damage *
                        self.defense)  # Apply defense to reduce damage taken
    self.health -= actual_damage
    if self.health <= 0:
      print(f"{self.name} has been defeated!")

    self.reset_defense()  # Reset defense attribute after taking damage
    return actual_damage

  # SELF DESCRIBE
  def is_alive(self):
    """
        Checks if the player is alive.

        Returns:
            bool: True if the player's health is greater than zero, False otherwise.
        """
    return self.health > 0

  def self_describe(self):
    """
        Prints information about the player, including their name, health, and weapon (if they have one).
        """
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Score: {self.score}")
    if self.weapon:
      print(f"Weapon: {self.weapon.name}")
    else:
      print("No weapon equipped.")
    Player.show_inventory(self)
