"""Main code for Crack Dash."""

# Path: games/graphic_games/crack_dash

# Imports.
import sys, random, json 
from pathlib import Path

import pygame
from pygame.locals import *

# Load in the preferences file.
path = Path('preferences.json')
preferences = json.loads(path.read_text())

# Window constants.
WINDOWWIDTH = 600
WINDOWHEIGHT = 450
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2

# General constants.
FPS = int(preferences["FPS"])


def main():
    """Main code for Crack Dash."""
    global DISPLAYSURF, MAINCLOCK, images, sounds

    # Initialize pygame and set up a clock.
    pygame.init()
    MAINCLOCK = pygame.time.Clock()

    # Load in the images and sounds.

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Crack Dash")

    # Run the game.
    run_game()


def run_game():
    """Run the main game."""

    # Main loop.
    while True:

        # Check for events.
        for event in pygame.event.get():

            # Check for quit.
            if event.type == QUIT:
                terminate()

            # Check if the player is pressing a key.
            if event.type == K_DOWN:

                # Check for the ESCAPE key.
                if event.key == K_ESCAPE:
                    terminate()


def terminate():
    """Quit out of the game."""

    pygame.quit()
    sys.exit()


main()