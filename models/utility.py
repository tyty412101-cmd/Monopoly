from models.property import Property

class Utility(Property):
    def __init__(self, name):
        super().__init__(name, price=150, rent=20)
