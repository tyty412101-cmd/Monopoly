from mechanics.transactions import pay_player, pay_bank
from mechanics.jail import handle_jail
from mechanics.rules import handle_space


class TurnManager:
    def __init__(self, state):
        self.state = state
        self.double_count = 0

    def current_player(self):
        return self.state.players[self.state.current_index]

    def handle_turn(self, player, roll, is_double):
        if player.in_jail:
            handle_jail(player, roll)
            self.state.next_player()
            return

        if is_double:
            self.double_count += 1
        else:
            self.double_count = 0

        if self.double_count == 3:
            print("Rolled 3 doubles → GO TO JAIL")
            player.go_to_jail()
            self.double_count = 0
            self.state.next_player()
            return

        player.move(roll)

        if player.position < roll:
            print("Passed GO → +200")
            player.money += 200

        tile = self.state.board.get_tile(player.position)
        handle_space(player, tile, self.state)

        if not is_double:
            self.state.next_player()
