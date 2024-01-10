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
PATH = "games/graphic_games/crack_dash"

# Check if audio is on or off.
if preferences["audio"].lower() == "false":
    AUDIO = False 
else:
    AUDIO = True


def main():
    """Main code for Crack Dash."""
    global DISPLAYSURF, MAINCLOCK, images, sounds

    # Initialize pygame and set up a clock.
    pygame.init()
    MAINCLOCK = pygame.time.Clock()

    # Load in the images and sounds.
    images = Images()

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
            if event.type == KEYDOWN:

                # Check for the ESCAPE key.
                if event.key == K_ESCAPE:
                    terminate()

        # Draw the game on the screen.
        DISPLAYSURF.blit(images.bg_img, (0, 0))

        # Update the game.
        pygame.display.update()
        MAINCLOCK.tick(FPS)


def terminate():
    """Quit out of the game."""

    pygame.quit()
    sys.exit()


class Images:
    """Load in the images for the file as attributes."""

    def __init__(self):
        """Initialize the images."""

        self.bg_img = pygame.image.load(f"{PATH}/images/background.png")


main()