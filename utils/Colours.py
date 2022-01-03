class Colour:
    shorts = {}

    def __init__(self, name, rgb, short=None):
        self.name = name
        self.rgb = tuple(rgb)

        if short is None:
            self.short = name[0]
        else:
            self.short = short
        Colour.shorts[self.short] = self

        self.hex = "#"
        for c in self.rgb:
            self.hex += str(hex(c)).strip('0x').rjust(2, '0')

    @classmethod
    def pre(cls, shortcode):
        if shortcode not in cls.shorts.keys():
            return None
        return cls.shorts[shortcode]

    def __eq__(self, other):
        if self.rgb[0] == -1 or other.rgb == -1:
            return True

        return self.rgb == other.rgb


PINK = Colour('pink', [255, 192, 203])
WHITE = Colour('white', [255, 255, 255])
BLUE = Colour('blue', [0, 0, 255])
YELLOW = Colour('yellow', [255, 255, 0])
ORANGE = Colour('orange', [255,140,0])
BLACK = Colour('black', [0, 0, 0], 'bl')
RED = Colour('red', [255, 0, 0])
GREEN = Colour('green', [0, 255, 0])
_JOKER = Colour('jocker', [-1, -1, -1])

CYAN = Colour('cyan', [0, 255, 255])
MAGENDA = Colour('magenta', [255, 0, 255])

if __name__ == '__main__':
    print(YELLOW.hex)