import pygame, os

class Test():


    def __init__(self):

        w, h = pygame.display.get_surface().get_size()
        
        # Backround
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Code_Magier', 'Assets', 'Room.png')).convert_alpha(), (w,h))

       #self.rect = self.image.get_rect(topleft = numbers)
    
        
