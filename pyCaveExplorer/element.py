'''
A game element in pyCaveExplorer
Anything that is placed on the grid MUST extend this class!
'''

class GameElement(object):
    def __init__(self, x=0, y=0):
        # The x and y variables may not be needed...
        # Coordinates could be determined more elegantly another way
        self.x = x # x position on grid
        self.y = y # y position on grid
