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
        "vulnerability": player.vulnerability
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
    player.resistance = data["resistance"]
    player.immunity = data["immunity"]
    player.vulnerability = data["vulnerability"]

    print(f"Game loaded from {filename}")
    return player



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


def main_menu(screen):
    pygame.display.set_caption("Cyborg Soul - Main Menu")
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    title = font.render("Cyborg Soul", True, (255, 255, 255))
    start_text = small_font.render("Press ENTER to Start", True, (200, 200, 200))
    load_text = small_font.render("Press L to Load Game", True, (200, 200, 200))
    quit_text = small_font.render("Press ESC to Quit", True, (200, 200, 200))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "new"
                elif event.key == pygame.K_l:
                    return "load"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        screen.fill((0, 0, 0))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 150))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 300))
        screen.blit(load_text, (SCREEN_WIDTH // 2 - load_text.get_width() // 2, 350))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 400))

        pygame.display.flip()
        clock.tick(60)




def game_loop(load=False):
    pygame.display.set_caption("Cyborg Soul")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    BattleField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    crosshair = Crosshair()
    field = BattleField(player)

    if load:
        load_game(player)

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

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        crosshair.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        choice = main_menu(screen)
        if choice == "new":
            game_loop(load=False)
        elif choice == "load":
            game_loop(load=True)

if __name__ == '__main__':
    main()
