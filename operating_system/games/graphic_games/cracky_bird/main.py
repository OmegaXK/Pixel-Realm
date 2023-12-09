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
PIPEMINY = -400
PIPEMAXY = -100
HITBOXWIDTH = 30

# Define other constants.
FPS = 60
JUMPHEIGHT = 4.3

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
    pygame.display.set_icon(assets.cracky_bird_img)
    
    # Run the game.
    run_game()


def run_game():
    """Run the actual Cracky-Bird game."""
    global cracky_bird_rect, fallspeed, gravity, pipe_rect, pipes, score
    global best_score

    # Define game variables.
    fallspeed = 0
    gravity = .2
    cracky_bird_rect = assets.cracky_bird_img.get_rect()
    best_score = 0
    score = 0

    while True:
        restart_screen()

        # Reset game variables before starting.
        pipe_frame = 0
        pipes = []
        score = 0

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
                pygame.time.wait(500)
                break
            
            # Draw the bird.
            DISPLAYSURF.blit(assets.cracky_bird_img, cracky_bird_rect)

            # Draw the score.
            draw_score(score)

            # Draw the best score.
            draw_best_score(best_score)

            # Update the display.
            pygame.display.update()
            MAINCLOCK.tick(FPS)


def restart_screen():
    """Show this screen before each round starts.
    This screen performs the following:
    1. Positions the bird in the center of the screen
    2. Holds that position until the player presses a jump button
    3. Returns to start the game."""

    global cracky_bird_rect, score, best_score

    # Calculate the player's best score.
    if score >= best_score:
        best_score = score

    # Position the bird.
    cracky_bird_rect.center = (CENTERX, CENTERY)

    # Draw the basic background.
    DISPLAYSURF.blit(assets.background, (0, 0))

    # Draw the player.
    DISPLAYSURF.blit(assets.cracky_bird_img, cracky_bird_rect)

    # Draw the score as 0.
    draw_score(0)

    # Draw the best score.
    draw_best_score(best_score)

    # Update.
    pygame.display.update()

    # Give the player a second to react.
    pygame.time.wait(500)

    # Repeat until the player presses a jump key.
    while True:

        # Check for events.
        for event in pygame.event.get():

            # Check for quit.
            if event.type == QUIT:
                terminate()

            # Check if the player is pressing a key.
            if event.type == KEYDOWN:

                # Check if the player is pressing the ESCAPE key.
                if event.key == K_ESCAPE:
                    terminate()

            # Check if the player has released a key.
            if event.type == KEYUP:

                # Check if the player wants to jump.
                    if event.key == K_SPACE or event.key == K_UP or \
                        event.key == K_w:
                        jump_bird(JUMPHEIGHT + 2)
                        return

            # Check if the player has released the mouse.
            if event.type == MOUSEBUTTONUP:
                jump_bird(JUMPHEIGHT + 2)
                return
            
        # Draw the basic background.
        DISPLAYSURF.blit(assets.background, (0, 0))

        # Draw the player.
        DISPLAYSURF.blit(assets.cracky_bird_img, cracky_bird_rect)

        # Draw the score as 0.
        draw_score(0)

        # Draw the best score.
        draw_best_score(best_score)

        # Update the screen.
        pygame.display.update()
        MAINCLOCK.tick(FPS)


def draw_best_score(best_score):
    """Draw the player's best score."""
    scorefont = create_font(30)
    bestscoresurf = scorefont.render(f'Best score: {best_score}', True, BLACK)
    bestscorerect = bestscoresurf.get_rect()
    bestscorerect.bottomleft = (0, WINDOWHEIGHT)
    DISPLAYSURF.blit(bestscoresurf, bestscorerect)


def draw_score(score):
    """Draw the current score text on the screen."""
    scorefont = create_font(30)
    scoresurf = scorefont.render(f'Score: {score}', True, BLACK)
    scorerect = scoresurf.get_rect()
    scorerect.topleft = (0, 0)
    DISPLAYSURF.blit(scoresurf, scorerect)


def move_pipes():
    """Move the pipes."""
    global pipes, score

    # Move the pipe.
    for pipe in pipes:
        pipe['rect'].left -= PIPESPEED

        # Check if the pipe is off the screen.
        if pipe['rect'].right <= 0:
            pipes.remove(pipe)

            # Update the score.
            score += 1


def spawn_pipe():
    """Spawn in a new pipe."""
    global pipes

    pipe = assets.pipe_img

    gap_size = 100
    gap_offset = -58  # Offset to align the gap with the visual gap.

    new_pipe = {}

    new_pipe['rect'] = pipe.get_rect()
    new_pipe['rect'].top = random.randint(PIPEMINY, PIPEMAXY)

    gap_start = new_pipe['rect'].centery - (gap_size / 2) - 30
    gap_end = new_pipe['rect'].centery + (gap_size / 2) - gap_offset

    new_pipe['img'] = assets.pipe_img
    new_pipe['gap_start'] = gap_start 
    new_pipe['gap_end'] = gap_end

    new_pipe['rect'].left = WINDOWWIDTH

    pipes.append(new_pipe)

                
def check_bird_collision():
    """Check if the bird is touching obstacles or edges of screen."""

    # Check if the bird is touching the floor and ceiling.
    if cracky_bird_rect.centery <= 0:
        return True 
    
    elif cracky_bird_rect.centery >= WINDOWHEIGHT:
        return True
    
    # Check if the bird has hit a pipe.
    for pipe in pipes:

        # Create separate rects for the top and bottom pipes.
        top_pipe_rect = pygame.Rect(pipe['rect'].left, pipe['rect'].top, 
                                    HITBOXWIDTH, 
                                    pipe['gap_start'] - pipe['rect'].top)
        bottom_pipe_rect = pygame.Rect(pipe['rect'].left, pipe['gap_end'], 
                                       HITBOXWIDTH, 
                                       pipe['rect'].bottom - pipe['gap_end'])

        # Check if the bird has hit any of the rects.
        if cracky_bird_rect.colliderect(top_pipe_rect) or \
            cracky_bird_rect.colliderect(bottom_pipe_rect):
            return True
        
    # The bird has not hit anything.
    return False


def jump_bird(jump_height):
    """Make the cracky-bird jump."""
    global fallspeed

    fallspeed = -jump_height


def emulate_gravity():
    """Emulate the cracky-bird's gravity."""
    global cracky_bird_rect, fallspeed
    
    cracky_bird_rect.y += fallspeed
    fallspeed += gravity


def create_font(size):
    """Return a font of the given size."""
    return pygame.font.Font('freesansbold.ttf', size)


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
        self.pipe_img = pygame.transform.scale(self.pipe_img, (60, 1000))


# Run cracky bird.
main()