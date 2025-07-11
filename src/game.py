import pygame
import random
import os
import sys
from config import *
from player import Player
from obstacle import Obstacle
from collectible import Collectible


class Game:
    def __init__(self):
        try:
            pygame.init()
            pygame.mixer.init()
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption(TITLE)
            self.clock = pygame.time.Clock()
            self.running = True
            self.font = pygame.font.SysFont('Arial', 30)

            # Controle de spawn
            self.last_obstacle_x = WIDTH
            self.min_obstacle_distance = 400

            self.load_assets()
            self.reset()

        except pygame.error as e:
            print(f"Erro ao inicializar o Pygame: {e}")
            sys.exit(1)

    def load_assets(self):
        try:
            # Carrega imagens
            self.background = pygame.image.load(os.path.join(IMG_DIR, 'background.png')).convert()
            self.ground = pygame.image.load(os.path.join(IMG_DIR, 'ground.png')).convert()

            # Carrega sons
            self.jump_sound = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'jump.wav'))
            self.collect_sound = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'collect.wav'))
            self.game_over_sound = pygame.mixer.Sound(os.path.join(AUDIO_DIR, 'game_over.wav'))

            # Configura música de fundo
            music_path = os.path.join(AUDIO_DIR, 'SuperHero_original_no_Intro.ogg')
            if os.path.exists(music_path):
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.set_volume(0.5)
            else:
                print(f"Aviso: Arquivo de música não encontrado em {music_path}")

        except Exception as e:
            print(f"Erro ao carregar assets: {e}")
            sys.exit(1)

    def reset(self):
        self.all_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

        self.score = 0
        self.game_speed = GAME_SPEED
        self.obstacle_timer = 0
        self.collectible_timer = 0
        self.playing = True
        self.last_obstacle_x = WIDTH

        # Inicia/Reinicia a música
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.music.play(loops=-1)

    def spawn_obstacle(self):
        x_pos = WIDTH + random.randint(50, 200)
        obs = Obstacle(self, x_pos)
        self.obstacles.add(obs)
        self.all_sprites.add(obs)
        self.last_obstacle_x = x_pos

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.playing:
                    self.reset()
                # Tecla M para mute/unmute
                if event.key == pygame.K_m:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

    def update(self):
        if not self.playing:
            return

        self.all_sprites.update()

        now = pygame.time.get_ticks()
        if now - self.obstacle_timer > OBSTACLE_FREQUENCY + random.randrange(-500, 500):
            if (not self.obstacles) or (WIDTH - self.last_obstacle_x > self.min_obstacle_distance):
                self.obstacle_timer = now
                self.spawn_obstacle()

        if now - self.collectible_timer > COLLECTIBLE_FREQUENCY + random.randrange(-1000, 1000):
            self.collectible_timer = now
            if not self.obstacles or (random.random() > 0.5):
                col = Collectible(self)
                self.collectibles.add(col)
                self.all_sprites.add(col)

        # Verifica colisões
        for obstacle in self.obstacles:
            if pygame.sprite.collide_rect(self.player, obstacle):
                self.playing = False
                self.game_over_sound.play()
                break

        hits = pygame.sprite.spritecollide(self.player, self.collectibles, True)
        for hit in hits:
            self.score += 10
            self.collect_sound.play()

        self.game_speed = GAME_SPEED + self.score // 100

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.ground, (0, HEIGHT - 100))

        self.all_sprites.draw(self.screen)

        score_text = self.font.render(f'Score: {self.score}', True, BLACK)
        self.screen.blit(score_text, (10, 10))

        if not self.playing:
            game_over_text = self.font.render('Game Over! Press SPACE to restart', True, RED)
            self.screen.blit(game_over_text, (WIDTH / 2 - 200, HEIGHT / 2))

        pygame.display.flip()

    def run(self):
        try:
            while self.running:
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.draw()

        except Exception as e:
            print(f"Erro durante a execução: {e}")

        finally:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()