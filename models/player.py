class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
        self.in_jail = False

    def move(self, steps, board_size):
        self.position = (self.position + steps) % board_size

    def pay(self, amount):
        self.money -= amount

    def receive(self, amount):
        self.money += amount

    def __str__(self):
        return f"{self.name} ($ {self.money})"
