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
    "laser bolt blaster": [2000, 25, 25, 150, 0.3],
    "plasma launcher": [6000, 50, 50, 200, .75]
}

# name: worth, cost, melee_attack, melee_size
melee_arms = {
    "dagger": [100, 5, 5, 20],
    "gladius": [250, 7, 12, 25],
    "scimitar": [400, 12, 18, 30]
}
# name: worth, cost, defense
chest_armor = {
    "aluminum armor": [20, 5, 2],
    "iron armor": [40, 5, 5],
    "kevlar armor": [100, 10, 10],
    "steel armor": [500, 20, 25],
    "titanium armor": [2000, 40, 50],
    "tungsten armor": [5000, 100, 200]
}

# name: worth, cost, speed
leg_mods = {
    "athletic springs": [15, 5, 60],
    "pneumatic knees": [180, 8, 70],
    "deployable skates": [1250, 15, 100],
    "rocket sleds": [4000, 25, 150]
}

# name: size, health, ranged_atk, ranged_rate, shot_range,  melee_atk, defense, speed
enemies = {
    "grunt": (12, 10, 5, 3, 100, 0, 0, 40),
    "archer": (14, 20, 8, 1.2, 200, 0, 0, 50),
    "tank": (20, 200, 0, 0, 0, 15, 10, 25),
}

PLAYER_STATS = [
        ("Max Health", "health_max"),
        ("Health", "health"),
        ("Ranged Attack", "ranged_attack"),
        ("Fire Range", "shoot_range"),
        ("Fire Rate", "shot_rate"),
        ("Melee Attack", "melee_attack"),
        ("Melee Size", "melee_size"),
        ("Melee Rate", "melee_rate"),
        ("Defense", "defense"),
        ("Speed", "speed"),
        ("Regeneration", "regenerate"),
        ("Regen Rate", "regen_rate")
    ]

EQUIPMENT_SLOTS = [
        ("Right Arm", "r_arm"),
        ("Melee Arm", "m_arm"),
        ("Chest", "chest"),
        ("Legs", "leg"),
        ("Chip", "chip"),
    ]


