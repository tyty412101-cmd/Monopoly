class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
        self.in_jail = False
        self.jail_turns = 0
        self.bankrupt = False

    def move(self, steps):
        self.position = (self.position + steps) % 40

    def go_to_jail(self):
        self.position = 10
        self.in_jail = True
        self.jail_turns = 0

    def pay(self, amount):
        self.money -= amount
        if self.money < 0:
            self.bankrupt = True

    def receive(self, amount):
        self.money += amount
