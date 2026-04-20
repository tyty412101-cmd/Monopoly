class TurnManager:
    def __init__(self, state, dice, rules):
        self.state = state
        self.dice = dice
        self.rules = rules

    def play_turn(self):
        player = self.state.current_player()

        print(f"\n--- {player.name}'s turn ---")

        roll = self.dice.roll()
        print(f"Rolled: {roll}")

        player.move(roll, self.state.board)

        tile = self.state.board.get_tile(player.position)
        print(f"Landed on: {tile.name}")

        self.rules.handle_tile(player, tile)

        self.state.next_turn()
