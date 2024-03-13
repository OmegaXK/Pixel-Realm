"""A joke app that tells you it's time for Crack."""

# Imports.
import sys, random, os

import pygame 
from pygame.locals import *

# Set up the path.
resource_path = os.path.join(os.path.dirname(__file__), '')
rp = resource_path.replace('operating_system/apps/entertainment', 'operating_system/')

# Constants.
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2

# Colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (180, 0, 0)
BLUE = (0, 0, 210)


def main():
    """Main function for Be-Crack."""
    global DISPLAYSURF

    # Initialize pygame.
    pygame.init()

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Be Crack")
    pygame.display.set_icon(pygame.image.load(f'{rp}apps/entertainment/be_crack_logo.png'))

    # Run the main loop.
    run_app()


def run_app():
    """Run the main Be-Crack loop."""

    time_frame = 0
    time = get_random_time()

    while True:

        # Check for events.
        for event in pygame.event.get():

            # Check for quit.
            if event.type == QUIT:
                terminate()

            # Check if the user is pressing a key.
            if event.type == KEYDOWN:

                # Check for ESCAPE key.
                if event.key == K_ESCAPE:
                    terminate()

        # Draw the screen.
        DISPLAYSURF.fill(RED)

        # Draw the title text.
        draw_text("It is Time for Crack", 80, BLUE, CENTERX, 140)

        # Check if it's time to update the time.
        if time_frame >= 3600:
            time = get_random_time()
            time_frame = 0
        else:
            time_frame += 1

        # Draw the time text.
        draw_text(f"Current Time:  {time}", 55, BLUE, CENTERX, 300)

        # Update the game.
        pygame.display.update()


def get_random_time():
    """Return a random time."""

    # Choose a random hour and minute.
    hour = str(random.randint(1, 12))
    minute = str(random.randint(1, 60))

    # Check to see if there needs to be a zero before the minute.
    if len(minute) == 1:
        minute = f"0{minute}"

    # Choose PM or AM.
    if random.randint(1, 2) == 1:
        day = "PM"
    else:
        day = "AM"

    return f'{hour} : {minute} {day}'


def draw_text(text, size, color, x, y):
    """Draw text based on the given parameters."""

    font = pygame.font.Font("freesansbold.ttf", size)
    textsurf = font.render(text, True, color)
    textrect = textsurf.get_rect()
    textrect.center = (x, y)
    DISPLAYSURF.blit(textsurf, textrect)


def terminate():
    """Quit the program."""

    pygame.quit()
    sys.exit()


# Run the main code.
main()