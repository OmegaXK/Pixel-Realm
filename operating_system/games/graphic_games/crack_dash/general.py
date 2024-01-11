"""The general functions and classes for Crack Dash."""

import sys 

import pygame
from pygame.locals import *

# Constants.
PATH = "games/graphic_games/crack_dash"
CUBEWIDTH = 65
CUBEHEIGHT = CUBEWIDTH


# Functions.
def terminate():
    """Quit out of the game."""

    pygame.quit()
    sys.exit()


# Classes.
class Images:
    """Load in the images for the file as attributes."""

    def __init__(self):
        """Initialize the images."""

        self.bg_img = pygame.image.load(f"{PATH}/images/background.png")
        # The background was custom made to be the right size to start.

        self.cube_img = pygame.image.load(f"{PATH}/images/cube.png")
        self.cube_img = pygame.transform.scale(self.cube_img, (CUBEWIDTH, CUBEHEIGHT))