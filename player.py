import pygame
import math
from entity import *
from constants import *


class Player(Entity):
    containers = ()

    def __init__(self, x, y, name):
        super().__init__(x, y, 10)
        self.name = name
        self.last_move_vec = None
        self.x = x
        self.y = y
        self.health_max = 100
        self.health = self.health_max
        self.ranged_attack = 2
        self.ranged_bonus = 0
        self.melee_attack = 2
        self.melee_bonus = 0
        self.defense = 1
        self.armor_bonus = 0
        self.speed = PLAYER_BASE_SPEED
        self.speed_bonus = 0
        self.humanity = 100
        self.rotation = 0
        self.add(*self.containers)
        self.timer = 0
        self.credits = 0
        self.shoot_range = 100
        self.shoot_bonus = 0
        self.melee_size = 40
        self.melee_size_bonus = 0
        self.chip = None
        self.eye = None
        self.r_arm = None
        self.m_arm = None
        self.chest = None
        self.leg = None
        self.resistance = None
        self.immunity = None
        self.vulnerability = None

    def player_shape(self):
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
            rotated.append((self.x + vec.x, self.y + vec.y))
        return rotated

    def draw(self, screen):
        pygame.draw.polygon(screen, "blue", self.player_shape())

    def move(self, dt):
        forward = pygame.Vector2(0, 1)
        return forward * PLAYER_BASE_SPEED * dt

    def update(self, dt):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        self.rotation = math.degrees(math.atan2(dy, dx))  # store in degrees

        keys = pygame.key.get_pressed()
        move_vec = pygame.Vector2(0, 0)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            move_vec.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            move_vec.x += 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            move_vec.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            move_vec.y += 1

        if move_vec.length_squared() > 0:
            move_vec = move_vec.normalize() * PLAYER_BASE_SPEED * dt
            self.x += move_vec.x
            self.y += move_vec.y
