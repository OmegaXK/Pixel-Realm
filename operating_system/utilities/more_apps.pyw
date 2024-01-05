"""A window containing more apps."""

# A lot of this code is the same as in the main GUI file.

import os, sys, platform, subprocess, json
from pathlib import Path

import pygame
from pygame.locals import *

# Load in the preferences file.
path = Path('preferences.json')
preferences = json.loads(path.read_text())

# Window constants. (Same as main GUI)
WINDOWWIDTH = 960
WINDOWHEIGHT = 540
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2

# Other constants.
FPS = int(preferences["FPS"])
APPWIDTH = 100
APPHEIGHT = 100


def main():
    """Main code for the More Apps window."""
    global MAINCLOCK, DISPLAYSURF, images, sounds

    # Initialize pygame and set up a clock.
    pygame.init()
    MAINCLOCK = pygame.time.Clock()

    # Load in the assets.
    images = Images()
    sounds = Sounds()

    # Options.
    if preferences['audio'].lower() == "true":
        disable_sound = False
    else:
        disable_sound = True

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Pixel Realm")
    pygame.display.set_icon(images.pixel_realm_logo)


class App():
    """Represent the apps on the desktop."""

    def __init__(self, path, logo, x, y):
        """Initialize the apps."""
            
        self.path = path
        self.logo = logo
        self.x = x
        self.y = y

        self.rect = pygame.Rect(0, 0, APPWIDTH, APPHEIGHT)
        self.rect.center = (self.x, self.y)

    def draw(self):
        """Draw the app on the screen."""

        DISPLAYSURF.blit(self.logo, self.rect)

    def check_click(self, mouse_pos):
        """Check if the user clicks the app."""

        if self.rect.collidepoint(mouse_pos):
            self.open()

    def open(self):
        """Open the app."""

        # Open the app.
        start_file(self.path)


class Images:
    """The images needed for the More Apps page."""

    def __init__(self):
        """Initialize the images."""
        pass 


class Sounds:
    """The sounds needed for the More Apps page."""

    def __init__(self):
        """Initialize the sounds."""
        pass 


def start_file(filepath):
    """Start the file passed, regardless of your current platform."""

    if platform.system() == 'Darwin':       # macOS
        subprocess.run(('python3', filepath))
    elif platform.system() == 'Windows':    # Windows
        cwd = os.getcwd()
        file_path = os.path.join(cwd, filepath)
        os.startfile(file_path)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))


def terminate():
    """Quit the program."""
    pygame.quit()
    sys.exit()


# Run the program.
main()