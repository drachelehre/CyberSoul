import pygame
import json
import os
from entity import *
from player import *
from enemy import *
from parts import *
from constants import *
from crosshair import *
from battlefield import *
from utils import *
from melee import *


SAVE_FOLDER = "saves"


def save_game(player):
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    filename = os.path.join(SAVE_FOLDER, f"{player.name}_save.json")

    data = {
        "name": player.name,
        "x": player.x,
        "y": player.y,
        "health": player.health,
        "health_max": player.health_max,
        "ranged_attack": player.ranged_attack,
        "ranged_bonus": player.ranged_bonus,
        "melee_attack": player.melee_attack,
        "melee_bonus": player.melee_bonus,
        "defense": player.defense,
        "armor_bonus": player.armor_bonus,
        "speed": player.speed,
        "speed_bonus": player.speed_bonus,
        "humanity": player.humanity,
        "rotation": player.rotation,
        "credits": player.credits,
        "shoot_range": player.shoot_range,
        "shoot_bonus": player.shoot_bonus,
        "melee_size": player.melee_size,
        "melee_size_bonus": player.melee_size_bonus,
        "chip": player.chip,
        "eye": player.eye,
        "r_arm": player.r_arm,
        "m_arm": player.m_arm,
        "chest": player.chest,
        "leg": player.leg,
        "resistance": player.resistance,
        "immunity": player.immunity,
        "vulnerability": player.vulnerability,
        "inventory":player.inventory
    }

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Game saved to {filename}")


def load_game(name):
    filename = os.path.join(SAVE_FOLDER, f"{name}_save.json")
    if not os.path.exists(filename):
        print(f"No save found for {name}.")
        return None

    with open(filename, "r") as f:
        data = json.load(f)

    player = Player(data["x"], data["y"], data["name"])
    player.health = data["health"]
    player.health_max = data["health_max"]
    player.ranged_attack = data["ranged_attack"]
    player.ranged_bonus = data["ranged_bonus"]
    player.melee_attack = data["melee_attack"]
    player.melee_bonus = data["melee_bonus"]
    player.defense = data["defense"]
    player.armor_bonus = data["armor_bonus"]
    player.speed = data["speed"]
    player.speed_bonus = data["speed_bonus"]
    player.humanity = data["humanity"]
    player.rotation = data["rotation"]
    player.credits = data["credits"]
    player.shoot_range = data["shoot_range"]
    player.shoot_bonus = data["shoot_bonus"]
    player.melee_size = data["melee_size"]
    player.melee_size_bonus = data["melee_size_bonus"]
    player.chip = data["chip"]
    player.eye = data["eye"]
    player.r_arm = data["r_arm"]
    player.m_arm = data["m_arm"]
    player.chest = data["chest"]
    player.leg = data["leg"]
    player.inventory = data["inventory"]

    print(f"Game loaded from {filename}")
    return player


