from entity import *
from constants import *
import pygame
import math
from player import *


class Melee(Entity):
    containers = ()

    def __init__(self, owner, x, y, arc_angle=90, lifetime=0.2):
        super().__init__(x, y, MELEE_BASE_SIZE)
        self.owner = owner  # <-- Player or Enemy
        self.arc_angle = arc_angle
        self.lifetime = lifetime
        self.elapsed = 0


    def update(self, dt):
        self.elapsed += dt
        if self.elapsed >= self.lifetime:
            self.kill()

    def draw(self, surface):
        # Always use the current equipped melee arm size
        if hasattr(self.owner, "m_arm") and self.owner.m_arm is not None:
            arc_radius = self.owner.m_arm.melee_size
        else:
            arc_radius = self.owner.melee_size  # fallback

        progress = max(0, min(self.elapsed / self.lifetime, 1))

        # Short forward-facing arc
        center_angle = math.radians(-self.owner.rotation)
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
                self.owner.position.x - arc_radius,
                self.owner.position.y - arc_radius,
                arc_radius * 2,
                arc_radius * 2
            ),
            start_angle,
            end_angle,
            thickness
        )


