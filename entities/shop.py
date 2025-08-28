from utils import generate_random_part
import pygame, random
from .entity import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Shop(Entity):
    containers = ()

    def __init__(self, player, size=20):
        # Offset based on % of screen size
        offset_x = SCREEN_WIDTH // 20   # ~5% of width
        offset_y = SCREEN_HEIGHT // 20  # ~5% of height

        # Pick a random corner, scaled offset
        corners = [
            (offset_x, offset_y),  # top-left
            (SCREEN_WIDTH - offset_x, offset_y),  # top-right
            (offset_x, SCREEN_HEIGHT - offset_y),  # bottom-left
            (SCREEN_WIDTH - offset_x, SCREEN_HEIGHT - offset_y)  # bottom-right
        ]
        x, y = random.choice(corners)

        super().__init__(x, y, size)
        self.player = player
        self.inventory = []
        self.stock()

    def draw(self, screen) -> None:
        """Draws shop

        :param screen:
        :return: None
        """
        # Green rectangle
        pygame.draw.rect(screen, "green", self.rect)

        # Black outline
        pygame.draw.rect(screen, "black", self.rect, width=2)

        # Dollar sign
        font = pygame.font.SysFont(None, self.size * 2)
        text = font.render("$", True, "white")
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def stock(self) -> None:
        """Stocks instance of shop

        :return:
        """
        self.inventory.clear()
        while len(self.inventory) < 7:
            part = generate_random_part()
            self.inventory.append(part)