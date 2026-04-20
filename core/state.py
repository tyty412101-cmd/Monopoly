class GameState:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.current_index = 0

    def next_player(self):
        self.current_index = (self.current_index + 1) % len(self.players)

    def get_active_players(self):
        return [p for p in self.players if not p.bankrupt]

    def is_game_over(self):
        return len(self.get_active_players()) == 1

    def get_winner(self):
        return self.get_active_players()[0]
