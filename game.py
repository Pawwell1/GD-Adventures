import sys
import pygame
import random

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('GD Adventures')
        self.screen = pygame.display.set_mode((1920, 1080))
        self.Icon = pygame.image.load('Resources/Profile Circle.png')
        pygame.display.set_icon(self.Icon)
        self.img = pygame.image.load('Resources/gk-icon.png')
        self.img2 = pygame.image.load('Resources/BE_Export_File-uhd.png')

        self.clock = pygame.time.Clock()

        self.img_pos = [160, 260]
        self.img2_pos = [70, 69]
        
    def run(self):
        while True:
            self.screen.blit(self.img, self.img_pos)
            self.screen.blit(self.img2, self.img2_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()