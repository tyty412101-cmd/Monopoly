class Card:
    def __init__(self, description, action):
        self.description = description
        self.action = action

    def apply(self, player, game):
        print(self.description)
        self.action(player, game)
