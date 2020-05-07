import random

PIECES = [
        [ "xxxx"],
        [ " x ", 
          "xxx" ],
        [ "xx"
          "xx" ],
         ["xx ",
          " xx"],
         [" xx",
          "xx "],
         ["x  ",
          "xxx"]
         ,
         ["  x",
          "xxx"]]

BOARD = [[" " * 10] for _ in range(20)]


class Piece:
    def __init__(self, data):
        self._data = data
        self._x = 5
        self._y = 0

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


def get_piece():
    return Piece(random.choice(PIECES))


CURRENT_PIECE = get_piece()

