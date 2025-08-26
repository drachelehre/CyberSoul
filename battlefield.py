import pygame
from constants import *
from enemy import *
from random import *
from utils import *


class BattleField(pygame.sprite.Sprite):
    containers = ()

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, *self.containers)
        self.player = player

        # Set the first spawn time randomly between 3 and 10 seconds
        self.next_spawn_time = random.uniform(3, 10)
        self.next_boss_spawn = 300
        self.next_shop_timer = 180
        self.spawn_timer = 0.0
        self.boss_spawn_timer = 0.0
        self.shop_spawn_timer = 0.0

    def spawn(self):
        enemy = generate_enemy(self.player)
        return enemy

    def spawn_boss(self):
        boss = generate_boss(self.player)
        return boss

    def spawn_shop(self):
        pass

    def update(self, dt):
        self.spawn_timer += dt
        self.boss_spawn_timer += dt
        self.shop_spawn_timer += dt

        if self.spawn_timer >= self.next_spawn_time:
            self.spawn_timer = 0
            self.next_spawn_time = random.uniform(3, 10)  # pick next spawn time
            self.spawn()

        if self.boss_spawn_timer >= self.next_boss_spawn:
            self.boss_spawn_timer = 0
            self.next_boss_spawn = 300
            self.spawn_boss()