def inventory_menu(screen, player):
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 24)

    clock = pygame.time.Clock()
    selected_index = 0
    page = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_r:
                    return
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % min(ITEMS_PER_PAGE, len(player.inventory) - page * ITEMS_PER_PAGE)
                elif event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % min(ITEMS_PER_PAGE, len(player.inventory) - page * ITEMS_PER_PAGE)
                elif event.key == pygame.K_RIGHT:
                    page = min(page + 1, max(0, (len(player.inventory) - 1) // ITEMS_PER_PAGE))
                    selected_index = 0
                elif event.key == pygame.K_LEFT:
                    page = max(0, page - 1)
                    selected_index = 0
                elif event.key == pygame.K_RETURN:
                    if player.inventory:
                        item = player.inventory[page * ITEMS_PER_PAGE + selected_index]
                        player.equip(item)

        screen.fill((30, 30, 30))

        title = font.render(f"Inventory (Page {page + 1})", True, (255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))

        # Show current humanity
        humanity_text = small_font.render(f"Humanity: {player.humanity}", True, (255, 180, 180))
        screen.blit(humanity_text, (SCREEN_WIDTH - humanity_text.get_width() - 20, 20))

        # Display items for current page
        start_index = page * ITEMS_PER_PAGE
        end_index = start_index + ITEMS_PER_PAGE
        for i, item in enumerate(player.inventory[start_index:end_index]):
            color = (255, 255, 0) if i == selected_index else (200, 200, 200)

            if isinstance(item, RangedArm):
                text = f"{item.condition} {item.name}"
                stats = (
                    f"Worth: {item.worth} | "
                    f"Rng+{item.ranged_bonus} | "
                    f"Shoot+{item.shoot_bonus} | "
                    f"Rate {item.rate} | "
                    f"Cost {item.cost} humanity"
                )
                item_surface = small_font.render(text, True, color)
                stats_surface = small_font.render(stats, True, (180, 180, 180))

                screen.blit(item_surface, (50, 150 + i * 60))
                screen.blit(stats_surface, (70, 180 + i * 60))
            else:
                text = f"{item.__class__.__name__} ({item.condition})"
                item_surface = small_font.render(text, True, color)
                screen.blit(item_surface, (50, 150 + i * 40))

        pygame.display.flip()
        clock.tick(60)


def pause_menu(screen, player):
    font = pygame.font.Font(None, 60)
    small_font = pygame.font.Font(None, 36)

    title = font.render("Paused", True, (255, 255, 255))
    save_text = small_font.render("S - Save Game", True, (200, 200, 200))
    return_text = small_font.render("R - Return to Game", True, (200, 200, 200))
    quit_text = small_font.render("Q - Quit to Main Menu", True, (200, 200, 200))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    save_game(player)
                elif event.key == pygame.K_r:
                    return  # go back to game
                elif event.key == pygame.K_q:
                    return "quit"

        screen.fill((0, 0, 0))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 150))
        screen.blit(save_text, (SCREEN_WIDTH // 2 - save_text.get_width() // 2, 250))
        screen.blit(return_text, (SCREEN_WIDTH // 2 - return_text.get_width() // 2, 300))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 350))

        pygame.display.flip()
        clock.tick(60)


def get_player_name(screen, prompt="Enter player name:"):
    font = pygame.font.Font(None, 48)
    clock = pygame.time.Clock()
    input_text = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and input_text.strip():
                    return input_text.strip()
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif len(input_text) < 20:  # limit name length
                    input_text += event.unicode

        screen.fill((0,0,0))
        prompt_surface = font.render(prompt, True, (255,255,255))
        input_surface = font.render(input_text, True, (200,200,200))
        screen.blit(prompt_surface, (SCREEN_WIDTH//2 - prompt_surface.get_width()//2, 200))
        screen.blit(input_surface, (SCREEN_WIDTH//2 - input_surface.get_width()//2, 300))
        pygame.display.flip()
        clock.tick(60)

def status_screen(screen, player):
    pass

def game_over(screen):
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    game_over_note = font.render("Game OVER", True, (255, 255, 255))
    bad_end_hum = small_font.render("You lost yourself to the machine", True, (200, 200, 200))
    screen.fill((0, 0, 0))
    screen.blit(game_over_note, (SCREEN_WIDTH // 2 - game_over_note.get_width() // 2, 150))
    screen.blit(bad_end_hum, (SCREEN_WIDTH // 2 - bad_end_hum.get_width() // 2, 300))


def main_menu(screen):
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    title = font.render("Cyborg Soul", True, (255, 255, 255))
    start_text = small_font.render("Press ENTER to Start New Game", True, (200, 200, 200))
    load_text = small_font.render("Press L to Load Game", True, (200, 200, 200))
    quit_text = small_font.render("Press ESC to Quit", True, (200, 200, 200))

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    name = get_player_name(screen, "Name your character:")
                    return "new", name
                elif event.key == pygame.K_l:
                    name = get_player_name(screen, "Enter save name:")
                    return "load", name
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit(); exit()

        screen.fill((0, 0, 0))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 150))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 300))
        screen.blit(load_text, (SCREEN_WIDTH // 2 - load_text.get_width() // 2, 350))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 400))
        pygame.display.flip()
        clock.tick(60)


def choose_save_file(screen):
    saves = [f[:-10] for f in os.listdir(SAVE_FOLDER) if f.endswith("_save.json")]
    if not saves:
        return None
    font = pygame.font.Font(None, 48)
    clock = pygame.time.Clock()
    index = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return saves[index]
                elif event.key == pygame.K_UP:
                    index = (index - 1) % len(saves)
                elif event.key == pygame.K_DOWN:
                    index = (index + 1) % len(saves)

        screen.fill((0,0,0))
        for i, name in enumerate(saves):
            color = (255,255,0) if i == index else (200,200,200)
            text_surface = font.render(name, True, color)
            screen.blit(text_surface, (SCREEN_WIDTH//2 - text_surface.get_width()//2, 200 + i*50))
        pygame.display.flip()
        clock.tick(60)


def game_loop(player):
    pygame.display.set_caption("Cyborg Soul")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    melee = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    BattleField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Melee.containers = (melee, updatable, drawable)

    player.add(*Player.containers)  # make sure player is in groups
    crosshair = Crosshair()
    field = BattleField(player)

    player.inventory.append(generate_ranged_arm())
    player.inventory.append(generate_ranged_arm())
    player.inventory.append(generate_ranged_arm())

    dt = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # pause menu
                    choice = pause_menu(screen, player)
                    if choice == "quit":
                        return  # quit to main menu
                if event.key == pygame.K_i:
                    inventory_menu(screen, player)

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        crosshair.draw(screen)

        if player.humanity <= 0:
            game_over(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        choice, name = main_menu(screen)
        if choice == "new":
            player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, name)
            game_loop(player)
        elif choice == "load":
            player = load_game(name)
            if player:
                game_loop(player)


if __name__ == "__main__":
    main()
