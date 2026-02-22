import sys
import pygame
from setting import Settings

class Showroon:
    '''Overall class for managing the game assets and behavior'''
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))
        pygame.display.set_caption("Showroom")

    def run_game():
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self._update_screen()            
            self.clock.tick(60)


    def _check_events():
        '''respond to keyboard and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
# Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
            # MAke the most recently drawn screen visible.
        pygame.display.flip()  
