'''
Handles all the important methods of a pyCaveExplorer game.
Also manages all GameElement objects
'''

import pygame
from constants import *
from solver import Solver

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

        self.draw_grid()

    def draw_grid(self):
        '''
        Draw grid squares to match grid created by solver
        '''
        # SOLVER
        self.solver = Solver()
        self.solver.populate()
        for row in self.solver.grid:
            for item in row:
                print "Item", item # DEBUG
                print "item x", item.x # DEBUG
                print "item y", item.y # DEBUG
                element = self.solver.grid[item.x / TILESIZE_X] \
                    [item.y / TILESIZE_Y]
                print "Element", element # DEBUG
                if element.type == ELEMENT_WALL:
                    # Draw dark grey square
                    print "wall element at", item.x, item.y
                    pass
                elif element.type == ELEMENT_PATH:
                    # Draw light brown square (or nothing)
                    print "path element at", item.x, item.y
                    pass

    def draw(self, surface):
        '''
        Draws the game window onto the specified surface
        '''
        surface.blit(self.window, (GAME_WINDOW_ORIGIN_X, GAME_WINDOW_ORIGIN_Y))
