'''
Controls shadows on grid tiles
'''

from constants import *
from element import GameElement

class Shadows(GameElement):
    def __init__(self, *args, **kwargs):
        super(Shadows, self).__init__(*args, **kwargs)
        self.darkness = LIGHT_LOW # how dark the tile is, between 0 and 255
