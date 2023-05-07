class Consumable:
    def __init__(self, name, health_effect):
        self.name = name
        self.health_effect = health_effect

    def use(self, player):
        player.health += self.health_effect
        print(f"{player.name} used {self.name} and gained {self.health_effect} health!")
        print(f"{player.name}'s is at {player.health}.")
