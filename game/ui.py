import pygame

from game.settings import *


class UI:

    def __init__(self):

        self.font = pygame.font.SysFont("arial", 28, bold=True)
        self.big_font = pygame.font.SysFont("arial", 80, bold=True)
        self.medium_font = pygame.font.SysFont("arial", 40, bold=True)

    def draw_hud(self, screen, score, speed, elapsed_time):

        minutes = elapsed_time // 60
        seconds = elapsed_time % 60

        screen.blit(
            self.font.render(f"Puntos: {score}", True, WHITE),
            (20, 20)
        )

        screen.blit(
            self.font.render(f"Velocidad: {speed}", True, WHITE),
            (20, 55)
        )

        screen.blit(
            self.font.render(
                f"Tiempo: {minutes:02}:{seconds:02}",
                True,
                WHITE
            ),
            (20, 90)
        )

    def draw_game_over(self, screen, score):

        # Fondo oscuro transparente
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(170)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # GAME OVER
        title = self.big_font.render(
            "GAME OVER",
            True,
            (230, 40, 40)
        )

        title_rect = title.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 120)
        )

        screen.blit(title, title_rect)

        # Puntaje
        score_text = self.medium_font.render(
            f"Puntuación: {score}",
            True,
            WHITE
        )

        score_rect = score_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 30)
        )

        screen.blit(score_text, score_rect)

        # Reiniciar
        restart = self.font.render(
            "ESPACIO - Jugar nuevamente",
            True,
            WHITE
        )

        restart_rect = restart.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 40)
        )

        screen.blit(restart, restart_rect)

        # Salir
        exit_text = self.font.render(
            "ESC - Salir",
            True,
            WHITE
        )

        exit_rect = exit_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 80)
        )

        screen.blit(exit_text, exit_rect)