"""This file resets Pixel Realm."""

# Imports.
import json 
from pathlib import Path

import pygame 
from pygame.locals import *

# Constants.
WINDOWWIDTH = 300
WINDOWHEIGHT = 300
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2
FPS = 60

# Colors.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    """Main function for the reset wizard."""
    global DISPLAYSURF, MAINCLOCK, BIGFONT, SMALLFONT

    # Initialize pygame and set up a clock.
    pygame.init()
    MAINCLOCK = pygame.time.Clock()

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Reset Wizard")

    # Set up the fonts.
    BIGFONT = create_font(100)
    SMALLFONT = create_font(40)

    # Run the reset code.
    reset()


def reset():
    """Reset Pixel Realm."""

    DISPLAYSURF.fill(WHITE)
    draw_text("Reset Pixel Realm", BIGFONT, CENTERX, 40)

    pygame.display.update()
    pygame.time.wait(1000)


def draw_text(text, font, x, y):
    """Draw the text based on the given args."""

    textsurf = font.render(text, True, BLACK)
    textrect = textsurf.get_rect()
    textrect.center = (x, y)
    DISPLAYSURF.blit(textsurf, textrect)


def create_font(size):
    """Return a font of the given size."""
    
    return pygame.font.Font('freesansbold.ttf')


main()