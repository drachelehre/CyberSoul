import pygame
from player import *
from entity import *


class Enemy(Entity):
    containers = ()

    def __init__(self, player, x, y, size, health, ranged_attack, ranged_rate, shoot_range,
                 melee_attack, defense, speed):
        super().__init__(x, y, size)
        self.x = x
        self.y = y
        self.add(*self.containers)
        self.player = player
        self.health = health
        self.ranged_attack = ranged_attack
        self.shot_rate = ranged_rate
        self.shoot_range = shoot_range
        self.melee_attack = melee_attack
        self.defense = defense
        self.speed = speed
        self.rotation = 0
        self.timer = 0.0



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
        player_pos = self.player.position
        enemy_pos = self.position

        direction_vector = player_pos - enemy_pos
        if direction_vector.length() > 0:
            direction_vector = direction_vector.normalize()
            enemy_pos += direction_vector * self.speed * dt
            self.position = enemy_pos
            self.x, self.y = self.position.x, self.position.y

            # rotate to face the player
            self.rotation = direction_vector.angle_to(pygame.Vector2(1, 0))

        # --- NEW: decide to shoot ---
        self.shoot(dt)

    def shoot(self, dt):
        if not hasattr(self, "timer"):
            self.timer = 0
        if self.timer > 0:
            self.timer -= dt
            return

        # distance to player
        to_player = self.player.position - self.position
        dist = to_player.length()

        # only fire if in range
        if dist <= self.shoot_range:
            direction = to_player.normalize()
            velocity = direction * PLAYER_SHOOT_SPEED

            spawn_pos = self.position + direction * 12  # muzzle offset

            shot = Shot(
                spawn_pos.x,
                spawn_pos.y,
                velocity,
                self.shoot_range,
                self  # owner
            )
            shot.add(*Shot.containers)

            self.timer = self.shot_rate  # cooldown



