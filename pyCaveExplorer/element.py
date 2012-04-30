'''
A game element in pyCaveExplorer
Anything that is placed on the grid MUST extend this class!
'''

class GameElement:
    def __init__(self, gridX=0, gridY=0):
        self.gridX = gridX # x position on grid
        self.gridY = gridY # y position on grid
