'''
Starting tile for player on a level
Randomly picked out of empty path tiles
'''

from element import GameElement
from constants import *

class Start(GameElement):
    def __init__(self, *args, **kwargs):
        super(Start, self).__init__(*args, **kwargs)
        self.group = ELEMENT_START
        pass
