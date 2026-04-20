def transfer_money(from_player, to_player, amount):
    from_player.pay(amount)
    to_player.receive(amount)
