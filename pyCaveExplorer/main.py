"""
Main file for pyCaveExplorer.

Just a note -- you can run the script this way, by running

  $ python main.py

Or you can use the console_script entry-point defined in setup.py
and just the following instead

  $ explore-the-cave

"""

import sys
import pygame
from constants import *

def main():
    """ This is the main entry point for the game.

    You can find a reference to it in setup.py under the console-scripts
    entry-point.  This is the function that gets run when you type::

        $ explore-the-cave

    Awesome!
    """

    # Initialize pygame
    pygame.init()

    # Set up the window
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("pyCaveExplorer")

    # Set up clock so we can have animations later
    clock = pygame.time.Clock()

    #######################
    ### START GAME LOOP ###  # Can't handle my ridiciulous comment blocks?
    #######################  # THEN GO HOME

    while True:
        clock.tick(30) # Set FPS to 30

        ### Event handling ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() # Quit the game

        # Get a grey background
        screen.fill(COLOR_GREY)

        # Add a silly title-thing, just to do something
        title_font = pygame.font.SysFont("sans-serif", 48)
        title_text = title_font.render("pyCaveExplorer", True,
            COLOR_BLACK, COLOR_GOLD)
        screen.blit(title_text, (200, 200))

        # Update the screen
        pygame.display.flip()

    #######################
    #### END GAME LOOP ####
    #######################

# Start the game
if __name__ == '__main__':
    main()
