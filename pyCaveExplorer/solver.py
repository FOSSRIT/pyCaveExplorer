'''
Generates and solves the grid in pyCaveExplorer
'''

import random # perhaps be more specific?
from constants import *
from path import Path
from wall import Wall
from treasure import Treasure
from start import Start
from goal import Goal

class Solver:
    def __init__(self):
        # GAME INITIALIZATION #
        self.grid = [
            [Path(i, x) for x in range(GRID_HEIGHT)]
            for i in range(GRID_WIDTH)
        ]

    def populate(self):
        '''Populate the grid'''
        # TODO: X and Y coordinates for drawing are being done strangley.
        # Once we get to screen drawing, we'll have to figure that out.
        # I sort of half-assedly did it for now. Not sure if it'd work.
        self.start_point = None # start point has not been placed
        self.goal_point = None # end point has not been placed
        for row in self.grid:
            for col in row:
                square_type = random.randint(0, 1)
                # 0 : make a wall.
                # 1 : make a path.
                if square_type == 0:
                    self.grid[col.x][col.y] = \
                        Wall(col.x * TILESIZE_X, col.y * TILESIZE_Y)
                    print("Wall generated at {}, {}".format(col.x, col.y))
                elif square_type == 1:
                    self.grid[col.x][col.y] = \
                        Path(col.x * TILESIZE_X, col.y * TILESIZE_Y)
                    print("Path generated at {}, {}".format(col.x, col.y)),
                    path_type = random.randint(0, (TILE_TYPES - 1))
                    # 0 : make starting point (if not set)
                    # 1 : make goal point (if not set)
                    # 2 : make treasure
                    # 3-9 : do nothing
                    if path_type == 0 and not self.start_point:
                        self.start_point = Start()
                        self.grid[col.x][col.y].contents.append(self.start_point)
                        print "\tStart point placed here!"
                    elif path_type == 1 and not self.goal_point:
                        self.goal_point = Goal()
                        self.grid[col.x][col.y].contents.append(self.goal_point)
                        print "\tGoal point placed here!"
                    elif path_type == 2:
                        self.grid[col.x][col.y].contents.append(Treasure())
                        print "\tTreasure placed here!"
                    else:
                        print "\t"

    def test_grid(self):
        '''Test to see if the grid is good for play'''
        pass
