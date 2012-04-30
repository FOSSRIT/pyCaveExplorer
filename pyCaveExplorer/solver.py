'''
Generates and solves the grid in pyCaveExplorer
'''

from game import Game

class Solver:
    def __init__(self):
        self.game = Game()
    def init_grid(self):
        '''Sets up the game grid'''
        grid = []
