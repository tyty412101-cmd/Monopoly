from models.tile import Tile
from models.property import Property

class Board:
    def __init__(self):
        self.tiles = self.create_board()

    def create_board(self):
        return [
            Tile("GO"),
            Property("Mediterranean Avenue", 60, 2),
            Tile("Community Chest"),
            Property("Baltic Avenue", 60, 4),
            Tile("Income Tax"),
            Property("Reading Railroad", 200, 25),
            Property("Oriental Avenue", 100, 6),
            Tile("Chance"),
            Property("Vermont Avenue", 100, 6),
            Property("Connecticut Avenue", 120, 8),
        ]

    def get_tile(self, position):
        return self.tiles[position]
