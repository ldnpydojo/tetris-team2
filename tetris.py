import random
import pgzero

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

BOARD = [[' '] * 10 for _ in range(15)]
BOARD.append(['*'] * 10)


from pprint import pprint
pprint(BOARD)

class Piece:
    def __init__(self, data):
        self._data = data
        self.x = 5
        self.y = 0

    @property
    def data(self):
        return self._data

    def right(self):
        return self.x + len(self._data[0])

    def bottom(self):
        return self.y + len(self.data)

    def tiles(self):
        for y, line in enumerate(self._data):
            for x, char in enumerate(line):
                if char != ' ':
                    yield x + self.x, y + self.y

    def collides(self):
        for x, y in self.tiles():
            if BOARD[y][x] != ' ':
                return True
        return False


def get_piece():
    return Piece(random.choice(PIECES))


CURRENT_PIECE = get_piece()

BOARD_WIDTH = 10

def draw():
    screen.fill((0, 0, 0))

    screen.draw.rect(Rect((0, 0), (32 * 10, 32 * 15)), (255, 255, 255))

    piece = CURRENT_PIECE
    for x, y in piece.tiles():
            screen.draw.filled_rect(Rect(((x)*32, (y)*32), (32, 32)), (255, 255, 255))

    for y, row in enumerate(BOARD):
        for x, char in enumerate(row):
            if char != ' ':
                screen.draw.filled_rect(Rect((x*32, y*32), (32, 32)), (255, 255, 255))




def on_key_down(key):
    if key == keys.LEFT:
        if CURRENT_PIECE.x:
            CURRENT_PIECE.x -= 1
            if CURRENT_PIECE.collides():
                CURRENT_PIECE.x += 1

    elif key == keys.RIGHT:
        if CURRENT_PIECE.right() < BOARD_WIDTH:
            CURRENT_PIECE.x += 1
            if CURRENT_PIECE.collides():
                CURRENT_PIECE.x -= 1

    elif key == keys.DOWN:
        ticky()
    
    elif key == keys.UP:
        piece = CURRENT_PIECE
        while CURRENT_PIECE == piece:
            ticky()

def ticky():
    global CURRENT_PIECE
    global BOARD
    CURRENT_PIECE.y += 1
    
    if CURRENT_PIECE.collides():
        CURRENT_PIECE.y -= 1
        for x, y in CURRENT_PIECE.tiles():
            BOARD[y][x] = '*'

        completed_rows = []

        for y, row in enumerate(BOARD):
            row_complete = not any(char==' ' for char in row)
            if row_complete:
                completed_rows.append(y)

        BOARD = [row for y, row in enumerate(BOARD) if y not in completed_rows]


        CURRENT_PIECE = get_piece()



clock.schedule_interval(ticky, 0.25)
