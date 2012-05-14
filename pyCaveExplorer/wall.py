'''
Wall object for pyCaveExplorer
    * Blocks the player's path
'''

from element import GameElement
from constants import *

class Wall(GameElement):
    def __init__(self, *args, **kwargs):
        super(Wall, self).__init__(*args, **kwargs)
        self.type = ELEMENT_WALL
        pass
