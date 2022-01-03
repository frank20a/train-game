from utils.Colours import *

class Card:
    def __init__(self):
        pass


class TrainCard(Card):
    count = 0

    def __init__(self, colour=None, jocker=False):
        super().__init__()

        self.id = TrainCard.count
        TrainCard.count += 1

        self.colour = Colour.pre(colour)
        self.jocker = jocker

    def isColour(self, colour):
        if self.jocker:
            return True

        return colour.short == self.colour.short


class TicketCard(Card):
    def __init__(self, outbound, inbound, points):
        super().__init__()
        self.outbound = outbound
        self.inbound = inbound
        self.points = points
