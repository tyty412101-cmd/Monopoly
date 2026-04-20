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

            Tile("Jail"),

            Property("St. Charles Place", 140, 10),
            Utility("Electric Company"),
            Property("States Avenue", 140, 10),
            Property("Virginia Avenue", 160, 12),

            Railroad("Pennsylvania Railroad"),

            Property("St. James Place", 180, 14),
            Tile("Community Chest"),
            Property("Tennessee Avenue", 180, 14),
            Property("New York Avenue", 200, 16),

            Tile("Free Parking"),

            Property("Kentucky Avenue", 220, 18),
            Tile("Chance"),
            Property("Indiana Avenue", 220, 18),
            Property("Illinois Avenue", 240, 20),

            Railroad("B. & O. Railroad"),

            Property("Atlantic Avenue", 260, 22),
            Property("Ventnor Avenue", 260, 22),
            Utility("Water Works"),
            Property("Marvin Gardens", 280, 24),

            Tile("Go To Jail"),

            Property("Pacific Avenue", 300, 26),
            Property("North Carolina Avenue", 300, 26),
            Tile("Community Chest"),
            Property("Pennsylvania Avenue", 320, 28),

            Railroad("Short Line"),

            Tile("Chance"),
            Property("Park Place", 350, 35),
            Tile("Luxury Tax"),
            Property("Boardwalk", 400, 50),
        ]

    def get_tile(self, position):
        return self.tiles[position]
