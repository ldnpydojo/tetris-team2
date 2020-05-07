from numpy import random
COLOUR_LIST = [(255,255,255),
               (255,255,0),
               (255,0,0),
               (0,255,0),
               (0,0,255),
               (255,0,255),
               (0,255,255)]

def choose_random_colour():
    return random.choice(COLOUR_LIST)