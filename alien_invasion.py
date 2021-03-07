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
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        #start the main look for the game 
        
        while True:
            #watch for keyboard and mouse movements 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen for each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #make most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    #make a game instance and run the game 
    ai = AlienInvasion()
    ai.run_game()
