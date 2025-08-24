conditions = {
    "Decayed": 0.1,
    "Poor": 0.15,
    "Subpar": 0.2,
    "Good": 0.4,
    "Excellent": 0.1,
    "Pristine": 0.05
    }

# name: worth, cost, range_attack, shoot_range, rate
ranged_arms = {
    "Finger Gun": [200, 5, 15, 50, 1.2],
    "Hand Cannon": [500, 10, 25, 80, 0.8],
    "Laser Bolt Blaster": [2000, 25, 25, 150, 0.3],
    "Plasma Launcher": [6000, 50, 50, 200, .75]
}

# name: worth, cost, melee_attack, melee_size
melee_arms = {
    "Dagger": [100, 5, 5, 20],
    "Gladius": [250, 7, 12, 25],
    "Scimitar": [400, 12, 18, 30]
}
# name: worth, cost, defense
chest_armor = {
    "Aluminum Armor": [20, 5, 2],
    "Iron Armor": [40, 5, 5],
    "Kevlar Armor": [100, 10, 10],
    "Steel Armor": [500, 20, 25],
    "Titanium Armor": [2000, 40, 50],
    "Tungsten Armor": [5000, 100, 200]
}

# name: worth, cost, speed
leg_mods = {
    "Athletic Springs": [15, 5, 60],
    "Pneumatic Knees": [180, 8, 70],
    "Deployable Skates": [1250, 15, 100],
    "Rocket Sleds": [4000, 25, 150]
}

implant_chip = {
    "Muscle Twitch Enhancer": [4000, 100, .5, 0, 0],
    "Wound Closure": [5000, 200, 0, 1, .5],
    "Physical Overclock": [10000, 500, .1, 10, .1]
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
