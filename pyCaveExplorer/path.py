'''
An empty path segment
'''

from constants import *
from element import GameElement

'''
I think there may be a better way to check neighbors than having each Path
object store values for each of its neighbors. For now though, I have ported
your code with identical functionality. -- odd
'''

class Path(GameElement):
    def __init__(self, ps, *args, **kwargs):
        super(Path, self).__init__(*args, **kwargs)
        self.group = ELEMENT_PATH
        self.neighbors = {'n': None, 's': None, 'e': None, 'w': None}
        self.contents = [] # tile's "inventory"
        self.light = 0 # how brightly lit the tile is (0 is unlit)
        self.passable = True # can the player be in this square?
        # May reimplement functionality of the below variables... -- odd
        self.map_checked = False # has this path been map checked?
        self.parent_solver = ps

    def show_items(self):
        for item in self.contents:
            pass # PORT: game.doc.addChild(contents[i]);
    
    def find_neighbors(self):
        # West
        if self.x > 0:
            if self.parent_solver.grid[self.x-1][self.y].group == ELEMENT_WALL:
                self.neighbors['w'] = None
            else:
                self.neighbors['w'] = self.parent_solver.grid[self.x-1][self.y]
        
        # North
        if self.y > 0:
            if self.parent_solver.grid[self.x][self.y-1].group == ELEMENT_WALL:
                self.neighbors['n'] = None
            else:
                self.neighbors['n'] = self.parent_solver.grid[self.x][self.y-1]

        # East
        if (self.x + 1) < len(self.parent_solver.grid):
            if self.parent_solver.grid[self.x+1][self.y].group == ELEMENT_WALL:
                self.neighbors['e'] = None
            else:
                self.neighbors['e'] = self.parent_solver.grid[self.x+1][self.y]

        # South
        if (self.y + 1) < len(self.parent_solver.grid[self.x]):
            if self.parent_solver.grid[self.x][self.y+1].group == ELEMENT_WALL:
                self.neighbors['s'] = None
            else:
                self.neighbors['s'] = self.parent_solver.grid[self.x][self.y+1]

    def grab_neighbors(self, path, step=0):
        self.map_checked = True
        step += 1
        print 'grab_neighbors() step print:', step # DEBUG
        
        if self.contents[0].group == ELEMENT_GOAL:
            print 'Found goal at step', step
            self.parent_solver.path_lengths.append(step)
        for d in DIRECTIONS:
            if self.neighbors[d] != None and self.neighbors[d] != path \
                and self.neighbors[d].map_checked != False:
                self.neighbors[d].grab_neighbors(self, step)
