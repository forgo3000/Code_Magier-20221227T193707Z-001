import pygame, os
from rooms import Room
from player import Player
from settings import *
from test import Test
class Level:

    def __init__(self):

        # get display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group  setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        self.backround()

        # sprite player
        self.human()

        self.test = Test()


    def backround(self):
        # Backround
        Room((0, 0), [self.visible_sprites])

    def objects(self):
        pass

    def human(self):
        # Player
        self.player = Player((20, HEIGHT/2), [self.visible_sprites])
        

    def run(self):
        # update and draw the game

        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()



        