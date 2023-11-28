"""The main file for the Pixel Realm OS GUI."""

import pygame, os, sys
from pygame.locals import *

from login import login, sign_up, main as login_main

# Window constants.
WINDOWWIDTH = 1920
WINDOWHEIGHT = 1080
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2

# Other constants.
FPS = 60

def main():
    """Main code for the OS GUI."""
    global MAINCLOCK, DISPLAYSURF

    # Initialize pygame and set up a clock.
    pygame.init()
    MAINCLOCK = pygame.time.Clock()

    # Load in the assets.
    load_assets()

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    # Run the OS GUI
    run_gui()


def run_gui():
    """Run the OS."""

    # Run the main loop.
    while True:
        # Check for events.
        for event in pygame.event.get():
            # Quit the program if the user closes the window.
            if event.type == QUIT:
                terminate()

            # Check if the user presses a key.
            if event.type == KEYDOWN:
                # Check if the user presses the escape key.
                if event.key == K_ESCAPE:
                    terminate()

        # Draw the desktop wallpaper.
        DISPLAYSURF.blit(desktop_wallpaper, (0, 0))

        # Update the display.
        pygame.display.update()
        MAINCLOCK.tick(FPS)


def load_assets():
    """Load the assets for the OS."""
    global desktop_wallpaper
    
    # Load in the desktop wallpaper.
    desktop_wallpaper = pygame.image.load('assets/images/desktop_wallpaper.png')
    desktop_wallpaper = pygame.transform.scale(desktop_wallpaper, 
                                               (WINDOWWIDTH, WINDOWHEIGHT))

    return


def terminate():
    """Quit the program."""
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    # If the user logs in succsesfully, the GUI opens.
    if login_main() == True:
        main()