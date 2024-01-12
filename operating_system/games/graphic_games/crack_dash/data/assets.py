"""The general functions and classes for Crack Dash."""

import sys 

import pygame
from pygame.locals import *

# Constants.
PATH = "games/graphic_games/crack_dash/"
CUBEWIDTH = 65
CUBEHEIGHT = CUBEWIDTH


# Functions.
def terminate():
    """Quit out of the game."""

    pygame.quit()
    sys.exit()


def create_font(size):
    """Return a font with the correct size."""
    return pygame.font.Font('freesansbold.ttf', size)


# Classes.
class Images:
    """Load in the images for the file as attributes."""

    def __init__(self):
        """Initialize the images."""

        self.bg_img = pygame.image.load(f"{PATH}/images/background.png")
        # The background was custom made to be the right size to start.

        # Load in the cube.
        self.cube_img = pygame.image.load(f"{PATH}/images/cube.png")
        self.cube_img = pygame.transform.scale(self.cube_img, (CUBEWIDTH, CUBEHEIGHT))

        # Load in the spikes.
        self.spike_img = pygame.image.load(f"{PATH}/images/spike.png")
        self.spike_img = pygame.transform.scale(self.spike_img, (40, 40))

        self.double_spike_img = pygame.image.load(f"{PATH}/images/double_spike.png")
        self.double_spike_img = pygame.transform.scale(self.double_spike_img, (80, 70))