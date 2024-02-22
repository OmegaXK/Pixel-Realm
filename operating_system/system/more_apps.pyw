"""A window containing more apps."""

# A lot of this code is the same as in the main GUI file.

# Imports.
import os, sys, platform, subprocess, json
from pathlib import Path

import pygame
from pygame.locals import *

import assets

# Load in the preferences file.
path = Path('user_info/preferences.json')
preferences = json.loads(path.read_text())

# Window constants. (Same as main GUI)
WINDOWWIDTH = 540
WINDOWHEIGHT = 540
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2

# Other constants.
FPS = int(preferences["FPS"])

# App constants.
APPWIDTH = 100
APPHEIGHT = 100
GAPX = 160
GAPY = 160
STARTX = 108

# Colors.
GRAY = (160, 160, 160) # Light gray color.
RED = (255, 0, 0)
ORANGE = (255, 145, 0)
YELLOW = (247, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (154, 0, 255)


def main():
    """Main code for the More Apps window."""
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

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("More Apps")
    pygame.display.set_icon(images.pixel_realm_logo)

    # Load in the apps.
    # Entertainment apps.
    crack_chat = App('apps/entertainment/crack_chat.py', images.crack_chat_logo, STARTX, 70)
    crack_tube = App('apps/entertainment/crack_tube.pyw', images.crack_tube_logo, STARTX, 70 + GAPY)
    be_crack = App('apps/entertainment/be_crack.pyw', images.be_crack_logo, STARTX + GAPX, 70 + GAPY)
    mine_crack = App('apps/entertainment/mine_crack.pyw', images.mine_crack_logo, STARTX, 70 + GAPY * 2)

    # Useful apps.
    crack_ai = App('apps/useful_apps/crackai.pyw', images.crackai_logo, STARTX + GAPX, 70)
    crackazon = App('apps/useful_apps/crackazon.py', images.crackazon_logo, STARTX + GAPX * 2, 70)
    crackle_maps = App('apps/useful_apps/crackle_maps.pyw', images.crackle_maps_logo, STARTX + GAPX * 2, 70 + GAPY)
    crack_mail = App('apps/useful_apps/crack_mail.py', images.crack_mail_logo, STARTX + GAPX, 70 + GAPY * 2)

    # Other apps.
    free_robux = App('apps/free_robux/open.pyw', images.free_robux_logo, STARTX + GAPX * 2, 70 + GAPY * 2)
    
    # Create a list of all the apps.
    apps = [crack_chat, crack_ai, crackazon, crack_tube, be_crack, crackle_maps,
            mine_crack, crack_mail, free_robux]

    run_gui()


def run_gui():
    """Run the More Apps GUI."""

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
        DISPLAYSURF.fill(BGCOLOR)

        # Draw all of the apps.
        for app in apps:
            app.draw()

        # Draw some text at the bottom of the screen.
        draw_pr_text()

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

    def open(self):
        """Open the app."""

        # Open the app.
        start_file(self.path)


def draw_pr_text():
    """Draw the Copyright Pixel Realm text."""

    # Create the font.
    font = pygame.font.Font('freesansbold.ttf', 30)

    # Make the text and position it.
    textsurf = font.render('Copyright Pixel Realm 2024', True, BLACK)
    textrect = textsurf.get_rect()
    textrect.midbottom = (CENTERX, WINDOWHEIGHT - 15)

    # Draw the text on the screen.
    DISPLAYSURF.blit(textsurf, textrect)


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
    
    print("\nMore Apps - Close")
    pygame.quit()
    sys.exit()


# Run the program.
print("\nMore Apps - Open")
main()