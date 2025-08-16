import random
from lists import *
from parts import *
from rangedarm import *
from meleearm import *


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
