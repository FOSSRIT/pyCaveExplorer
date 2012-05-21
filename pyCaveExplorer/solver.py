'''
Generates and solves the grid in pyCaveExplorer
'''

import random # perhaps be more specific? -- odd
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
            [Path(self, i, x) for x in range(GRID_HEIGHT)]
            for i in range(GRID_WIDTH)
        ]
        self.path_lengths = [] # stores lengths of working paths
        self.shortest_path = -1 # shortest working path from start to goal
        # self.game_grid = None

    def populate(self, pop_grid):
        needs_work = True
        while needs_work:
			# self.game_grid = pop_grid
			'''Populate the grid'''
			# TODO: X and Y coordinates for drawing are being done strangley.
			# Once we get to screen drawing, we'll have to figure that out.
			# I sort of half-assedly did it for now. Not sure if it'd work.
			self.start_point = None # start point has not been placed
			self.goal_point = None # end point has not been placed
			for row in pop_grid:
				for col in row:
					square_type = random.randint(0, 1)
					# 0 : make a wall.
					# 1 : make a path.
					if square_type == 0:
						pop_grid[col.x][col.y] = \
							Wall(col.x, col.y)
						print("Wall generated at {}, {}".format(col.x, col.y))
					elif square_type == 1:
						pop_grid[col.x][col.y] = \
							Path(self, col.x, col.y)
						print("Path generated at {}, {}".format(col.x, col.y)),
						path_type = random.randint(0, (TILE_TYPES - 1))
						# 0 : make starting point (if not set)
						# 1 : make goal point (if not set)
						# 2 : make treasure
						# 3-9 : do nothing
						pop_grid[col.x][col.y].contents = []
						if path_type == 0 and not self.start_point:
							self.start_point = Start(col.x, col.y)
							pop_grid[col.x][col.y].contents.append(self.start_point)
							print "\tStart point placed here!"
						elif path_type == 1 and not self.goal_point:
							self.goal_point = Goal(col.x, col.y)
							pop_grid[col.x][col.y].contents.append(self.goal_point)
							print "\tGoal point placed here!"
						elif path_type == 2:
							pop_grid[col.x][col.y].contents.append(Treasure(
								col.x, col.y))
							print "\tTreasure placed here!"
						else:
							print "\t"
			if self.start_point != None and self.goal_point != None:
				print 'Solver has start and goal, getting neighbors...' # DEBUG
				for row in pop_grid:
					for col in row:
						if pop_grid[col.x]\
						[col.y].group != ELEMENT_WALL:
							pop_grid[col.x]\
							[col.y].find_neighbors()
				print 'Tracing path...' # DEBUG
				if self.get_grid_path(pop_grid):
					needs_work = False
			else:
				print 'Missing start or goal, trying again...' # DEBUG

    def set_player_start(self):
        '''Drop player on the start location'''
        # could set player x/y here
        # we'll do this later, just so we do it right based on how
        # I've ported it -- odd
        pass

    def correct_display_order(self):
        '''Shift special objects to top of display list'''
        pass # nothing was in this function when I ported it -- odd

    def get_grid_path(self, pop_grid):
        '''Find a path to the goal to check if grid is solvable'''
        self.grid[self.start_point.x][self.start_point.y].grab_neighbors(
            self.grid[self.start_point.x][self.start_point.y], -1)
        # The above seems kinda janky. Man, I love that word. "Janky". -- odd
        if len(self.path_lengths) > 0:
            print 'Found paths, lengths:' # DEBUG
            for l in self.path_lengths:
                print l # DEBUG
            return True
        else:
            print 'No paths found, retrying'
            return False