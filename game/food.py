import random
import pygame

from game.settings import (
    WIDTH,
    HEIGHT,
    CELL_SIZE,
    FOOD_RED,
    GREEN
)


class Food:

    def __init__(self):
        self.position = (0, 0)
        self.respawn([])

    # ======================================
    # GENERAR COMIDA
    # ======================================

    def respawn(self, occupied):

        while True:

            x = random.randrange(0, WIDTH, CELL_SIZE)
            y = random.randrange(0, HEIGHT, CELL_SIZE)

            if (x, y) not in occupied:
                self.position = (x, y)
                return

    # Compatibilidad si el main usa spawn()
    def spawn(self, occupied):
        self.respawn(occupied)

    # ======================================
    # DIBUJAR MANZANA
    # ======================================

    def draw(self, screen):

        x, y = self.position

        center = (
            x + CELL_SIZE // 2,
            y + CELL_SIZE // 2 + 1
        )

        radius = CELL_SIZE // 2 - 3

        # sombra
        pygame.draw.circle(
            screen,
            (120, 20, 20),
            (center[0] + 2, center[1] + 2),
            radius
        )

        # manzana
        pygame.draw.circle(
            screen,
            FOOD_RED,
            center,
            radius
        )

        # brillo
        pygame.draw.circle(
            screen,
            (255, 170, 170),
            (center[0] - 4, center[1] - 4),
            3
        )

        # tallo
        pygame.draw.line(
            screen,
            (80, 45, 20),
            (center[0], center[1] - radius),
            (center[0], center[1] - radius - 6),
            2
        )

        # hoja
        pygame.draw.ellipse(
            screen,
            GREEN,
            (
                center[0] + 1,
                center[1] - radius - 7,
                8,
                5
            )
        )

    # ======================================
    # POSICIÓN
    # ======================================

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]