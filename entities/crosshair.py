import pygame


class Crosshair:
    def __init__(self):
        self.color = (255, 255, 255)  # white
        self.size = 10                # length of crosshair lines
        self.thickness = 2            # line thickness

    def draw(self, screen):
        mx, my = pygame.mouse.get_pos()
        pygame.draw.line(screen, self.color, (mx - self.size, my), (mx + self.size, my), self.thickness)
        pygame.draw.line(screen, self.color, (mx, my - self.size), (mx, my + self.size), self.thickness)
