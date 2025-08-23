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
from legs import *


SAVE_FOLDER = "saves"

ITEM_CLASSES = {
    "RangedArm": RangedArm,
    "MeleeArm": MeleeArm,
    "Chest": Chest,
    "Leg": Legs,
    "Chip": Chip
    # add others here
}

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
        "melee_attack": player.melee_attack,
        "defense": player.defense,
        "speed": player.speed,
        "humanity": player.humanity,
        "rotation": player.rotation,
        "credits": player.credits,
        "shoot_range": player.shoot_range,
        "shot_rate": player.shot_rate,
        "melee_size": player.melee_size,
        "regenerate": player.regenerate,
        "regen_timer": player.regen_timer,
        "regen_rate": player.regen_timer,
        "chip": player.chip.to_dict() if player.chip else None,
        "r_arm": player.r_arm.to_dict() if player.r_arm else None,
        "m_arm": player.m_arm.to_dict() if player.m_arm else None,
        "chest": player.chest.to_dict() if player.chest else None,
        "leg": player.leg.to_dict() if player.leg else None,
        "inventory": [item.to_dict() for item in player.inventory]
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
    player.melee_attack = data["melee_attack"]
    player.defense = data["defense"]
    player.speed = data["speed"]
    player.humanity = data["humanity"]
    player.rotation = data["rotation"]
    player.credits = data["credits"]
    player.shoot_range = data["shoot_range"]
    player.shot_rate = data["shot_rate"]
    player.melee_size = data["melee_size"]
    player.regenerate = data["regenerate"]
    player.regen_timer = data['regen_timer']
    player.regen_rate = data["regen_rate"]

    # equipment
    def load_part(part_data):
        if part_data is None:
            return None
        cls = ITEM_CLASSES.get(part_data["type"])
        if cls:
            return cls.from_dict(part_data)
        return None

    player.r_arm = load_part(data["r_arm"])
    player.m_arm = load_part(data["m_arm"])
    player.chest = load_part(data["chest"])
    player.leg = load_part(data["leg"])
    player.chip = load_part(data["chip"])
    player.inventory = [load_part(item) for item in data["inventory"]]

    print(f"Game loaded from {filename}")
    return player


