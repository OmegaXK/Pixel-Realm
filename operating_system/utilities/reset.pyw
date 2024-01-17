"""This file resets Pixel Realm."""

# Imports.
import sys, os
from pathlib import Path

import pygame 
from pygame.locals import *

# Constants.
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2
FPS = 60

# Colors.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    """Main function for the reset wizard."""
    global DISPLAYSURF, BIGFONT, SMALLFONT

    # Initialize pygame.
    pygame.init()

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Reset Wizard")

    # Set up the fonts.
    BIGFONT = create_font(50)
    SMALLFONT = create_font(25)

    # Run the reset code.
    reset()
    pygame.quit()
    sys.exit()


def reset():
    """Reset Pixel Realm."""

    # Let the user confirm that they want to reset Pixel Realm.
    confirmation()

    # Reset everything.
    DISPLAYSURF.fill(WHITE)
    draw_text("Reset Pixel Realm", BIGFONT, CENTERX, 50, BLACK)
    pygame.display.update()
    pygame.time.wait(1000)

    draw_text("Resetting Account...", SMALLFONT, CENTERX, CENTERY, BLACK)
    reset_account()
    pygame.display.update()
    pygame.time.wait(2000)

    DISPLAYSURF.fill(WHITE)
    draw_text("Reset Pixel Realm", BIGFONT, CENTERX, 50, BLACK)
    pygame.display.update()
    pygame.time.wait(1000)

    draw_text("Resetting Data...", SMALLFONT, CENTERX, CENTERY, BLACK)
    reset_data()
    pygame.display.update()
    pygame.time.wait(2000)

    DISPLAYSURF.fill(WHITE)
    draw_text("Reset Pixel Realm", BIGFONT, CENTERX, 50, BLACK)
    pygame.display.update()
    pygame.time.wait(1000)

    # Draw text indicating the reset is complete.
    draw_text("Reset Complete.", BIGFONT, CENTERX, CENTERY, BLACK)
    pygame.display.update()
    pygame.time.wait(2000)

    # Return and quit the program.
    return


def confirmation():
    """Confirm that the user actually wants to reset their account."""

    button = pygame.Rect(0, 0, 200, 100)
    button.center = (CENTERX, CENTERY)

    quit_button = pygame.Rect(0, 0, 200, 100)
    quit_button.center = (CENTERX, CENTERY + 150)

    font = create_font(32)
    button_font = create_font(40)

    while True:
        # Check for events.
        for event in pygame.event.get():

            # Check for quit.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Check if the user is pressing a key.
            if event.type == KEYDOWN:

                # Check for escape key.
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # Check if the user is clicking the mouse.
            if event.type == MOUSEBUTTONDOWN:

                # Check if the mouse is over the button.
                if button.collidepoint(event.pos):
                    return
                
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                    
        DISPLAYSURF.fill(WHITE)

        draw_text("Reset Pixel Realm", BIGFONT, CENTERX, 50, BLACK)
        draw_text("Click the Button to Confirm", font, CENTERX, 150, BLACK)

        pygame.draw.rect(DISPLAYSURF, BLACK, button)
        draw_text("Confirm", button_font, button.centerx, button.centery, WHITE)

        pygame.draw.rect(DISPLAYSURF, BLACK, quit_button)
        draw_text("Exit", button_font, quit_button.centerx, quit_button.centery, WHITE)

        pygame.display.update()


def reset_data():
    """Reset the user's data."""
    
    # Start with Cracky Bird.
    path = Path('games/graphic_games/cracky_bird/data/personal_best.txt')
    path.write_text("0")

    # Now do Crack Dash.
    path = Path('games/graphic_games/crack_dash/data/personal_best.txt')
    path.write_text("0")

    return
    

def reset_account():
    """Reset the user's current account."""

    # Load in the path.
    path = Path('user_info/user_info.json')

    # Check if the user doesn't have an account.
    if not path.exists():
        # The user doesn't have an account.
        return 
    
    # Delete the path if it does exist.
    os.remove(path)
    return


def draw_text(text, font, x, y, color):
    """Draw the text based on the given args."""

    textsurf = font.render(text, True, color)
    textrect = textsurf.get_rect()
    textrect.center = (x, y)
    DISPLAYSURF.blit(textsurf, textrect)


def create_font(size):
    """Return a font of the given size."""
    
    return pygame.font.Font('freesansbold.ttf', size)


main()