from models.tile import Tile
from models.property import Property
from models.railroad import Railroad
from models.utility import Utility

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
            Railroad("Reading Railroad"),
            Property("Oriental Avenue", 100, 6),
            Tile("Chance"),
            Property("Vermont Avenue", 100, 6),
            Property("Connecticut Avenue", 120, 8),
        ]

    def get_tile(self, position):
        return self.tiles[position]
