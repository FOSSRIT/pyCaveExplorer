'''
Defines UI stuff for pyCaveExplorer
If this stuff should go elsewhere, please move it. :)
'''

import pygame

class Button:
    '''
    Button class that runs a command at mousedown.
    Not implemented yet, just an idea.
    '''

    def __init__(self, x, y, w, h, command):
        self.rect = Rect(x, y, w, h)
        self.command = command

    def handle_mouse_down(self, x, y):
        if self.rect.collidepoint(x, y):
            if self.command != None:
            self.command.do()

    def draw(self, surface):
        pygame.draw.rect(surface, COLOR_GREY, self.rect)
