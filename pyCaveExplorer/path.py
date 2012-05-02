'''
An empty path segment
'''

from element import GameElement

class Path(GameElement):
    def __init__(self, *args, **kwargs):
        super(Path, self).__init__(*args, **kwargs)
        self.contents = [] # tile's "inventory"
        self.light = 0 # how brightly lit the tile is (0 is unlit)
        self.passable = True # can the player be in this square?
    def show_items(self):
        # Something about adding contents to the doc?
        # TODO: I asked about the doc business, now I can finish coding here
        pass
