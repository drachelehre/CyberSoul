import random
from lists import *
from parts import *
from rangedarm import *
from meleearm import *
from chest import *
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

def generate_chest_armor():
    name, stats = random.choice(list(chest_armor.items()))
    worth, cost, defense = stats
    cond = random_condition()
    part = Chest(cond, worth, cost, defense)
    part.name = name
    part.chest_adjust()
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


def money_drop(player):
    player.credits += random.randint(10, 201)

def generate_random_part():
    random_parts = [generate_ranged_arm(), generate_melee_arm(), generate_chest_armor()]
    return random.choice(random_parts)

def part_drop():
    drop = False
    drop_chance = 15
    roll = random.randint(1, 100)
    if roll <= drop_chance:
        drop = True
        return generate_random_part(), drop
    return None, drop
