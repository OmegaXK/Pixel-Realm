"""Load in the assets for the main GUI."""

# Imports.
import os
import pygame
from pygame.locals import *

# Window constants.
WINDOWWIDTH = 960
WINDOWHEIGHT = 540
APPWIDTH = 100
APPHEIGHT = 100

# Set up path.
resource_path = os.path.join(os.path.dirname(__file__), '')
resource_path = resource_path.replace('operating_system/system/', 'operating_system/')
rp = resource_path # Make the code a little shorter.


class Images():
    """A class to represent the images."""

    def __init__(self):
        """Initialize the images."""

        self.desktop_wallpaper = pygame.image.load(f"{rp}assets/images/desktop_wallpaper.png")
        self.desktop_wallpaper = pygame.transform.scale(self.desktop_wallpaper, 
                                                        (WINDOWWIDTH, WINDOWHEIGHT))

        self.browser_logo = pygame.image.load(f"{rp}assets/images/browser_logo.png")
        self.browser_logo = pygame.transform.scale(self.browser_logo, 
                                                   (APPWIDTH, APPHEIGHT))

        self.notepad_logo = pygame.image.load(f'{rp}assets/images/notepad_logo.png')
        self.notepad_logo = pygame.transform.scale(self.notepad_logo, 
                                                   (APPWIDTH, APPHEIGHT))
        
        self.explorer_logo = pygame.image.load(f'{rp}assets/images/file_explorer_logo.png')
        self.explorer_logo = pygame.transform.scale(self.explorer_logo, 
                                                    (APPWIDTH, APPHEIGHT))
        
        self.settings_logo = pygame.image.load(f'{rp}assets/images/settings_logo.png')
        self.settings_logo = pygame.transform.scale(self.settings_logo,
                                                    (APPWIDTH, APPHEIGHT))
        
        self.pixel_realm_logo = pygame.image.load(f'{rp}assets/images/pixel_realm_logo.png')
        self.pixel_realm_logo = pygame.transform.scale(self.pixel_realm_logo,
                                                       (32, 32))
        
        self.rps_logo = pygame.image.load(f'{rp}assets/images/rps_logo.png')
        self.rps_logo = pygame.transform.scale(self.rps_logo,
                                               (APPWIDTH, APPHEIGHT))
        
        self.ttt_logo = pygame.image.load(f'{rp}assets/images/ttt_logo.png')
        self.ttt_logo = pygame.transform.scale(self.ttt_logo,
                                               (APPWIDTH, APPHEIGHT))
        
        self.cracky_bird_logo = pygame.image.load(f'{rp}assets/images/cracky_bird_logo.png')
        self.cracky_bird_logo = pygame.transform.scale(self.cracky_bird_logo,
                                                       (APPWIDTH, APPHEIGHT))
        
        self.enter_logo = pygame.image.load(f'{rp}assets/images/enter_logo.png')
        self.enter_logo = pygame.transform.scale(self.enter_logo,
                                                 (APPWIDTH, APPHEIGHT))

        self.crack_tube_logo = pygame.image.load(f'{rp}assets/images/crack_tube_logo.png')
        self.crack_tube_logo = pygame.transform.scale(self.crack_tube_logo,
                                                      (APPWIDTH, APPHEIGHT))
        
        self.hangman_logo = pygame.image.load(f'{rp}assets/images/hangman_logo.png')
        self.hangman_logo = pygame.transform.scale(self.hangman_logo, 
                                                   (APPWIDTH, APPHEIGHT))
        
        self.crackai_logo = pygame.image.load(f'{rp}assets/images/crackai_logo.png')
        self.crackai_logo = pygame.transform.scale(self.crackai_logo,
                                                   (APPWIDTH, APPHEIGHT))
        
        self.crackazon_logo = pygame.image.load(f'{rp}assets/images/crackazon_logo.png')
        self.crackazon_logo = pygame.transform.scale(self.crackazon_logo,
                                                     (APPWIDTH, APPHEIGHT))
        
        self.crack_chat_logo = pygame.image.load(f'{rp}assets/images/crack_chat_logo.png')
        self.crack_chat_logo = pygame.transform.scale(self.crack_chat_logo,
                                                      (APPWIDTH, APPHEIGHT))
        
        self.more_apps_logo = pygame.image.load(f'{rp}assets/images/more_apps.png')
        self.more_apps_logo = pygame.transform.scale(self.more_apps_logo,
                                                     (APPWIDTH, APPHEIGHT))
        
        self.crack_dash_logo = pygame.image.load(f'{rp}assets/images/crack_dash_logo.png')
        self.crack_dash_logo = pygame.transform.scale(self.crack_dash_logo,
                                                      (APPWIDTH, APPHEIGHT))
        
        self.be_crack_logo = pygame.image.load(f'{rp}assets/images/be_crack_logo.png')
        self.be_crack_logo = pygame.transform.scale(self.be_crack_logo,
                                                    (APPWIDTH, APPHEIGHT))
        
        self.crackle_maps_logo = pygame.image.load(f'{rp}assets/images/crackle_maps_logo.png')
        self.crackle_maps_logo = pygame.transform.scale(self.crackle_maps_logo,
                                                        (APPWIDTH, APPHEIGHT))
        
        self.mine_crack_logo = pygame.image.load(f'{rp}assets/images/mine_crack_logo.png')
        self.mine_crack_logo = pygame.transform.scale(self.mine_crack_logo,
                                                      (APPWIDTH, APPHEIGHT))
        
        self.crack_mail_logo = pygame.image.load(f'{rp}assets/images/crack_mail_logo.png')
        self.crack_mail_logo = pygame.transform.scale(self.crack_mail_logo,
                                                      (APPWIDTH, APPHEIGHT))
        
        self.free_robux_logo = pygame.image.load(f'{rp}assets/images/free_robux_logo.png')
        self.free_robux_logo = pygame.transform.scale(self.free_robux_logo,
                                                      (APPWIDTH, APPHEIGHT))
        

class Sounds:
    """A class to represent the sounds."""

    def __init__(self):
        """Initialize the sounds."""

        self.startup = pygame.mixer.Sound(f'{rp}assets/sounds/startup.wav')

        self.open_app = pygame.mixer.Sound(f'{rp}assets/sounds/open_app.wav')