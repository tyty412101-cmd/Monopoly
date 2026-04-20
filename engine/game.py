from .player import Player
from .board import create_board
from .dice import roll
from .rules import *

class Game:
    def __init__(self, names, ui):
        self.players = [Player(n) for n in names]
        self.board = create_board()
        self.turn = 0
        self.ui = ui
        self.houses_left = 32
        self.hotels_left = 12

    def current(self):
        return self.players[self.turn]

    def next_turn(self):
        p = self.current()
        if p.bankrupt:
            self.turn = (self.turn+1) % len(self.players)
            return

        self.ui.show_turn(p)

        if handle_jail(self, p):
            self.turn = (self.turn+1) % len(self.players)
            return

        doubles_count = 0

        while True:
            d1, d2, total = roll()
            self.ui.show_roll(d1, d2)

            if d1 == d2:
                doubles_count += 1
                if doubles_count == 3:
                    send_to_jail(p)
                    return
            else:
                doubles_count = 0

            move_player(self, p, total)

            if d1 != d2:
                break

        self.turn = (self.turn+1) % len(self.players)

    def play(self):
        while True:
            alive = [p for p in self.players if not p.bankrupt]
            if len(alive) == 1:
                self.ui.show_winner(alive[0])
                break
            self.next_turn()
