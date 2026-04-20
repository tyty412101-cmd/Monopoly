from core.state import GameState
from core.turn_manager import TurnManager
from models.board import Board
from models.player import Player
from mechanics.dice import roll_dice


class Game:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.board = Board()
        self.state = GameState(self.players, self.board)
        self.turn_manager = TurnManager(self.state)

    def start(self):
        print("=== MONOPOLY START ===")

        while not self.state.is_game_over():
            player = self.turn_manager.current_player()
            print(f"\n--- {player.name}'s turn ---")

            dice1, dice2 = roll_dice()
            total = dice1 + dice2
            print(f"Rolled: {dice1} + {dice2} = {total}")

            self.turn_manager.handle_turn(player, total, dice1 == dice2)

        winner = self.state.get_winner()
        print(f"\n🏆 Winner: {winner.name}")
