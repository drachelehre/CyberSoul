import random
from lists import *
from parts import *
from rangedarm import *
from meleearm import *
from player import *
from enemy import *


def random_condition():
    r = random.random()
    total = 0
    for cond, prob in conditions.items():
        total += prob
        if r <= total:
            return cond
    return "good"  # fallback


def generate_ranged_arm():
    name, stats = random.choice(list(ranged_arms.items()))
    worth, cost, rng_bonus, shoot_bonus, rate = stats
    cond = random_condition()
    part = RangedArm(cond, worth, cost, rng_bonus, shoot_bonus, rate)
    part.name = name
    part.rate = rate
    part.ranged_adjust()  # apply condition scaling
    return part


def generate_melee_arm():
    name, stats = random.choice(list(melee_arms.items()))
    worth, cost, melee_attack, melee_size = stats
    cond = random_condition()
    part = MeleeArm(cond, worth, cost, melee_attack, melee_size)
    part.name = name
    part.melee_adjust()
    return part


def generate_enemy(player):
    name, stats = random.choice(list(enemies.items()))
    size, health, ranged_attack, ranged_rate, shot_range, melee_attack, defense, speed = stats

    edges = [
        lambda: (-ENEMY_MAX_SIZE, random.randint(0, SCREEN_HEIGHT)),
        lambda: (SCREEN_WIDTH + ENEMY_MAX_SIZE, random.randint(0, SCREEN_HEIGHT)),
        lambda: (random.randint(0, SCREEN_WIDTH), -ENEMY_MAX_SIZE),
        lambda: (random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT + ENEMY_MAX_SIZE),
    ]

    x, y = random.choice(edges)()

    enemy = Enemy(player, x, y, size, health, ranged_attack, ranged_rate, shot_range,
                  melee_attack, defense, speed)
    enemy.name = name
    return enemy
