'''
Holds constants for pyCaveExplorer
'''

# As a great person once said, only you can prevent hard coding of values

TILESIZE_X = 40 # Width of tiles
TILESIZE_Y = 40 # Height of tiles

GRID_WIDTH = 11 # Tiles fitting horizontally
GRID_HEIGHT = 8 # Tiles fitting vertically

TILE_TYPES = 10 # Weight for grid population
CONTENTS_TYPES = 13 # Weight for item population

MINIMUM_MOVES = 3 # Number of moves the goal must be from the start point

# Colors
COLOR_BLACK = 0, 0, 0
COLOR_BLUE = 0, 0, 255
COLOR_BROWN = 156, 102, 31
COLOR_GOLD = 255, 204, 0
COLOR_GREEN = 0, 128, 0
COLOR_GREY = 125, 125, 125
COLOR_RED = 176, 23, 31
COLOR_WHITE = 255, 255, 255

# Colors (dark)
COLOR_DARK_GREY = 75, 75, 75

# Colors (light)
COLOR_LIGHT_BROWN = 244, 164, 96

# Interface
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GAME_WINDOW_ORIGIN_X = 25
GAME_WINDOW_ORIGIN_Y = 25
GAME_WINDOW_WIDTH = TILESIZE_X * GRID_WIDTH
GAME_WINDOW_HEIGHT = TILESIZE_Y * GRID_HEIGHT

# Elements
ELEMENT_PATH = "path"
ELEMENT_WALL = "wall"
ELEMENT_START = "start"
ELEMENT_GOAL = "goal"
ELEMENT_TREASURE = "treasure"
