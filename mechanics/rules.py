class Rules:
    def handle_tile(self, player, tile):
        name = tile.name

        if name == "Income Tax":
            print("Pay $200 tax")
            player.pay(200)

        elif name == "Luxury Tax":
            print("Pay $100 tax")
            player.pay(100)

        elif name == "Go To Jail":
            print("Go to Jail!")
            player.position = 10
            player.in_jail = True

        elif name == "Jail":
            print("Just visiting jail")

        elif name in ["Chance", "Community Chest"]:
            print(f"{name} card system coming next...")

        else:
            try:
                tile.on_land(player)
            except TypeError:
                tile.on_land(player)

        if player.money < 0:
            print(f"{player.name} is bankrupt!")
            exit()
