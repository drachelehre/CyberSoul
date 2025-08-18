conditions = {
    "decayed": 0.1,
    "poor": 0.15,
    "subpar": 0.2,
    "good": 0.3,
    "excellent": 0.2,
    "pristine": 0.05
    }

# name: worth, cost, range_attack, shoot_range, rate
ranged_arms = {
    "finger gun": [200, 5, 15, 50, 1.2],
    "hand cannon": [500, 10, 25, 80, 0.8],
    "laser bolt blaster": [2000, 25, 50, 150, 0.3],
}

# name: worth, cost, melee_attack, melee_size
melee_arms = {
    "dagger": [100, 5, 5, 20],
    "gladius": [250, 7, 12, 25],
    "scimitar": [400, 12, 18, 30]
}

# name: size, health, ranged_atk, ranged_rate, shot_range,  melee_atk, defense, speed
enemies = {
    "grunt": (12, 50, 5, 3, 100, 0, 0, 40),
    "archer": (14, 40, 8, 1.2, 200, 0, 0, 50),
    "tank": (20, 200, 0, 0, 0, 15, 10, 25),
}
