'''
Handles all the important methods of a pyCaveExplorer game.
Also manages all GameElement objects
'''

import pygame
from constants import *

class Game:
    def __init__(self):
        self.window = pygame.Surface((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
        
        # GRID SETUP
        self.window.fill(COLOR_BROWN)
        for x in range(GRID_WIDTH):
            pygame.draw.line(self.window, COLOR_GREY,
                (x * TILESIZE_X, 0),
                (x * TILESIZE_X, GAME_WINDOW_HEIGHT))
        for y in range(GRID_HEIGHT):
            pygame.draw.line(self.window, COLOR_GREY,
                (0, y * TILESIZE_Y),
                (GAME_WINDOW_WIDTH, y * TILESIZE_Y))

        # SOLVER
    def draw(self, surface):
        '''
        Draws the game window onto the specified surface
        '''
        surface.blit(self.window, (GAME_WINDOW_ORIGIN_X, GAME_WINDOW_ORIGIN_Y))
