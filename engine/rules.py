def send_to_jail(player):
    player.pos = 10
    player.in_jail = True
    player.jail_turns = 0

def handle_jail(game, player):
    if not player.in_jail:
        return False

    game.ui.show_message(f"{player.name} is in jail")

    if player.get_out_cards:
        use = game.ui.choose("Use Get Out of Jail card? (y/n)")
        if use == "y":
            player.get_out_cards -= 1
            player.in_jail = False
            return False

    if player.jail_turns == 2:
        player.money -= 50
        player.in_jail = False
        return False

    player.jail_turns += 1
    return True

def move_player(game, player, steps):
    old = player.pos
    player.pos = (player.pos + steps) % 40

    if player.pos < old:
        player.money += 200

    tile = game.board[player.pos]
    resolve_tile(game, player, tile)

def resolve_tile(game, player, tile):
    if tile.type == "property":
        handle_property(game, player, tile)
    elif tile.type == "chance":
        game.ui.draw_chance(player)
    elif tile.type == "community":
        game.ui.draw_community(player)
    elif tile.type == "tax":
        player.money -= tile.amount
    elif tile.type == "goto_jail":
        send_to_jail(player)

def handle_property(game, player, prop):
    if not prop.owner:
        buy = game.ui.choose(f"Buy {prop.name} for {prop.cost}? y/n")
        if buy == "y":
            player.money -= prop.cost
            prop.owner = player
            player.properties.append(prop)
        else:
            auction(game, prop)
    elif prop.owner != player:
        rent = calculate_rent(game, prop)
        player.money -= rent
        prop.owner.money += rent

def calculate_rent(game, prop):
    if prop.group == "railroad":
        count = sum(1 for p in prop.owner.properties if p.group == "railroad")
        return 25 * (2 ** (count-1))

    if prop.group == "utility":
        # dice-based rent handled elsewhere
        return 100

    return prop.rents[prop.houses]

def auction(game, prop):
    bids = {}
    for p in game.players:
        bid = int(game.ui.choose(f"{p.name} bid (0 skip): "))
        if bid <= p.money:
            bids[p] = bid

    if bids:
        winner = max(bids, key=bids.get)
        price = bids[winner]
        winner.money -= price
        winner.properties.append(prop)
        prop.owner = winner
