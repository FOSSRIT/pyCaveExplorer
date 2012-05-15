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
    def __init__(self, *args, **kwargs):
        super(Path, self).__init__(*args, **kwargs)
        self.group = ELEMENT_PATH
        self.neighbors = {'n': None, 's': None, 'e': None, 'w': None}
        self.contents = [] # tile's "inventory"
        self.light = 0 # how brightly lit the tile is (0 is unlit)
        self.passable = True # can the player be in this square?
        # May reimplement functionality of the below variable... -- odd
        self.map_checked = False # has this path been map checked?
    
    def show_items(self):
        for item in self.contents:
            pass # PORT: game.doc.addChild(contents[i]);
    
    def find_neighbors(self):
        # West
        if self.x > 0 and game.solver.grid[x-1][y].group == ELEMENT_WALL:
            self.neighbors['w'] = None
        else:
            self.neighbors['w'] = game.solver.grid[x-1][y]
        
        # North
        if self.y > 0 and game.solver.grid[x][y-1].group == ELEMENT_WALL:
            self.neighbors['n'] = None
        else:
            self.neighbors['n'] = game.solver.grid[x][y-1]

        # East
        if (self.x + 1) < len(game.solver.grid) \
            and game.solver.grid[x+1][y].group == ELEMENT_WALL:
            self.neighbors['e'] = None
        else:
            self.neighbors['e'] = game.solver.grid[x+1][y]

        # South
        if (self.y + 1) < len(game.solver.grid[x]) \
            and game.solver.grid[x][y+1].group == ELEMENT_WALL:
            self.neighbors['s'] = None
        else:
            self.neighbors['s'] = game.solver.grid[x][y+1]


        
