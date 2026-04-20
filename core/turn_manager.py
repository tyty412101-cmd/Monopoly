class TurnManager:
    def __init__(self, players):
        self.players = players
        self.current_index = 0

    def current_player(self):
        return self.players[self.current_index]

    def next_turn(self):
        self.current_index = (self.current_index + 1) % len(self.players)
        return self.current_player()
