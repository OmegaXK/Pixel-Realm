"""The main file for the Pixel Realm OS GUI."""

import os, sys, platform, subprocess

import pygame
from pygame.locals import *

from login import main as login_main

# Window constants.
WINDOWWIDTH = 960
WINDOWHEIGHT = 540
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2

# Other constants.
FPS = 60
APPWIDTH = 100
APPHEIGHT = 100


def main():
    """Main code for the OS GUI."""
    global MAINCLOCK, DISPLAYSURF, assets, apps

    # Initialize pygame and set up a clock.
    pygame.init()
    MAINCLOCK = pygame.time.Clock()

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Pixel Realm")

    # Load in the assets.
    assets = Assets()

    # Load in the apps.
    browser = App('apps/browser.pyw', assets.browser_logo, 90, 450)
    notepad = App('apps/notepad.pyw', assets.notepad_logo, 210, 450)
    explorer = App('apps/explorer.pyw', assets.explorer_logo, 330, 450)

    # Create a list of all the apps.
    apps = [browser, notepad, explorer]

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

            # Check if the user clicks the mouse.
            if event.type == MOUSEBUTTONDOWN:
                # Check if the user click an app.
                for app in apps:
                    app.check_click(event.pos)

        # Draw the desktop wallpaper.
        DISPLAYSURF.blit(assets.desktop_wallpaper, (0, 0))

        # Draw all of the apps.
        for app in apps:
            app.draw()

        # Update the display.
        pygame.display.update()
        MAINCLOCK.tick(FPS)


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


class Assets():
    """A class to represent the assets."""

    def __init__(self):
        """Initialize the assets."""

        self.desktop_wallpaper = pygame.image.load("assets/images/desktop_wallpaper.png")
        self.desktop_wallpaper = pygame.transform.scale(self.desktop_wallpaper, 
                                                        (WINDOWWIDTH, WINDOWHEIGHT))

        self.browser_logo = pygame.image.load('assets/images/browser_logo.png')
        self.browser_logo = pygame.transform.scale(self.browser_logo, 
                                                   (APPWIDTH, APPHEIGHT))

        self.notepad_logo = pygame.image.load('assets/images/notepad_logo.png')
        self.notepad_logo = pygame.transform.scale(self.notepad_logo, 
                                                   (APPWIDTH, APPHEIGHT))
        
        self.explorer_logo = pygame.image.load('assets/images/file_explorer_logo.png')
        self.explorer_logo = pygame.transform.scale(self.explorer_logo, 
                                                    (APPWIDTH, APPHEIGHT))

def start_file(filepath):
    """Start the file passed, regardless of your current platform."""

    if platform.system() == 'Darwin':       # macOS
        subprocess.run(('python3', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))


def terminate():
    """Quit the program."""
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    # If the user logs in succsesfully, the GUI opens.
    if login_main() == True:
        main()