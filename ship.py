import pygame

class Ship:
    #a class to manage the ship 

    def __init__(self, ai_game):
        #initialize the game and set its starting position 
        self.screen = ai_game.screen