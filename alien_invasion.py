import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    #Overall class to manage game assets and behavior

    def __init__(self):
        #initialize the game, and create game resources 
        pygame.init()
        
        self.settings = Settings()

        #screen dimensions adjusted for my pc 
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        #start the main look for the game 
        
        while True:
            #watch for keyboard and mouse movements 
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event) 
                
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        #respond to key press 
        if event.key == pygame.K_RIGHT:
            #move key to the right 
            self.ship.moving_right = True 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        #respond to key releases 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        #redraw the screen for each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #make most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    #make a game instance and run the game 
    ai = AlienInvasion()
    ai.run_game()
