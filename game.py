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
        self.img = pygame.image.load('Resources/Profile Circle.png')

        self.clock = pygame.time.Clock()

        self.img_pos = [160, 260]
        self.movement = [False, False]
        
    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()