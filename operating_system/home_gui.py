"""The main file for the Pixel Realm OS GUI."""

import os, sys, platform, subprocess, json
from pathlib import Path

import pygame
from pygame.locals import *

from utilities.login import main as login_main
import utilities.loading as loading

# Load in the preferences file.
path = Path('preferences.json')
preferences = json.loads(path.read_text())

# Window constants.
WINDOWWIDTH = 960
WINDOWHEIGHT = 540
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2

# Other constants.
FPS = int(preferences["FPS"])


def main():
    """Main code for the OS GUI."""
    global MAINCLOCK, DISPLAYSURF, images, sounds, apps

    # Initialize pygame and set up a clock.
    pygame.init()
    MAINCLOCK = pygame.time.Clock()

    # Load in the assets.
    images = loading.Images()
    sounds = loading.Sounds()

    # Options.
    if preferences['audio'].lower() == "true":
        disable_sound = False
    else:
        disable_sound = True

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Pixel Realm")
    pygame.display.set_icon(images.pixel_realm_logo)

    # Load in the apps.
    # Basic OS apps.
    browser = App('apps/browser.pyw', images.browser_logo, 90, 450)
    notepad = App('apps/notepad.pyw', images.notepad_logo, 210, 450)
    explorer = App('apps/explorer.pyw', images.explorer_logo, 330, 450)
    settings = App('utilities/settings.py', images.settings_logo, 450, 450)

    # Game apps.
    rps = App('games/cli_games/rock-paper-scissors.py', 
              images.rps_logo, 570, 450)
    ttt = App('games/cli_games/tic-tac-toe.py', images.ttt_logo, 690, 450)
    cracky_bird = App('games/graphic_games/cracky_bird/main.pyw', 
                      images.cracky_bird_logo, 690, 60)
    enter = App('games/cli_games/enter_bar_clicker.py', images.enter_logo, 810, 60)
    hangman = App('games/cli_games/hangman.py', images.hangman_logo, 810, 185)

    # Entertainment apps.
    crack_tube = App('apps/crack_tube.pyw', images.crack_tube_logo, 690, 185)
    crack_chat = App('apps/crack_chat.py', images.crack_chat_logo, 570, 330)

    # Useful apps.
    crackai = App('apps/crackai.pyw', images.crackai_logo, 690, 310)
    crackazon = App('apps/crackazon.py', images.crackazon_logo, 810, 310)
    more_apps = App('utilities/more_apps.pyw', images.more_apps_logo, 570, 60)

    # Create a list of all the apps.
    apps = [browser, notepad, explorer, settings, rps, ttt, cracky_bird,
            enter, crack_tube, hangman, crackai, crackazon, crack_chat, 
            more_apps]

    # Run the OS GUI, and the play the startup sound.
    if not disable_sound:
        sounds.startup.play()

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
        DISPLAYSURF.blit(images.desktop_wallpaper, (0, 0))

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

    print('\nTerminate')
    sys.exit()


if __name__ == "__main__":
    # If the user logs in succsesfully, the GUI opens.
    if login_main() == True:
        main()