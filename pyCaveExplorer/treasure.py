'''
Treasure object for pyCaveExplorer
    * randomly dropped in available path squares
    * give player shiny trinkets or spare lights/batteries
'''

from element import GameElement

class Treasure(GameElement):
    def __init__(self, *args, **kwargs):
        super(Treasure, self).__init__(*args, **kwargs)
        pass
