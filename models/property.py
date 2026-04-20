from models.tile import Tile

class Property(Tile):
    def __init__(self, name, price, rent):
        super().__init__(name)
        self.price = price
        self.rent = rent
        self.owner = None

    def on_land(self, player):
        if self.owner is None:
            choice = input(f"Buy {self.name} for ${self.price}? (y/n): ")
            if choice.lower() == "y" and player.money >= self.price:
                player.pay(self.price)
                self.owner = player
                player.properties.append(self)
                print(f"{player.name} bought {self.name}")
        else:
            if self.owner != player:
                print(f"Pay rent: ${self.rent}")
                player.pay(self.rent)
                self.owner.receive(self.rent)
