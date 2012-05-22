'''
The player object for pyCaveExplorer
'''

class Player(GameElement):
    def __init__(self):
        self.inventory = [] # the player's inventory
        # TODO: Discuss use of inventory data structure
        #   instead of count variables
