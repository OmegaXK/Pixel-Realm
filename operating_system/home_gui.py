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

    # Load in the assets.
    assets = Assets()

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Pixel Realm")
    pygame.display.set_icon(assets.pixel_realm_logo)

    # Load in the apps.
    browser = App('apps/browser.pyw', assets.browser_logo, 90, 450)
    notepad = App('apps/notepad.pyw', assets.notepad_logo, 210, 450)
    explorer = App('apps/explorer.pyw', assets.explorer_logo, 330, 450)
    settings = App('settings.py', assets.settings_logo, 450, 450)

    # Game apps.
    rps = App('games/cli_games/rock-paper-scissors.py', 
              assets.rps_logo, 570, 450)
    ttt = App('games/cli_games/tic-tac-toe.py', assets.ttt_logo, 690, 450)

    # Create a list of all the apps.
    apps = [browser, notepad, explorer, settings, rps, ttt]

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
        
        self.settings_logo = pygame.image.load('assets/images/settings_logo.png')
        self.settings_logo = pygame.transform.scale(self.settings_logo,
                                                    (APPWIDTH, APPHEIGHT))
        
        self.pixel_realm_logo = pygame.image.load('assets/images/pixel_realm_logo.png')
        self.pixel_realm_logo = pygame.transform.scale(self.pixel_realm_logo,
                                                       (32, 32))
        
        self.rps_logo = pygame.image.load('assets/images/rps_logo.png')
        self.rps_logo = pygame.transform.scale(self.rps_logo,
                                               (APPWIDTH, APPHEIGHT))
        
        self.ttt_logo = pygame.image.load('assets/images/ttt_logo.png')
        self.ttt_logo = pygame.transform.scale(self.ttt_logo,
                                               (APPWIDTH, APPHEIGHT))
        
        self.cracky_bird_logo = pygame.image.load('assets/images/cracky_bird_logo.png')
        self.cracky_bird_logo = pygame.transform.scale(self.cracky_bird_logo,
                                                       (APPWIDTH, APPHEIGHT))
        

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


if __name__ == "__main__":
    # If the user logs in succsesfully, the GUI opens.
    if login_main() == True:
        main()