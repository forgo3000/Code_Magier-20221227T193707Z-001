from ast import Break
from turtle import update
import pygame, os
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)

        w, h = pygame.display.get_surface().get_size()

        # Backround
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Code_Magier', 'Assets', 'Magier.png')).convert_alpha(), (w * 0.03125 ,h * 0.088888))

        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.looking = "right"
    
    def input(self):
        keys_pressed = pygame.key.get_pressed()
        w, h = pygame.display.get_surface().get_size()

        if keys_pressed[pygame.K_a]:
            self.direction.x = -1
            if self.looking == "right":
                self.image = pygame.transform.flip(self.image,1,0)
                self.looking = "left"
        elif keys_pressed[pygame.K_d]:
            self.direction.x = 1
            if self.looking == "left":
                self.image = pygame.transform.flip(self.image,1,0)
                self.looking = "right"
        else:
            self.direction.x = 0

        if keys_pressed[pygame.K_SPACE]:
            self.direction.y = -1
            
        elif self.rect.y + self.image.get_height() <= h - (h * 0.072222222222):
            self.direction.y = 1
        else:
            self.direction.y = 0
        

    def move(self, speed):

        self.rect.center += self.direction * speed
    
    def update(self):
        self.input()
        self.move(self.speed)