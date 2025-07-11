import pygame
from code.config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'player.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 4, HEIGHT - 100)
        self.pos = pygame.math.Vector2(WIDTH / 4, HEIGHT - 100)
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)
        self.jumping = False
        self.score = 0

    def update(self):
        self.acc = pygame.math.Vector2(0, PLAYER_GRAVITY)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jump()

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.y > HEIGHT - 100:
            self.pos.y = HEIGHT - 100
            self.vel.y = 0
            self.jumping = False

        self.rect.midbottom = self.pos

    def jump(self):
        self.vel.y = -PLAYER_JUMP
        self.jumping = True
        self.game.jump_sound.play()