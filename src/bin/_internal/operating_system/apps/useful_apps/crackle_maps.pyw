"""A ripoff of Apple Maps called Crackle Maps."""

# Imports.
import sys, os

import pygame 
from pygame.locals import *

# Set up the path.
resource_path = os.path.join(os.path.dirname(__file__), '')
rp = resource_path.replace('operating_system/apps/useful_apps', 'operating_system/')

# Constants.
WINDOWWIDTH = 800
WINDOWHEIGHT = 800


def main():
    """Main function for Crackle Maps."""
    global DISPLAYSURF, bg_img

    # Load in the background image.
    bg_img = pygame.image.load(f"{rp}apps/useful_apps/crack_map.png")
    bg_img = pygame.transform.scale(bg_img, (WINDOWWIDTH, WINDOWHEIGHT))

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Crackle Maps")
    pygame.display.set_icon(bg_img)

    # Run the main loop.
    run_map()


def run_map():
    """Run the Crackle Maps main loop."""

    while True:

        # Check for events.
        for event in pygame.event.get():

            # Check for quit.
            if event.type == QUIT:
                terminate()

            # Check if the player is pressing a key.
            if event.type == KEYDOWN:

                # Check for the escape key.
                if event.key == K_ESCAPE:
                    terminate()

        # Draw the screen.
        DISPLAYSURF.blit(bg_img, (0, 0))

        # Update the screen.
        pygame.display.update()


def terminate():
    """Quit the program."""

    pygame.quit()
    sys.exit()


# Run the main code.
main()