import pygame
from player import *
from entity import *


class Enemy(Entity):
    containers = ()

    def __init__(self, player, x, y, size, health, ranged_attack, ranged_rate, melee_attack, defense, speed):
        super().__init__(x, y, size)
        self.x = x
        self.y = y
        self.add(*self.containers)
        self.player = player
        self.health = health
        self.ranged_attack = ranged_attack
        self.ranged_rate = ranged_rate
        self.melee_attack = melee_attack
        self.defense = defense
        self.speed = speed
        self.rotation = 0

    def enemy_shape(self):
        points = [
            (0, -12),  # head top
            (6, -6),
            (4, 0),
            (8, 6),
            (4, 8),
            (4, 14),
            (0, 18),
            (-4, 14),
            (-4, 8),
            (-8, 6),
            (-4, 0),
            (-6, -6),
        ]
        rotated = []
        for px, py in points:
            vec = pygame.Vector2(px, py).rotate(self.rotation)  # negative for pygame's y-down

            rotated.append((self.position.x + vec.x, self.position.y + vec.y))
        return rotated

    def draw(self, screen):
        pygame.draw.polygon(screen, "red", self.enemy_shape())

    def update(self, dt):
        if not self.player:
            return  # safety check

        # current enemy position as Vector2
        enemy_pos = pygame.Vector2(self.x, self.y)
        # player position as Vector2
        player_pos = pygame.Vector2(self.player.x, self.player.y)

        # vector pointing from enemy to player
        direction_vector = player_pos - enemy_pos

        if direction_vector.length() > 0:
            # normalize to get direction only
            direction_vector = direction_vector.normalize()

            # move enemy toward player
            enemy_pos += direction_vector * self.speed * dt

            # update Enemy coordinates
            self.x, self.y = enemy_pos.x, enemy_pos.y
            self.position.x, self.position.y = self.x, self.y

            # rotate to face the player
            self.rotation = direction_vector.angle_to(pygame.Vector2(1, 0))
            self.position.x, self.position.y = self.x, self.y

            # Update rotation so enemy faces the player
            self.rotation = direction_vector.angle_to(pygame.Vector2(1, 0))
