from core.state import GameState
from core.turn_manager import TurnManager
from models.player import Player
from models.board import Board
from mechanics.dice import roll_dice

class Game:
    def __init__(self):
        self.state = GameState.SETUP
        self.players = []
        self.board = Board()
        self.turn_manager = None

    def setup(self):
        print("=== MONOPOLY SETUP ===")

        num_players = int(input("Number of players: "))
        for i in range(num_players):
            name = input(f"Player {i+1} name: ")
            self.players.append(Player(name))

        self.turn_manager = TurnManager(self.players)
        self.state = GameState.RUNNING

    def run(self):
        print("=== GAME START ===")

        while self.state == GameState.RUNNING:
            player = self.turn_manager.current_player()
            print(f"\n{player.name}'s turn")

            dice = roll_dice()
            print(f"Rolled: {dice}")

            player.move(dice, len(self.board.tiles))
            tile = self.board.get_tile(player.position)

            print(f"Landed on: {tile.name}")
            tile.on_land(player, self)

            if player.money <= 0:
                print(f"{player.name} is bankrupt!")
                self.players.remove(player)
                if len(self.players) == 1:
                    print(f"{self.players[0].name} wins!")
                    self.state = GameState.ENDED
                    break

            self.turn_manager.next_turn()
