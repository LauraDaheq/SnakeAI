# ============================================
# CONFIGURACIÓN GENERAL
# ============================================

import pygame

pygame.init()

# -----------------------------
# Tamaño de la ventana
# -----------------------------
WIDTH = 1000
HEIGHT = 700

# Tamaño de cada casilla
CELL_SIZE = 25

# Cuadrícula
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

# FPS
FPS = 12


# ============================================
# COLORES
# ============================================

BACKGROUND = (42, 24, 16)

GRID_LIGHT = (56, 35, 22)
GRID_DARK = (48, 29, 18)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (220, 60, 60)
GREEN = (55, 205, 75)
BLUE = (70, 160, 255)

YELLOW = (255, 220, 40)

GRAY = (110, 110, 110)

SNAKE_GREEN = (40, 210, 70)
SNAKE_BLUE = (70, 170, 255)

FOOD_RED = (230, 55, 55)


# ============================================
# FUENTES
# ============================================

TITLE_FONT = pygame.font.SysFont(
    "arial",
    48,
    bold=True
)

MENU_FONT = pygame.font.SysFont(
    "arial",
    30
)

SMALL_FONT = pygame.font.SysFont(
    "arial",
    22
)


# ============================================
# CONTROLES
# ============================================

PLAYER1 = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}

PLAYER2 = {
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1),
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0),
}