def inventory_menu(screen, player):
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 24)
    inv_font = pygame.font.Font(None, 16)

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
                elif event.key == pygame.K_s:
                    status_screen(screen, player)
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
                    f"Attack: {item.ranged_attack} | "
                    f"Range: {item.shoot_range} | "
                    f"Rate: {item.rate} | "
                    f"Cost: {item.cost} humanity"
                )
                item_surface = inv_font.render(text, True, color)
                stats_surface = inv_font.render(stats, True, (180, 180, 180))

                screen.blit(item_surface, (50, 120 + i * 45))
                screen.blit(stats_surface, (70, 140 + i * 45))
            elif isinstance(item, MeleeArm):
                text = f"{item.condition} {item.name}"
                stats = (
                    f"Worth: {item.worth} | "
                    f"Attack: {item.melee_attack} | "
                    f"Range: {item.melee_size} | "
                    f"Cost: {item.cost} humanity"
                )
                item_surface = inv_font.render(text, True, color)
                stats_surface = inv_font.render(stats, True, (180, 180, 180))

                screen.blit(item_surface, (50, 120 + i * 45))
                screen.blit(stats_surface, (70, 140 + i * 45))
            elif isinstance(item, Chest):
                text = f"{item.condition} {item.name}"
                stats = (
                    f"Worth: {item.worth} | "
                    f"Defense: {item.defense} | "
                    f"Cost {item.cost} humanity"
                )
                item_surface = inv_font.render(text, True, color)
                stats_surface = inv_font.render(stats, True, (180, 180, 180))

                screen.blit(item_surface, (50, 120 + i * 45))
                screen.blit(stats_surface, (70, 140 + i * 45))
            elif isinstance(item, Legs):
                text = f"{item.condition} {item.name}"
                stats = (
                    f"Worth: {item.worth} | "
                    f"Speed: {item.speed} | "
                    f"Cost {item.cost} humanity"
                )
                item_surface = inv_font.render(text, True, color)
                stats_surface = inv_font.render(stats, True, (180, 180, 180))

                screen.blit(item_surface, (50, 120 + i * 45))
                screen.blit(stats_surface, (70, 140 + i * 45))
            elif isinstance(item, Chip):
                text = f"{item.condition} {item.name}"
                stats = (
                    f"Worth: {item.worth} | "
                    f"Melee Rate: {item.melee_rate} | "
                    f"Regenerate: {item.regenerate} | "
                    f"Regen Rate: {item.regen_rate} | "
                    f"Cost {item.cost} humanity"
                )
                item_surface = inv_font.render(text, True, color)
                stats_surface = inv_font.render(stats, True, (180, 180, 180))

                screen.blit(item_surface, (50, 120 + i * 45))
                screen.blit(stats_surface, (70, 140 + i * 45))
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
    title_font = pygame.font.Font(None, 48)
    section_font = pygame.font.Font(None, 32)
    item_font = pygame.font.Font(None, 22)
    exit_font = pygame.font.Font(None, 18)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_r):
                    return
                elif event.key == pygame.K_s:
                    inventory_menu(screen, player)

        screen.fill((0, 0, 0))

        # Title
        title_text = title_font.render("Status", True, (255, 255, 255))
        screen.blit(title_text, (750 // 2 - title_text.get_width() // 2, 30))

        # Column headers
        equip_text = section_font.render("Equipment", True, (255, 255, 255))
        stats_text = section_font.render("Stats", True, (255, 255, 255))

        left_x = 100      # equipment column start
        right_x = 400     # stats column start
        top_y = 90        # start just below title

        screen.blit(equip_text, (left_x, top_y))
        screen.blit(stats_text, (right_x, top_y))

        # Equipment list (left column)
        y = top_y + 40
        for label, attr in EQUIPMENT_SLOTS:
            item = getattr(player, attr, None)
            item_name = item.name if item else "None"
            text = item_font.render(f"{label}: {item_name}", True, (200, 200, 200))
            screen.blit(text, (left_x, y))
            y += 28  # line spacing

        # Stats list (right column)
        y = top_y + 40
        for label, attr in PLAYER_STATS:
            value = getattr(player, attr, "N/A")
            text = item_font.render(f"{label}: {value}", True, (200, 200, 200))
            screen.blit(text, (right_x, y))
            y += 28  # line spacing

        # Exit hint
        exit_text = exit_font.render("Press Esc or R to go back", True, (255, 255, 255))
        screen.blit(exit_text, (20, 480))

        pygame.display.flip()
        clock.tick(60)




def game_over(screen):
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    load_font = pygame.font.Font(None, 24)
    exit_font = pygame.font.Font(None, 20)
    game_over_note = font.render("Game Over", True, (255, 255, 255))
    bad_end_hum = small_font.render("You lost to the machine", True, (200, 200, 200))
    load_text = load_font.render("Press 'L' to load a file", True, "grey")
    screen.fill((0, 0, 0))
    screen.blit(game_over_note, (SCREEN_WIDTH // 2 - game_over_note.get_width() // 2, 150))
    screen.blit(bad_end_hum, (SCREEN_WIDTH // 2 - bad_end_hum.get_width() // 2, 300))
    screen.blit(load_text, (SCREEN_WIDTH // 2 - load_text.get_width() // 2, 350))

    exit_text = exit_font.render("Press q to go to main menu", True, (255, 255, 255))
    screen.blit(exit_text, (20, 480))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                main_menu(screen)



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
    enemy_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    BattleField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Melee.containers = (melee, updatable, drawable)
    Enemy.containers = (enemy_group, updatable, drawable)

    player.add(*Player.containers)  # make sure player is in groups
    crosshair = Crosshair()
    field = BattleField(player)

    dt = 0
    running = True

    # drop notification initialization
    drop_text = None
    drop_text_timer = 0
    drop_font = pygame.font.Font(None, 24)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # pause menu
                    selection = pause_menu(screen, player)
                    if selection == "quit":
                        return  # quit to main menu
                if event.key == pygame.K_r:
                    inventory_menu(screen, player)
                if event.key == pygame.K_c:
                    status_screen(screen, player)

        small_font = pygame.font.Font(None, 24)

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        crosshair.draw(screen)

        # Show current and maximum hp
        health_text = small_font.render(f"Health: {player.health}/{player.health_max}", True, (255, 180, 180))
        screen.blit(health_text, (SCREEN_WIDTH//7 - health_text.get_width() + 20, 10))

        # Show current credit amount
        credits_text = small_font.render(f"Credits: {player.credits}", True, (255, 180, 180))
        screen.blit(credits_text, (SCREEN_WIDTH - credits_text.get_width() - 20, 10))

        if player.humanity <= 0 or player.health <= 0:
            game_over(screen)

        # Player shots hit enemies
        for shot in shots:
            if isinstance(shot.owner, Player):
                hits = pygame.sprite.spritecollide(shot, enemy_group, False)
                for enemy in hits:
                    enemy.health -= shot.owner.ranged_attack
                    shot.kill()

        # Enemy shots hit player
        for shot in shots:
            if isinstance(shot.owner, Enemy):
                if player.rect.colliderect(shot.rect):
                    player.health -= max(1, shot.owner.ranged_attack - player.defense)
                    shot.kill()

        # Player melee hits enemies
        for m in melee:
            if isinstance(m.owner, Player):
                hits = pygame.sprite.spritecollide(m, enemy_group, False)
                for enemy in hits:
                    enemy.health -= m.owner.melee_attack

        # Enemy melee hits player
        for m in melee:
            if isinstance(m.owner, Enemy):
                if player.rect.colliderect(m.rect):
                    player.health -= max(1, m.owner.melee_attack - player.defense)

        # Enemy death/drop check
        for e in enemy_group:
            if e.health <= 0:
                e.kill()
                money_drop(player)
                part, dropped = part_drop()
                if dropped:
                    player.inventory.append(part)
                    drop_text = drop_font.render(f"{part.name} dropped!", True, (255, 255, 0))
                    drop_text_timer = pygame.time.get_ticks() + 5000  # show for 5s

        # Drop Notification
        if drop_text and pygame.time.get_ticks() < drop_text_timer:
            screen.blit(drop_text, (SCREEN_WIDTH // 2 - drop_text.get_width() // 2, 450))
        else:
            drop_text = None

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
