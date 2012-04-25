'''
A game element in pyCaveExplorer
Anything that is placed on the grid MUST extend this class!
'''

class GameElement:
    def __init__(self):
        self.gridX = 0 # x position on grid
        self.gridY = 0 # y position on grid
