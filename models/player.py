class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
        self.in_jail = False

    def move(self, steps, board):
        self.position = (self.position + steps) % len(board.tiles)

        if self.position < steps:
            self.money += 200
            print(f"{self.name} passed GO! +$200")

    def pay(self, amount):
        self.money -= amount

    def receive(self, amount):
        self.money += amount
