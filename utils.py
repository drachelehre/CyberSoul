import random
from lists import *
from parts import *
from rangedarm import *


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
    part.cost_adjust()  # apply condition scaling
    return part
