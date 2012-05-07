'''
Handles all the important methods of a pyCaveExplorer game.
Also manages all GameElement objects
'''

import pygame
from constants import *

class Game:
    def __init__(self):
        self.window = pygame.Surface((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
        self.window.fill(COLOR_BROWN)
        # Set up grid
        # Solver stuff
        self.draw()
    def draw(self):
        # Draw the grid
        pygame.draw.line(self.window, COLOR_GREY, (100, 0), (100, 300), 4) 
        pass
