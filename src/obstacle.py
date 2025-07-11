import pygame
import random
import os
from config import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x_pos):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.type = random.choice(['rock', 'tree'])

        # Carrega imagens com alpha
        if self.type == 'rock':
            self.image = pygame.image.load(os.path.join(IMG_DIR, 'rock.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))  # Tamanho fixo para rocha
            self.hitbox = pygame.Rect(0, 0, 30, 30)  # Hitbox menor que o sprite
        else:
            self.image = pygame.image.load(os.path.join(IMG_DIR, 'tree.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (60, 80))  # Tamanho fixo para árvore
            self.hitbox = pygame.Rect(0, 0, 50, 60)  # Hitbox menor que o sprite

        self.rect = self.image.get_rect()
        self.rect.x = x_pos  # Posição recebida como parâmetro
        self.rect.bottom = HEIGHT - GROUND_HEIGHT + 5  # 5px acima do chão
        self.hitbox.midbottom = self.rect.midbottom  # Alinha hitbox
        self.speed = GAME_SPEED
        self.passed = False  # Para controle de pontuação

    def update(self):
        self.rect.x -= self.speed
        self.hitbox.midbottom = self.rect.midbottom  # Atualiza hitbox

        # Remove se sair da tela
        if self.rect.right < 0:
            self.kill()

        # Marca como passado quando sair da tela pela esquerda (para pontuação)
        if not self.passed and self.rect.right < WIDTH // 2:
            self.passed = True
            return True
        return False