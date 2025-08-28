import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

SCREEN_WIDTH = config["screen"]["width"]
SCREEN_HEIGHT = config["screen"]["height"]

ENEMY_MIN_SIZE = config["enemy"]["min_size"]
ENEMY_SIZES = config["enemy"]["sizes"]
ENEMY_BASE_SPEED = config["enemy"]["base_speed"]
ENEMY_MAX_SIZE = config["enemy"]["sizes"] * config["enemy"]["min_size"]
ENEMY_SPAWN_MIN = config["enemy"]["spawn_min"]
ENEMY_SPAWN_MAX = config["enemy"]["spawn_max"]
ENEMY_MELEE_SIZE = config["enemy"]["melee_size"]
ENEMY_SHOOT_SPEED = config["enemy"]["shoot_speed"]
ENEMY_MELEE_RATE = config["enemy"]["melee_rate"]

PLAYER_BASE_SPEED = config["player"]["base_speed"]
PLAYER_BASE_REGEN = config["player"]["base_regen"]
PLAYER_BASE_REGEN_RATE = config["player"]["base_regen_rate"]
PLAYER_SHOOT_SPEED = config["player"]["shoot_speed"]

SHOT_BASE_RANGE = config["shot"]["base_range"]
SHOT_RADIUS = config["shot"]["radius"]

MELEE_BASE_SIZE = config["melee"]["base_size"]
MELEE_SWIPE_RATE = config["melee"]["swipe_rate"]

ITEMS_PER_PAGE = config["ui"]["items_per_page"]
