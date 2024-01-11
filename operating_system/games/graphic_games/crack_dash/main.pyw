"""Main code for Crack Dash."""

# Path: games/graphic_games/crack_dash

# Imports.
import random, json 
from pathlib import Path

import pygame
from pygame.locals import *

import general

# Load in the preferences file.
path = Path('preferences.json')
preferences = json.loads(path.read_text())

# Window constants.
WINDOWWIDTH = 600
WINDOWHEIGHT = 450
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2
GROUNDHEIGHT = 121

# Cube constants.
JUMPHEIGHT = 14

# General constants.
FPS = int(preferences["FPS"])
GRAVITY = -1

# Check if audio is on or off.
if preferences["audio"].lower() == "false":
    AUDIO = False 
else:
    AUDIO = True


def main():
    """Main code for Crack Dash."""
    global DISPLAYSURF, MAINCLOCK, images, sounds

    # Initialize pygame and set up a clock.
    pygame.init()
    MAINCLOCK = pygame.time.Clock()

    # Load in the images and sounds.
    images = general.Images()

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Crack Dash")

    # Run the game.
    run_game()


def run_game():
    """Run the main game."""
    global cube_rect, fallspeed

    # Define the game variables.
    score = 0
    cube_rect = images.cube_img.get_rect()
    fallspeed = 0

    # Set up the player.
    cube_rect.centerx = CENTERX 
    cube_rect.bottom = WINDOWHEIGHT - GROUNDHEIGHT

    # Main loop.
    while True:

        # Check for events.
        for event in pygame.event.get():

            # Check for quit.
            if event.type == QUIT:
                general.terminate()

            # Check if the player is pressing a key.
            if event.type == KEYDOWN:

                # Check for the ESCAPE key.
                if event.key == K_ESCAPE:
                    general.terminate()

                # Check if the player is pressing a jump key.
                if event.key == K_UP or event.key == K_w:
                    cube_jump()
                
                if event.key == K_SPACE or event.key == K_RSHIFT:
                    cube_jump()

            if event.type == MOUSEBUTTONDOWN:
                cube_jump()

        # Draw the game on the screen.
        DISPLAYSURF.blit(images.bg_img, (0, 0))

        # Update the cube.
        gravity()

        # Draw the cube.
        DISPLAYSURF.blit(images.cube_img, cube_rect)

        # Update the game.
        pygame.display.update()
        MAINCLOCK.tick(FPS)


def gravity():
    """Simulate gravity."""
    global fallspeed

    cube_rect.y += fallspeed

    if cube_rect.bottom >= WINDOWHEIGHT - GROUNDHEIGHT:

        # Push the cube out of the ground.
        while cube_rect.bottom >= WINDOWHEIGHT - GROUNDHEIGHT:
            cube_rect.y -= 1
        
    else:
        # The cube falls.
        fallspeed -= GRAVITY


def cube_jump():
    """Make the cube jump."""
    global fallspeed 
    
    if cube_rect.y > 250:
        fallspeed = -JUMPHEIGHT


main()