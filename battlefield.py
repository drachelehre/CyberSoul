import pygame
from constants import *
from enemy import *
from random import *
from utils import *


class BattleField(pygame.sprite.Sprite):
    containers = ()

    def __init__(self, player):
        # Unpack containers tuple when adding to sprite groups
        pygame.sprite.Sprite.__init__(self, *self.containers)
        self.player = player
        self.spawn_timer = 0.0

    def spawn(self):
        # Generate enemy and automatically add it to Enemy.containers groups
        enemy = generate_enemy(self.player)
        return enemy

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer >= ENEMY_SPAWN_MAX:
            self.spawn_timer = 0
            self.spawn()

