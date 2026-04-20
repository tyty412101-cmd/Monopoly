class GameState:
    def __init__(self):
        self.players = []
        self.current_player_index = 0
        self.board = None
        self.is_running = True

    def current_player(self):
        return self.players[self.current_player_index]

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
