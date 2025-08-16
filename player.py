import pygame
import math
from entity import *
from constants import *
from rangedarm import *
from meleearm import *
from shot import *
from melee import *


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
        self.melee_attack = 2
        self.defense = 1
        self.speed = PLAYER_BASE_SPEED
        self.humanity = 1000
        self.rotation = 0
        self.add(*self.containers)
        self.timer = 0
        self.credits = 0
        self.shoot_range = SHOT_BASE_RANGE
        self.shot_rate = 1.5
        self.melee_size = MELEE_BASE_SIZE
        self.melee_rate = MELEE_SWIPE_RATE
        self.chip = None
        self.eye = None
        self.r_arm = None
        self.m_arm = None
        self.chest = None
        self.leg = None
        self.inventory = []

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

            rotated.append((self.position.x + vec.x, self.position.y + vec.y))
        return rotated

    def draw(self, screen):
        pygame.draw.polygon(screen, "blue", self.player_shape())

    def move(self, dt):
        forward = pygame.Vector2(0, 1)
        return forward * PLAYER_BASE_SPEED * dt

    def equip(self, part):
        """
        Equip a Part object, deduct humanity, and apply its bonuses.
        Old part bonuses are removed but humanity is never refunded.
        """
        # Humanity cost is paid immediately
        self.humanity -= part.cost
        if self.humanity < 0:
            self.humanity = 0  # just to avoid going negative

        # Equip based on type
        if isinstance(part, RangedArm):
            # Remove bonuses from currently equipped ranged arm and put back in inventory
            if self.r_arm:
                self.inventory.append(self.r_arm)

            # Equip new part
            self.r_arm = part
            self.ranged_attack = part.ranged_attack
            self.shoot_range = part.shoot_range
            self.shot_rate = self.r_arm.rate

        elif isinstance(part, MeleeArm):
            # Remove bonuses from currently equipped ranged arm and put back in inventory
            if self.r_arm:
                self.inventory.append(self.r_arm)

            # Equip new part
            self.r_arm = part
            self.melee_attack = part.melee_attack
            self.melee_size = part.melee_size

        # TODO: elif isinstance(part, ChestArmor): ...
        # TODO: add other types here

        # Remove from inventory so it's not re-used
        if part in self.inventory:
            self.inventory.remove(part)

    def update(self, dt):
        # ROTATION toward mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.position.x
        dy = mouse_y - self.position.y
        self.rotation = math.degrees(math.atan2(dy, dx))

        # MOVEMENT
        keys = pygame.key.get_pressed()
        move_vec = pygame.Vector2(0, 0)
        if keys[pygame.K_a]:
            move_vec.x -= 1
        if keys[pygame.K_d]:
            move_vec.x += 1
        if keys[pygame.K_w]:
            move_vec.y -= 1
        if keys[pygame.K_s]:
            move_vec.y += 1

        if move_vec.length_squared() > 0:
            move_vec = move_vec.normalize() * PLAYER_BASE_SPEED * dt
            self.position += move_vec

        # ATTACKS
        if pygame.mouse.get_pressed()[0]:
            self.shoot(dt)
        if pygame.mouse.get_pressed()[2]:
            self.melee(dt)

    def shoot(self, dt):
        if self.timer > 0:
            self.timer -= dt
            return

        if not pygame.mouse.get_pressed()[0]:  # Left click only
            return

        direction = pygame.Vector2(1, 0).rotate(self.rotation)
        velocity = direction * PLAYER_SHOOT_SPEED

        shot = Shot(
            self.position.x,
            self.position.y,
            velocity,
            self.shoot_range
        )

        shot.add(*Shot.containers)
        self.timer = self.shot_rate

    def melee(self, dt):
        if self.timer > 0:
            self.timer -= dt
            return

        if not pygame.mouse.get_pressed()[2]:  # Right click only
            return

        melee_attack = Melee(self, self.position.x, self.position.y)
        melee_attack.add(*Melee.containers)

        self.timer = self.melee_rate
