import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.size = size

        # bounding box for collisions
        self.rect = pygame.Rect(0, 0, size * 2, size * 2)
        self.rect.center = (x, y)

        # who I collide with
        self.collision_groups = []

    def update_rect(self):
        self.rect.center = (round(self.position.x), round(self.position.y))

    def update(self, dt):
        self.update_rect()
        self.check_collisions()

    def check_collisions(self):
        """Check collisions with registered groups"""
        for group in self.collision_groups:
            hits = pygame.sprite.spritecollide(self, group, False)
            for target in hits:
                if target is not self:
                    self.on_collision(target)

    def on_collision(self, other):
        """Default behavior — override in subclasses"""
        pass
