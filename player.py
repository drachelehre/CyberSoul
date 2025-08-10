import pygame
from entity import *
from constants import *


class Player(Entity):
    containers = ()

    def __init__(self, x, y):
        super().__init__(x, y, 10)
        self.last_move_vec = None
        self.x = x
        self.y = y
        self.rotation = 0
        self.add(*self.containers)
        self.timer = 0

    def player_shape(self):
        return [
        (self.x + 0,  self.y - 12),  # head top
        (self.x + 6,  self.y - 6),   # head right
        (self.x + 4,  self.y + 0),   # right shoulder
        (self.x + 8,  self.y + 6),   # right elbow
        (self.x + 4,  self.y + 8),   # right waist
        (self.x + 4,  self.y + 14),  # right hip
        (self.x + 0,  self.y + 18),  # bottom
        (self.x - 4,  self.y + 14),  # left hip
        (self.x - 4,  self.y + 8),   # left waist
        (self.x - 8,  self.y + 6),   # left elbow
        (self.x - 4,  self.y + 0),   # left shoulder
        (self.x - 6,  self.y - 6),   # head left
    ]

    def draw(self, screen):
        pygame.draw.polygon(screen, (200, 50, 50), self.player_shape())

    def move(self, dt):
        forward = pygame.Vector2(0, 1)
        return forward * PLAYER_BASE_SPEED * dt

    def update(self, dt):
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
