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
from pygame.locals import *
from game import *

# Initialize pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("pyCaveExplorer")

# Set up clock so we can have animations later
clock = pygame.time.Clock()

quitting = False # is the game closing?

game = None # the current game

def display_menu():
    screen.fill(COLOR_GREY)
    title_font = pygame.font.SysFont("sans-serif", 48)
    title_text = title_font.render("pyCaveExplorer", True,
        COLOR_BLACK, COLOR_GOLD)
    screen.blit(title_text, (200, 200))

def render_game():
    game.draw(screen)

def main():
    """ This is the main entry point for the game.

    You can find a reference to it in setup.py under the console-scripts
    entry-point.  This is the function that gets run when you type::

        $ explore-the-cave

    Awesome!
    """
    
    global quitting
    global game

    #######################
    ### START GAME LOOP ###  # Can't handle my ridiciulous comment blocks?
    #######################  # THEN GET OUT OF THE KITCHEN

    while not quitting:
        clock.tick(30) # Set FPS to 30

        ### Event handling ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
            elif event.type == KEYDOWN:
                if event.key == K_RETURN: # RETURN -- Start game
                    game = Game()
                elif event.key == K_ESCAPE: # ESCAPE -- Quit
                    quitting = True

        # Draw the screen
        if game == None:
            display_menu()
        else:
            render_game()

        # Update the screen
        pygame.display.flip()

    #######################
    #### END GAME LOOP ####
    #######################

    pygame.quit() # quit the game

# Start the game
if __name__ == '__main__':
    main()
