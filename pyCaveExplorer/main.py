"""
Main file for pyCaveExplorer
"""

import pygame
import sys


def main():
    """ This is the main entry point for the game.

    You can find a reference to it in setup.py under the console-scripts
    entry-point.  This is the function that gets run when you type::

        $ explore-the-cave

    Awesome!
    """

    ### CONSTANTS ###
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREY = 125, 125, 125
    GOLD = 255, 204, 0

    ### INITIALIZE ###
    pygame.init()

    ### WINDOW FRAME ###
    screen = pygame.display.set_mode((640, 480))  # resolution tenative
    pygame.display.set_caption("pyCaveExplorer")

    ### GAME LOOP ###
    clock = pygame.time.Clock()  # framerate control for animation
    while True:
        clock.tick(50)

        # Event processing
        for event in pygame.event.get():
            # Quitting?
            if event.type == pygame.QUIT:
                sys.exit()

        # Get a brown background
        screen.fill(GREY)

        # Add a silly title-thing, just to do something

        title_font = pygame.font.SysFont("sans-serif", 48)
        title_text = title_font.render("pyCaveExplorer", True, BLACK, GOLD)
        screen.blit(title_text, (200, 200))

        # Update the screen
        pygame.display.flip()

# Start the game
main()  # this may be done in a different way in the future
