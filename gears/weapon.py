class Weapon:

  def __init__(self, name, durability=1, damage=10):
    self.name = name
    self.durability = durability
    self.damage = damage

  def attack(self, enemy):
    """
        Attacks an enemy with the weapon's strength, reducing the weapon's durability by 1.

        Args:
            enemy (Enemy): The enemy to attack.
        """
    enemy.take_damage(self.damage)
    self.durability -= 1
    if self.durability <= 0:
      print(f"{self.name} has broken!")
      self.strength = 0

  def take_damage(self, damage):
    """
        Reduces the weapon's durability by the given amount of damage.

        Args:
            damage (int): The amount of damage to take.
        """
    self.durability -= damage
    if self.durability <= 0:
      print(f"The {self.name} has broken!")
      self.damage = 0

  def __str__(self):
    return f"{self.name} (Durability: {self.durability}, Damage: {self.damage})"
