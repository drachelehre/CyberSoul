from .enemy import *


class Boss(Enemy):
    containers = ()

    def __init__(self, player, x, y, size, health, ranged_attack, ranged_rate, shoot_range,
                 melee_attack, defense, speed):
        super().__init__(player, x, y, size, health, ranged_attack, ranged_rate, shoot_range,
                         melee_attack, defense, speed)
        self.x = x
        self.y = y
        self.add(*self.containers)
        self.size = size * 2
        self.player = player
        self.health = health * 2
        self.ranged_attack = ranged_attack
        self.shot_rate = ranged_rate * 1.5
        self.shoot_range = shoot_range
        self.melee_attack = melee_attack * 1.5
        self.melee_rate = ENEMY_MELEE_RATE * 1.5
        self.defense = defense * 1.2
        self.speed = speed
        self.rotation = 0
        self.timer = 0.0
        self.melee_timer = 0.0

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
        pygame.draw.polygon(screen, "yellow", self.enemy_shape())
