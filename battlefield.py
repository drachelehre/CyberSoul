import pygame

from constants import *
from player import Player
from random import *


class BattleField(pygame.sprite.Sprite):
    containers = ()

    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ENEMY_MAX_SIZE, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ENEMY_MAX_SIZE, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ENEMY_MAX_SIZE),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ENEMY_MAX_SIZE
            ),
        ],
    ]

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.player = player
        self.spawn_timer = 0.0

    def spawn(self, x, y, width, height, rotation):
        pass

    def update(self, dt):
        self.spawn_timer += dt






