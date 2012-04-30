'''
Generates and solves the grid in pyCaveExplorer
'''

from constants import *
from game import Game
from path import Path

class Solver:
    def __init__(self):
        # GAME INITIALIZATION #
        self.game = Game() # the game object
        self.grid = [
            [Path(i, x) for x in range(GRID_HEIGHT)]
            for i in range(GRID_WIDTH)
        ]

    def populate(self):
        '''Populate the grid'''
        self.start_set = False # start point has not been placed
        self.goal_set = False # end point has not been placed
        for row in self.grid:
            for col in self.grid:
                print row, col

s = Solver()
s.populate()
