class Railroad:
    def __init__(self, name):
        self.name = name
        self.price = 200
        self.owner = None

    def get_rent(self, owner):
        count = sum(1 for r in owner.properties if isinstance(r, Railroad))
        return 25 * (2 ** (count - 1))
