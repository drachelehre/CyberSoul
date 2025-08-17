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

    def update(self, dt):
        self.elapsed += dt
        if self.elapsed >= self.lifetime:
            self.kill()

    def draw(self, surface):
        # Always use the current equipped melee arm size
        if hasattr(self.player, "m_arm") and self.player.m_arm is not None:
            arc_radius = self.player.m_arm.melee_size
        else:
            arc_radius = self.player.melee_size  # fallback

        progress = max(0, min(self.elapsed / self.lifetime, 1))

        # Short forward-facing arc
        center_angle = math.radians(-self.player.rotation)
        half_span = math.radians(self.arc_angle) / 2
        start_angle = center_angle - half_span
        end_angle = center_angle + half_span

        # Thickness grows slightly as it swings
        base_thickness = 4
        max_thickness = 20
        thickness = int(base_thickness + (max_thickness - base_thickness) * progress)

        pygame.draw.arc(
            surface,
            (255, 0, 0),
            pygame.Rect(
                self.player.position.x - arc_radius,
                self.player.position.y - arc_radius,
                arc_radius * 2,
                arc_radius * 2
            ),
            start_angle,
            end_angle,
            thickness
        )


