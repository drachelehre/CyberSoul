from .entity import *
from constants import *
import pygame



class Shot(Entity):
    containers = ()

    def __init__(self, x, y, velocity, max_distance, owner):
        super().__init__(x, y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS
        self.velocity = velocity
        self.distance_traveled = 0
        self.max_distance = max_distance
        self.owner = owner  # <-- Player or Enemy

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        move_amount = self.velocity * dt
        self.position += move_amount
        self.distance_traveled += move_amount.length()

        if self.distance_traveled >= self.max_distance:
            self.kill()
        else:
            self.update_rect()

    def on_collision(self, other):
        from player import Player  # local import avoids circular import
        from enemy import Enemy  # same idea
        if isinstance(self.owner, Player) and isinstance(other, Enemy):
            other.health -= self.owner.ranged_attack
            self.kill()
        elif isinstance(self.owner, Enemy) and isinstance(other, Player):
            other.health -= max(1, self.owner.ranged_attack - other.defense)
            self.kill()