'''
Goal object for pyCaveExplorer
'''

from element import GameElement
from constants import *

class Goal(GameElement):
    def __init__(self, *args, **kwargs):
        super(Goal, self).__init__(*args, **kwargs)
        self.group = ELEMENT_GOAL
        pass
