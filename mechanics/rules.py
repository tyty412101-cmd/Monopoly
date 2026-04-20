from mechanics.transactions import pay_player


def handle_space(player, tile, state):
    print(f"Landed on {tile.name}")

    if hasattr(tile, "price"):
        if tile.owner is None:
            if player.money >= tile.price:
                print(f"Bought {tile.name}")
                player.money -= tile.price
                tile.owner = player
                player.properties.append(tile)
        elif tile.owner != player:
            rent = tile.get_rent() if hasattr(tile, "get_rent") else 25
            print(f"Pay rent: {rent}")
            pay_player(player, tile.owner, rent)

    elif tile.name == "Go To Jail":
        player.go_to_jail()

    elif tile.action:
        tile.action(player, state)
