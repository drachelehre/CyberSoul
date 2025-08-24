import pygame
from entity import *
from utils import generate_random_part


class Shop(Entity):
    def __init__(self, player, x, y, size):
        super().__init__(x, y, size)
        self.player = player
        self.inventory = []

    def stock(self):
        for i in range(9):
            self.inventory.append(generate_random_part())
