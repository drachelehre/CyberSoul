import pygame


class Entity(pygame.sprite.Sprite):
    """
    Superclass of all Entity classes
    """
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
        """Tracks position of invisible rectangle hit box

        :return: None
        """
        self.rect.center = (round(self.position.x), round(self.position.y))

    def collides_with(self, other):
        """Return True if this entity's rect overlaps with another's"""
        return self.rect.colliderect(other.rect)

    def on_collision(self, other):
        """Override in subclasses to define behavior"""
        pass
