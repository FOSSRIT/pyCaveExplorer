'''
Wall object for pyCaveExplorer
    * Blocks the player's path
'''

from element import GameElement

class Wall(GameElement):
    def __init__(self, *args, **kwargs):
        super(Wall, self).__init__(*args, **kwargs)
        pass
