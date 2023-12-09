"""The Crack-OS version of the game Flappy Bird - Cracky Bird."""

# Imports.
import sys, random

import pygame
from pygame.locals import *

# Define window constants.
WINDOWWIDTH = 288
WINDOWHEIGHT = 512
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2

# Pipe constants.
PIPESPAWNRATE = 120
PIPESPEED = 2

# Define other constants.
FPS = 60
JUMPHEIGHT = 5

# Define colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():
    """Main code for cracky-bird."""
    global MAINCLOCK, DISPLAYSURF, assets

    # Initialize pygame and set up a clock.
    pygame.init()
    MAINCLOCK = pygame.time.Clock()

    # Load in the assets.
    assets = Assets()
    
    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Cracky Bird")
    
    # Run the game.
    run_game()


def run_game():
    """Run the actual Cracky-Bird game."""
    global cracky_bird_rect, fallspeed, gravity, pipe_rect, pipes

    # Define game variables.
    fallspeed = 0
    gravity = .2
    pipes = []

    cracky_bird_rect = assets.cracky_bird_img.get_rect()
    cracky_bird_rect.center = (CENTERX, CENTERY)
    pipe_frame = 0

    while True:
        restart_screen()

        while True:
            # Check for events.
            for event in pygame.event.get():

                # Check for quit.
                if event.type == QUIT:
                    terminate()

                # Check if the player is pressing a key.
                if event.type == KEYDOWN:
                    
                    # Check if the player pressed ESCAPE.
                    if event.key == K_ESCAPE:
                        terminate()

                # Check if the player released a key.
                if event.type == KEYUP:

                    # Check if the player wants to jump.
                    if event.key == K_SPACE or event.key == K_UP or \
                        event.key == K_w:
                        jump_bird(JUMPHEIGHT)

                # Check if the player has released the mouse.
                if event.type == MOUSEBUTTONUP:
                    jump_bird(JUMPHEIGHT)

            # Draw the background.
            DISPLAYSURF.blit(assets.background, (0, 0))

            # Update and check the pipe frame.
            pipe_frame += 1
            if pipe_frame >= PIPESPAWNRATE:
                pipe_frame = 0
                spawn_pipe()

            # Move the pipes.
            move_pipes()

            # Draw the pipes.
            for pipe in pipes:
                DISPLAYSURF.blit(pipe['img'], pipe['rect'])

            # Update the bird.
            emulate_gravity()

            if check_bird_collision() == True:
                # The bird has hit something.
                break

            DISPLAYSURF.blit(assets.cracky_bird_img, cracky_bird_rect)

            # Update the display.
            pygame.display.update()
            MAINCLOCK.tick(FPS)


def move_pipes():
    """Move the pipes."""
    global pipes

    # Move the pipe.
    for pipe in pipes:
        pipe['rect'].left -= PIPESPEED

        # Check if the pipe is off the screen.
        if pipe['rect'].right <= 0:
            pipes.remove(pipe)


def spawn_pipe():
    """Spawn in a new pipe."""
    global pipes

    pipe = assets.pipe_img
    
    new_pipe = {'img': pipe, 'rect': pipe.get_rect()}

    new_pipe['rect'].top = random.randint(0, WINDOWHEIGHT - 400)
    new_pipe['rect'].left = WINDOWWIDTH

    pipes.append(new_pipe)


def restart_screen():
    """Show this screen before each round starts."""
    pass


def check_bird_collision():
    """Check if the bird is touching obstacles or edges of screen."""

    if cracky_bird_rect.centery <= 0:
        return True 
    
    elif cracky_bird_rect.centery >= WINDOWHEIGHT:
        return True


def jump_bird(jump_height):
    """Make the cracky-bird jump."""
    global fallspeed

    fallspeed = -jump_height


def emulate_gravity():
    """Emulate the cracky-bird's gravity."""
    global cracky_bird_rect, fallspeed
    
    cracky_bird_rect.y += fallspeed
    fallspeed += gravity


def terminate():
    """Quit out of the program."""
    pygame.quit()
    sys.exit()


class Assets():
    """Represent Crack-Bird's assets."""

    def __init__(self):
        """Initialize the assets."""

        self.background = pygame.image.load('images/background.png')
        self.background = pygame.transform.scale(self.background, 
                                                 (WINDOWWIDTH, WINDOWHEIGHT))
        
        self.cracky_bird_img = pygame.image.load('images/cracky_bird.png')
        self.cracky_bird_img = pygame.transform.scale(self.cracky_bird_img,
                                                      (60, 60))
        
        self.pipe_img = pygame.image.load('images/pipe.png')
        self.pipe_img = pygame.transform.scale(self.pipe_img, (60, 400))



# Run flappy bird.
main()