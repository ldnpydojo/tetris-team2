from numpy import random

COLOUR_DICT = {"white":  (255,255,255),
               "yellow": (255,255,0),
               "red": (255,0,0),
               "green": (0,255,0),
               "blue": (0,0,255),
               "magenta": (255,0,255),
               "cyan": (0,255,255)}

COLOUR_LIST = list(COLOUR_DICT.keys())

def choose_random_colour():
    return COLOUR_DICT[random.choice(COLOUR_LIST)]