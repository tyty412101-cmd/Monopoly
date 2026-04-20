class Property:
    def __init__(self, name, price, rents, color):
        self.name = name
        self.price = price
        self.rents = rents  # [base, 1h, 2h, 3h, 4h, hotel]
        self.color = color
        self.owner = None
        self.houses = 0
        self.hotel = False
        self.mortgaged = False

    def get_rent(self):
        if self.mortgaged:
            return 0

        if self.hotel:
            return self.rents[5]

        return self.rents[self.houses]
