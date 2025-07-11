import pygame
import os

# Configurações do jogo
WIDTH = 800
HEIGHT = 550
FPS = 60
TITLE = "Forest Runner"

# Caminhos
GAME_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(GAME_DIR, '../assets')
IMG_DIR = os.path.join(ASSETS_DIR, 'images')
AUDIO_DIR = os.path.join(ASSETS_DIR, 'audio')

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configurações do jogador
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 0.8
PLAYER_JUMP = 20

# Configurações do jogo
GAME_SPEED = 5
OBSTACLE_FREQUENCY = 1500  # ms
COLLECTIBLE_FREQUENCY = 3000  # ms

# Obstáculos
OBSTACLE_MIN_DISTANCE = 400  # Distância mínima entre obstáculos
OBSTACLE_SPAWN_RATE = 1500   # ms entre spawns

# Tamanhos
GROUND_HEIGHT = 100
PLAYER_HITBOX_REDUCTION = 0.7  # 70% do tamanho original para hitbox