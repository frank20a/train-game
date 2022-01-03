from utils.Colours import *
from Cards import *


class Hand:
    def __init__(self):
        self.tickets = []
        self.trains = []
        self.finished_tickets = []


class Player:
    def __init__(self, board, colour):
        self.board = board
        self.colour = Colour.pre(colour)
        self.hand = Hand()
        self.stations = 3
        self.trains = 45

    def draw_closed(self):
        pass

    def draw(self, n):
        if not 0 <= n <= 5:
            raise IndexError

    def make_route(self, route):
        pass

    def make_station(self):
        self.stations -= 1
