import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        #start the main look for the game 
        
        while True:
            #watch for keyboard and mouse movements 
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _update_bullets(self):
        self.bullets.update()
        #update position of bullets and get rid of old bullets 
        #update bullet positions  
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        #respond to key releases 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        #create a new bullet and add it to the bullets group 
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        #redraw the screen for each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)
        #make most recently drawn screen visible
        pygame.display.flip()

    def _create_fleet(self):
        #create the fleet of aliens 
        #make an alien and find the number of aliens in a row 
        #spacing between each alien is equal to one alien width 
        alien= Alien(self)
        alien_width, alien_height = alien.rect.size 
        alien_width = alien.rect.width
        availible_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = availible_space_x // (2*alien_width)

        #determine the number of rows of aliens that fit on the screen 
        ship_height = self.ship.rect.height
        availible_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = availible_space_y // (2 * alien_height)

        #create a full fleet of aliens 
        for row_number in range(number_rows):
            for alien_number in range (number_aliens_x):
                self._create_alien(alien_number, row_number)
            

    def _create_alien(self, alien_number, row_number):
        #create an alien and place it in the row 
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien) 

        


if __name__ == '__main__':
    #make a game instance and run the game 
    ai = AlienInvasion()
    ai.run_game()
