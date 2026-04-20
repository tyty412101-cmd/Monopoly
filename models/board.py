from models.property import Property
from models.railroad import Railroad
from models.utility import Utility
from models.tile import Tile


class Board:
    def __init__(self):
        self.tiles = self.create_board()

    def get_tile(self, position):
        return self.tiles[position]

    def create_board(self):
        return [
            Tile("GO"),
            Property("Mediterranean", 60, [2,10,30,90,160,250], "brown"),
            Tile("Community Chest"),
            Property("Baltic", 60, [4,20,60,180,320,450], "brown"),
            Tile("Income Tax", lambda p, s: p.pay(200)),

            Railroad("Reading Railroad"),
            Property("Oriental", 100, [6,30,90,270,400,550], "lightblue"),
            Tile("Chance"),
            Property("Vermont", 100, [6,30,90,270,400,550], "lightblue"),
            Property("Connecticut", 120, [8,40,100,300,450,600], "lightblue"),

            Tile("Jail"),
            Property("St Charles", 140, [10,50,150,450,625,750], "pink"),
            Utility("Electric Company"),
            Property("States", 140, [10,50,150,450,625,750], "pink"),
            Property("Virginia", 160, [12,60,180,500,700,900], "pink"),

            Railroad("Pennsylvania Railroad"),
            Property("St James", 180, [14,70,200,550,750,950], "orange"),
            Tile("Community Chest"),
            Property("Tennessee", 180, [14,70,200,550,750,950], "orange"),
            Property("New York", 200, [16,80,220,600,800,1000], "orange"),

            Tile("Free Parking"),
            Property("Kentucky", 220, [18,90,250,700,875,1050], "red"),
            Tile("Chance"),
            Property("Indiana", 220, [18,90,250,700,875,1050], "red"),
            Property("Illinois", 240, [20,100,300,750,925,1100], "red"),

            Railroad("B&O Railroad"),
            Property("Atlantic", 260, [22,110,330,800,975,1150], "yellow"),
            Property("Ventnor", 260, [22,110,330,800,975,1150], "yellow"),
            Utility("Water Works"),
            Property("Marvin Gardens", 280, [24,120,360,850,1025,1200], "yellow"),

            Tile("Go To Jail"),
            Property("Pacific", 300, [26,130,390,900,1100,1275], "green"),
            Property("North Carolina", 300, [26,130,390,900,1100,1275], "green"),
            Tile("Community Chest"),
            Property("Pennsylvania Ave", 320, [28,150,450,1000,1200,1400], "green"),

            Railroad("Short Line"),
            Tile("Chance"),
            Property("Park Place", 350, [35,175,500,1100,1300,1500], "blue"),
            Tile("Luxury Tax", lambda p, s: p.pay(100)),
            Property("Boardwalk", 400, [50,200,600,1400,1700,2000], "blue"),
        ]
