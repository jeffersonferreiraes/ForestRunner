import pygame
import random
import os
from config import *


class Collectible(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'coin.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + random.randrange(0, 300)
        self.rect.y = HEIGHT - random.randrange(120, 250)
        self.speed = GAME_SPEED

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()