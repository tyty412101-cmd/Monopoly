from models.tile import Tile

class Railroad(Tile):
    def __init__(self, name):
        super().__init__(name)
        self.price = 200
        self.owner = None

    def rent(self):
        if not self.owner:
            return 0
        count = sum(1 for p in self.owner.properties if isinstance(p, Railroad))
        return 25 * (2 ** (count - 1))

    def on_land(self, player):
        if self.owner is None:
            choice = input(f"Buy {self.name} for $200? (y/n): ")
            if choice.lower() == "y" and player.money >= 200:
                player.pay(200)
                self.owner = player
                player.properties.append(self)
        elif self.owner != player:
            rent = self.rent()
            print(f"Pay railroad rent: ${rent}")
            player.pay(rent)
            self.owner.receive(rent)
