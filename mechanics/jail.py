def handle_jail(player, roll):
    player.jail_turns += 1

    if roll % 2 == 0:
        print("Rolled doubles → OUT OF JAIL")
        player.in_jail = False
        player.move(roll)
        return

    if player.jail_turns >= 3:
        print("Paid 50 to leave jail")
        player.pay(50)
        player.in_jail = False
