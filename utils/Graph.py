from utils.Colours import *


class City:
    def __init__(self, name, position):
        self.conns = []
        self.station = None
        self.pos = position
        self.name = name

    def __str__(self):
        return self.name

    def has_child(self, target) -> bool:
        for conn in self.conns:
            if conn.connects_to(target):
                return True
        return False

    def has_station(self) -> bool:
        return self.station is not None

    def set_station(self, col):
        self.station = Colour.pre(col)

    def connects_to(self, player, target) -> bool:
        if self == target:
            return True

        for conn in self.conns:
            if conn.owner == player:
                if conn.connects_to(player, target):
                    return True

        return False


class Connection:
    def __init__(self, inbound, outbound, length, colour=None, tunnel=False):
        self.child_1 = inbound
        self.child_2 = outbound
        self.colour = colour
        self.length = length
        self.tunnel = tunnel
        self.owner = None

    def connects(self, target_1, target_2) -> bool:
        return (target_1 == self.child_1 and target_2 == self.child_2) or \
               (target_1 == self.child_2 and target_2 == self.child_1)

    def connects_to(self, target) -> bool:
        return target == self.child_2 or target == self.child_1
