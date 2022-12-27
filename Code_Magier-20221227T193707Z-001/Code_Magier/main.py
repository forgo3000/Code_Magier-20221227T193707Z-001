import pygame, sys
from settings import *
from level import Level
from pygame.locals import *

class Game:
    def __init__(self):

        # general setup
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Coder_Magier")
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while(True):
            
            keys_pressed = pygame.key.get_pressed()

            for event in pygame.event.get():
                # 0 zum beenden
                if event.type == pygame.QUIT or keys_pressed[pygame.K_0]:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('white')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()

