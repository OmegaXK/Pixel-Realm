"""This file resets Pixel Realm."""

# Imports.
import json, sys, os
from pathlib import Path

import pygame 
from pygame.locals import *

# Constants.
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2
FPS = 60

# Colors.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    """Main function for the reset wizard."""
    global DISPLAYSURF, BIGFONT, SMALLFONT

    # Initialize pygame.
    pygame.init()

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Reset Wizard")

    # Set up the fonts.
    BIGFONT = create_font(50)
    SMALLFONT = create_font(25)

    # Run the reset code.
    reset()


def reset():
    """Reset Pixel Realm."""

    pygame.event.get()

    DISPLAYSURF.fill(WHITE)
    draw_text("Reset Pixel Realm", BIGFONT, CENTERX, 40)
    pygame.display.update()
    pygame.time.wait(2000)

    draw_text("Resetting Account...", SMALLFONT, CENTERX, CENTERY)
    reset_account()
    pygame.display.update()
    pygame.time.wait(2000)


def reset_account():
    """Reset the user's current account."""

    # Load in the path.
    path = Path('user_info/user_info.json')

    # Check if the user doesn't have an account.
    if not path.exists():
        # The user doesn't have an account.
        return 
    
    # Delete the path if it does exist.
    os.remove(path)
    return


def draw_text(text, font, x, y):
    """Draw the text based on the given args."""

    textsurf = font.render(text, True, BLACK)
    textrect = textsurf.get_rect()
    textrect.center = (x, y)
    DISPLAYSURF.blit(textsurf, textrect)


def create_font(size):
    """Return a font of the given size."""
    
    return pygame.font.Font('freesansbold.ttf', size)


main()