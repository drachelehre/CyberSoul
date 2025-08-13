from entity import *
from constants import *
import pygame
import math
from player import *


class Melee(Entity):
    containers = ()

    def __init__(self, player, x, y, arc_angle=90, lifetime=0.2):
        super().__init__(x, y, MELEE_BASE_SIZE)
        self.player = player
        self.arc_angle = arc_angle
        self.lifetime = lifetime
        self.elapsed = 0
        self.range = MELEE_BASE_SIZE

        # Fix: symmetrical arc around player's facing
        center_angle = math.radians(self.player.rotation)
        half_arc = math.radians(self.arc_angle / 2)
        self.start_angle = center_angle - half_arc
        self.end_angle = center_angle + half_arc

    def draw(self, screen):
        # Base vector pointing right, rotated by player's current rotation
        direction = pygame.Vector2(1, 0).rotate(self.player.rotation)

        # Arc sweep
        half_arc = self.arc_angle / 2
        start_dir = direction.rotate(half_arc)
        end_dir = direction.rotate(-half_arc)

        rect = pygame.Rect(
            self.player.position.x - self.range,
            self.player.position.y - self.range,
            self.range * 2,
            self.range * 2
        )

        start_angle = math.atan2(-start_dir.y, start_dir.x)
        end_angle = math.atan2(-end_dir.y, end_dir.x)
        pygame.draw.arc(screen, "red", rect, start_angle, end_angle, 3)

    def update(self, dt):
        self.elapsed += dt
        if self.elapsed >= self.lifetime:
            self.kill()
