import sys
import pygame

class AlienInvasion:
    #Overall class to manage game assets and behavior

    def __init__(self):
        #initialize the game, and create game resources 
        pygame.init()
        
        #screen dimensions adjusted for my pc 
        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Alien Invasion")

        #self background color 
        self.bg_color = (230, 230, 230)

    def run_game(self):
        #start the main look for the game 
        
        while True:
            #watch for keyboard and mouse movements 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen for each pass through the loop
            self.screen.fill(self.bg_color)
            #make most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    #make a game instance and run the game 
    ai = AlienInvasion()
    ai.run_game()
