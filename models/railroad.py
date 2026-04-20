from models.property import Property

class Railroad(Property):
    def __init__(self, name):
        super().__init__(name, price=200, rent=25)
