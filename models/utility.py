class Utility:
    def __init__(self, name):
        self.name = name
        self.price = 150
        self.owner = None

    def get_rent(self, owner, dice_roll):
        count = sum(1 for u in owner.properties if isinstance(u, Utility))
        return dice_roll * (10 if count == 2 else 4)
