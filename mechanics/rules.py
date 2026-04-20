class Rules:
    def handle_tile(self, player, tile):
        tile.on_land(player)

        if player.money < 0:
            print(f"{player.name} is bankrupt!")
            exit()
