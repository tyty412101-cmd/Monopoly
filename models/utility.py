from models.tile import Tile

class Utility(Tile):
    def __init__(self, name):
        super().__init__(name)
        self.price = 150
        self.owner = None

    def on_land(self, player, dice_roll=None):
        if self.owner is None:
            choice = input(f"Buy {self.name} for $150? (y/n): ")
            if choice.lower() == "y" and player.money >= 150:
                player.pay(150)
                self.owner = player
                player.properties.append(self)
        elif self.owner != player:
            count = sum(1 for p in self.owner.properties if isinstance(p, Utility))
            multiplier = 10 if count == 2 else 4
            rent = multiplier * (dice_roll if dice_roll else 7)
            print(f"Pay utility rent: ${rent}")
            player.pay(rent)
            self.owner.receive(rent)
