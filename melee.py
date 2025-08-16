from entity import *
from constants import *
import pygame
import math
from player import *


class Melee(Entity):
    containers = ()

    def __init__(self, player, x, y, arc_angle=90, lifetime=0.2):
        super().__init__(x, y, player.melee_size)
        self.player = player
        self.arc_angle = arc_angle
        self.lifetime = lifetime
        self.elapsed = 0
        self.range = player.melee_size

        # Fix: symmetrical arc around player's facing
        center_angle = math.radians(self.player.rotation)
        half_arc = math.radians(self.arc_angle / 2)
        self.start_angle = center_angle - half_arc
        self.end_angle = center_angle + half_arc

    def draw(self, screen):
        direction = pygame.Vector2(1, 0).rotate(self.player.rotation)

        # Make arc angle change over time
        growth_factor = (self.elapsed / self.lifetime)
        current_arc_angle = self.arc_angle + 60 * growth_factor  # grows by up to +60 degrees

        half_arc = current_arc_angle / 2
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

        # Make line thickness change instead of radius
        thickness = int(3 + 5 * growth_factor)

        pygame.draw.arc(screen, "red", rect, start_angle, end_angle, thickness)

    def update(self, dt):
        self.elapsed += dt
        if self.elapsed >= self.lifetime:
            self.kill()
