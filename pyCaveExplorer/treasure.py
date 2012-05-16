'''
Treasure object for pyCaveExplorer
    * randomly dropped in available path squares
    * give player shiny trinkets or spare lights/batteries
'''

from element import GameElement
from constants import *

class Treasure(GameElement):
    def __init__(self, *args, **kwargs):
        super(Treasure, self).__init__(*args, **kwargs)
        self.group = ELEMENT_TREASURE
        pass
