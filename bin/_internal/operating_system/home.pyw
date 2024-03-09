"""The main file for the Pixel Realm OS GUI."""

# Imports.
import os, sys, platform, subprocess, json
from pathlib import Path

import pygame
from pygame.locals import *

from system.login import main as login_main
import system.assets as assets

# Path garbage.
resource_path = os.path.join(os.path.dirname(__file__), '')
path = Path(f'{resource_path}/information/path.txt')
path.write_text(resource_path)

# Load in the preferences file.
path = Path(f'{resource_path}/user_info/preferences.json')
preferences = json.loads(path.read_text())

# Window constants.
WINDOWWIDTH = 960 
WINDOWHEIGHT = 540
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2

# Colors.
BLACK = (0, 0, 0)
GRAY = (120, 120, 120)

# Other constants.
FPS = int(preferences["FPS"])
APPWIDTH = 100
APPHEIGHT = 100


def open_home():
    """Open the home page."""

    # If the user logs in succsesfully, the GUI opens.
    if login_main() == True:
        print("\nPixel Realm - Open")
        main()


def main():
    """Main code for the OS GUI."""
    global MAINCLOCK, DISPLAYSURF, images, sounds, apps, disable_sound

    # Initialize pygame and set up a clock.
    pygame.init()
    MAINCLOCK = pygame.time.Clock()

    # Load in the assets.
    images = assets.Images()
    sounds = assets.Sounds()

    # Options.
    if preferences['audio'].lower() == "true":
        disable_sound = False
    else:
        disable_sound = True

    if preferences['Background Music'].lower() == "true":
        bg_music = True
    else:
        bg_music = False

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Pixel Realm")
    pygame.display.set_icon(images.pixel_realm_logo)

    # Load in the apps.
    # Basic OS apps.
    browser = App(f'{resource_path}/apps/system_apps/browser.pyw', images.browser_logo, 90, 450)
    notepad = App(f'{resource_path}/apps/system_apps/notepad.pyw', images.notepad_logo, 210, 450)
    explorer = App(f'{resource_path}/apps/system_apps/explorer.pyw', images.explorer_logo, 330, 450)
    settings = App(f'{resource_path}/system/settings.py', images.settings_logo, 450, 450)
    reset = App(f'{resource_path}/utilities/reset.pyw', images.reset_logo, 570, 450)
    more_apps = App(f'{resource_path}/system/more_apps.pyw', images.more_apps_logo, 690, 450)

    # Game apps.
    rps = App(f'{resource_path}/games/cli_games/rock-paper-scissors.py', 
              images.rps_logo, 690, 60)
    ttt = App(f'{resource_path}/games/cli_games/tic-tac-toe.py', images.ttt_logo, 690, 185)
    cracky_bird = App(f'{resource_path}games/graphic_games/cracky_bird/main.pyw', 
                      images.cracky_bird_logo, 690, 310)
    enter = App(f'{resource_path}/games/cli_games/enter_bar_clicker.py', images.enter_logo, 810, 185)
    hangman = App(f'{resource_path}/games/cli_games/hangman.py', images.hangman_logo, 810, 60)
    crack_dash = App(f'{resource_path}/games/graphic_games/crack_dash/main.pyw', 
                     images.crack_dash_logo, 810, 310)

    # Create a list of all the apps.
    apps = [browser, notepad, explorer, settings, rps, ttt, cracky_bird,
            enter, hangman, more_apps, crack_dash, reset]

    # Play the startup sound.
    if not disable_sound:
        sounds.startup.play()

    # Start the music.
    pygame.mixer.music.load(f'{resource_path}/assets/sounds/background_music.mp3')

    if bg_music:
        pygame.mixer.music.play(-1, 0.0)

    # Run the OS GUI.
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
        if preferences['PR Background'].lower() == "true":
            DISPLAYSURF.blit(images.desktop_wallpaper, (0, 0))
        else:
            DISPLAYSURF.fill(GRAY)
            draw_pr_text()

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
            if not disable_sound:
                sounds.open_app.play()

            self.open()
            
            if 'reset.pyw' in self.path:
                # Quit after running reset.
                terminate()

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


def draw_pr_text():
    """Draw some basic text saying Pixel Realm."""

    font = pygame.font.Font('freesansbold.ttf', 80)
    textsurf = font.render("Pixel  Realm", True, BLACK)
    textrect = textsurf.get_rect()
    textrect.topleft = 65, 50
    DISPLAYSURF.blit(textsurf, textrect)


def terminate():
    """Quit the program."""
    pygame.quit()

    print('\nPixel Realm - Terminate')
    sys.exit()


if __name__ == "__main__":
    open_home()