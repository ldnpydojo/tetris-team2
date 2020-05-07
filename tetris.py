import random
import pgzero
import colours

LONG_BOI = [ "xxxx"]

MR_T = [ "   ", "xxx", " x "]

THE_ROCK = ["xx", "xx"]

SNAKE = ["xx ", " xx"]

SNAKE_TOO = [" xx", "xx "]

JAY = ["  x", "xxx"]

SILENT_BOB = ["x  ", "xxx"]

def rotate_90(data):
    return list(zip(*data))

def rotate_180(data):
    return [s[::-1] for s in data[::-1]]

def rotations(candidate):
    yield candidate
    yield rotate_90(candidate)
    yield rotate_180(candidate)
    yield rotate_90(rotate_180(candidate))

def and90(candidate):
    return [candidate, rotate_90(candidate)]

PIECES = [
        list(rotations(MR_T)),
        [THE_ROCK],
        and90(LONG_BOI),
        and90(SNAKE),
        and90(SNAKE_TOO),
        and90(JAY),
        and90(SILENT_BOB)]


BOARD = [['*'] + ([' '] * 10) + ['*'] for _ in range(15)]
BOARD.append(['*'] * 12)

class Piece:
    def __init__(self, data):
        self._data = data
        self.x = 5
        self.y = 0
        self.orientation = 0
        self.colour = colours.choose_random_colour()

    @property
    def data(self):
        return self._data[self.orientation]

    def rotate(self):

        old_orientation = self.orientation
        self.orientation += 1
        if self.orientation == len(self._data):
            self.orientation = 0

        if self.collides():
            self.orientation = old_orientation

    def right(self):
        return self.x + len(self.data)

    def bottom(self):
        return self.y + len(self.data)

    def tiles(self):
        for y, line in enumerate(self.data):
            for x, char in enumerate(line):
                if char != ' ':
                    yield x + self.x, y + self.y

    def collides(self):
        try:
            for x, y in self.tiles():
                if BOARD[y][x] != ' ':
                    return True
            return False
        except:
            return False


def get_piece():
    return Piece(random.choice(PIECES))


CURRENT_PIECE = get_piece()

BOARD_WIDTH = 10

GAME_STOP = False

def draw():

    if GAME_STOP:
        screen.fill((255, 0, 0))
    else:
        screen.fill((0, 0, 0))


    piece = CURRENT_PIECE
    for x, y in piece.tiles():
            screen.draw.filled_rect(Rect(((x)*32, (y)*32), (32, 32)), piece.colour)

    for y, row in enumerate(BOARD):
        for x, char in enumerate(row):
            colour = (255, 255, 255)
            if char != ' ':
                if isinstance(char, tuple):
                    colour = char
                screen.draw.filled_rect(Rect((x*32, y*32), (32, 32)), colour)

    if GAME_STOP:
        screen.blit('gameover.png', (64, 64))



def on_key_down(key):
    if key == keys.LEFT:
        CURRENT_PIECE.x -= 1
        if CURRENT_PIECE.collides():
            CURRENT_PIECE.x += 1

    elif key == keys.RIGHT:
        CURRENT_PIECE.x += 1
        if CURRENT_PIECE.collides():
            CURRENT_PIECE.x -= 1

    elif key == keys.DOWN:
        ticky()

    elif key == keys.SPACE:
        CURRENT_PIECE.rotate()
    
    elif key == keys.UP:
        piece = CURRENT_PIECE
        while CURRENT_PIECE == piece:
            ticky()

def ticky():
    global CURRENT_PIECE
    global BOARD
    global GAME_STOP

    if GAME_STOP:
        return

    CURRENT_PIECE.y += 1
    
    if CURRENT_PIECE.collides():
        CURRENT_PIECE.y -= 1
        for x, y in CURRENT_PIECE.tiles():
            BOARD[y][x] = CURRENT_PIECE.colour

        completed_rows = []

        for y, row in enumerate(BOARD[0:-1]):
            row_complete = not any(char==' ' for char in row)
            if row_complete:
                completed_rows.append(y)

        BOARD = [row for y, row in enumerate(BOARD) if y not in completed_rows]

        for _ in completed_rows:
            BOARD.insert(0, ['.'] + ([' '] * BOARD_WIDTH) + ['.'])

        CURRENT_PIECE = get_piece()

        if CURRENT_PIECE.collides():
           GAME_STOP = True 



clock.schedule_interval(ticky, 0.25)
