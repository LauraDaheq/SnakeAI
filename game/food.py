import random
import pygame

from game.settings import *


class Food:

    def __init__(self):
        self.position = self.random_position()

    def random_position(self):

        x = random.randrange(
            0,
            WIDTH // CELL_SIZE
        ) * CELL_SIZE

        y = random.randrange(
            0,
            HEIGHT // CELL_SIZE
        ) * CELL_SIZE

        return (x, y)

    def respawn(self):
        self.position = self.random_position()

    def draw(self, screen):

        x = self.position[0] + CELL_SIZE // 2
        y = self.position[1] + CELL_SIZE // 2

        pygame.draw.ellipse(
            screen,
            RED,
            pygame.Rect(x - 10, y - 11, 20, 22)
        )

        pygame.draw.ellipse(
            screen,
            DARK_RED,
            pygame.Rect(x - 7, y + 5, 14, 5)
        )

        pygame.draw.circle(
            screen,
            (255, 150, 150),
            (x - 5, y - 5),
            3
        )

        pygame.draw.line(
            screen,
            (90, 50, 20),
            (x, y - 11),
            (x + 3, y - 18),
            3
        )

        pygame.draw.ellipse(
            screen,
            (40, 180, 60),
            pygame.Rect(x + 2, y - 18, 8, 5)
        )