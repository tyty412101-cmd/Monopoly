def pay_player(payer, receiver, amount):
    payer.pay(amount)
    receiver.receive(amount)

def pay_bank(player, amount):
    player.pay(amount)
