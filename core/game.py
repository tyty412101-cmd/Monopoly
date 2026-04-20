from core.state import GameState
from core.turn_manager import TurnManager

from models.player import Player
from models.board import Board

from mechanics.dice import Dice
from mechanics.rules import Rules

class Game:
    def __init__(self):
        self.state = GameState()

        self.dice = Dice()
        self.rules = Rules()

        self.turn_manager = TurnManager(
            self.state,
            self.dice,
            self.rules
        )

    def setup(self):
        print("=== MONOPOLY SETUP ===")

        num_players = int(input("Number of players: "))

        for i in range(num_players):
            name = input(f"Player {i+1} name: ")
            self.state.players.append(Player(name))

        self.state.board = Board()

    def start(self):
        self.setup()

        while self.state.is_running:
            self.turn_manager.play_turn()
