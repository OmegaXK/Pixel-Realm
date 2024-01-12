"""Main code for Crack Dash."""

# Path: games/graphic_games/crack_dash

# Imports.
import random, json 
from pathlib import Path

import pygame
from pygame.locals import *

import data.assets as assets

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
JUMPHEIGHT = 18

# General constants.
FPS = int(preferences["FPS"])
GRAVITY = -1.5

# Colors.
BLACK = (0, 0, 0)

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
    images = assets.Images()

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Crack Dash")

    # Run the game.
    while True:
        run_game()
        pygame.time.wait(1000)


def run_game():
    """Run the main game."""
    global cube_rect, fallspeed, spikes, doubles, spike_speed, score
    global spike_rate

    # Define the game variables.
    score = 0
    cube_rect = images.cube_img.get_rect()
    fallspeed = 0
    spike_frame = 0
    spikes = []

    # These variables will update as the game progresses.
    spike_rate = 100
    doubles = False
    spike_speed = 7

    # Set up the player.
    cube_rect.centerx = CENTERX - 100
    cube_rect.bottom = WINDOWHEIGHT - GROUNDHEIGHT

    # Main loop.
    while True:

        # Check for events.
        for event in pygame.event.get():

            # Check for quit.
            if event.type == QUIT:
                assets.terminate()

            # Check if the player is pressing a key.
            if event.type == KEYDOWN:

                # Check for the ESCAPE key.
                if event.key == K_ESCAPE:
                    assets.terminate()

                # Check if the player is pressing a jump key.
                if event.key == K_UP or event.key == K_w:
                    cube_jump()
                
                if event.key == K_SPACE or event.key == K_RSHIFT:
                    cube_jump()

            if event.type == MOUSEBUTTONDOWN:
                cube_jump()

        # Draw the game on the screen.
        DISPLAYSURF.blit(images.bg_img, (0, 0))

        # Check to see if it's time to spawn a new spike.
        if spike_frame > spike_rate:
            spike_frame = 0
            spawn_spike()
        else:
            spike_frame += 1

        # Update the spikes, and check if we need to return.
        if update_spikes():
            return

        # Update the cube.
        cube_gravity()

        # Draw the cube.
        DISPLAYSURF.blit(images.cube_img, cube_rect)

        # Update the score.
        score += .1
        draw_score()

        # Update the level.
        update_level(score)

        # Update the game.
        pygame.display.update()
        MAINCLOCK.tick(FPS)


def update_level(score):
    """Update the variables based on the level."""
    global doubles, spike_speed, spike_rate

    if score >= 50:
        spike_rate = 70
        spike_speed = 8
    
    if score >= 100:
        spike_rate = 60
        spike_speed = 8.5
        doubles = True 

    if score >= 150:
        spike_rate = 50
        spike_speed = 9
    
    if score >= 200:
        spike_rate = 40
        spike_speed = 10
    
    if score >= 250:
        spike_speed = 12

    if score >= 300:
        spike_speed = 14


def draw_score():
    """Draw the score on the screen."""
    global score

    score_font = assets.create_font(30)
    score_surf = score_font.render(f"Score: {round(score)}", True, BLACK)
    score_rect = score_surf.get_rect()
    score_rect.topleft = (0, 0)
    DISPLAYSURF.blit(score_surf, score_rect)


def spawn_spike():
    """Spawn in a spike."""
    global spikes

    # Set up the new spike.
    new_spike = {}
    
    # Decide if the spike will be a double spike instead.
    if doubles:
        if random.randint(1, 2) == 1:
            new_spike['img'] = images.double_spike_img
        else:
            new_spike['img'] = images.spike_img
    else:
        new_spike['img'] = images.spike_img

    # Create the rect object.
    new_spike['rect'] = new_spike['img'].get_rect()
    new_spike['rect'].left = WINDOWWIDTH
    new_spike['rect'].bottom = WINDOWHEIGHT - GROUNDHEIGHT

    # Add the spike to the list.
    spikes.append(new_spike)


def update_spikes():
    """Update the spikes."""
    global spikes
    
    # Loop through all of the spikes.
    for spike in spikes[:]:

        # Move the spike.
        spike['rect'].x -= spike_speed

        # Check if the spike is offscreen.
        if spike['rect'].right <= 0:
            spikes.remove(spike)

        # Check if the spike is touching the player.
        if spike['rect'].colliderect(cube_rect):
            hit_player = True 
        else:
            hit_player = False
        
        # Draw the spike on the screen.
        DISPLAYSURF.blit(spike['img'], spike['rect'])

        # Return.
        return hit_player


def cube_gravity():
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