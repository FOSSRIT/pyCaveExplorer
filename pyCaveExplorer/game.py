'''
Handles all the important methods of a pyCaveExplorer game.
Also manages all GameElement objects
'''

import pygame
from constants import *
from solver import Solver

class Game:
    def __init__(self):
        # WINDOW SETUP
        self.window = pygame.Surface((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
        
        # GRID SETUP
        self.populate_grid() # fills in colors
        print 'Drawing the grid'
        self.draw_grid() # draws grey grid lines
     

    def draw_grid(self):
        for x in range(GRID_WIDTH):
            pygame.draw.line(self.window, COLOR_GREY,
                (x * TILESIZE_X, 0),
                (x * TILESIZE_X, GAME_WINDOW_HEIGHT))
        for y in range(GRID_HEIGHT):
            pygame.draw.line(self.window, COLOR_GREY,
                (0, y * TILESIZE_Y),
                (GAME_WINDOW_WIDTH, y * TILESIZE_Y))

    def populate_grid(self):
        '''
        Draw grid squares to match grid created by solver
        '''
        # SOLVER
        self.solver = Solver()
        self.solver.populate(self.solver.grid)
        for row in self.solver.grid:
            for item in row:
                square_surface = pygame.Surface((TILESIZE_X, TILESIZE_Y))
                contents_surface = pygame.Surface((TILESIZE_X / 2,
                    TILESIZE_Y / 2))
                
                # print "Item", item # DEBUG
                # print "item x", item.x # DEBUG
                # print "item y", item.y # DEBUG
                
                element = self.solver.grid[item.x][item.y]
                
                # print "Element", element # DEBUG
                
                if element.group == ELEMENT_WALL:
                    # Draw dark grey square
                    square_surface.fill(COLOR_DARK_GREY)
                    # print "wall element at", item.x, item.y # DEBUG
                elif element.group == ELEMENT_PATH:
                    # Draw light brown square (or nothing)
                    square_surface.fill(COLOR_LIGHT_BROWN)
                    # print "path element at", item.x, item.y # DEBUG
                    for i in element.contents:
                        if i.group == ELEMENT_START:
                            # Draw green square onto grid
                            contents_surface.fill(COLOR_GREEN)
                            # print "start element here" # DEBUG
                        elif i.group == ELEMENT_GOAL:
                            # Draw blue square onto grid
                            contents_surface.fill(COLOR_BLUE)
                            # print "goal element here" # DEBUG
                        elif i.group == ELEMENT_TREASURE:
                            # Draw gold square onto grid
                            contents_surface.fill(COLOR_GOLD)
                            # print "treasure element here" # DEBUG
                
                # Draw the contents onto the square
                square_surface.blit(contents_surface, (10, 10))

                # Draw the square onto the grid
                self.window.blit(square_surface, (item.x * TILESIZE_X,
                    TILESIZE_Y * item.y))
        
    def draw(self, surface):
        '''
        Draws the game window onto the specified surface
        '''
        surface.blit(self.window, (GAME_WINDOW_ORIGIN_X, GAME_WINDOW_ORIGIN_Y))
        
   
    		
