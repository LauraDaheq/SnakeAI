import pygame

from game.settings import (
    WIDTH,
    HEIGHT,
    CELL_SIZE
)


class Snake:

    def __init__(
        self,
        name="Jugador",
        color=(40, 210, 70),
        controller="human",
        ai=None,
        start_pos=(300, 300),
        direction=(1, 0)
    ):

        self.name = name
        self.color = color

        self.controller = controller
        self.ai = ai

        self.score = 0
        self.alive = True

        self.direction = direction

        x, y = start_pos

        self.body = [
            (x, y),
            (x - CELL_SIZE, y),
            (x - CELL_SIZE * 2, y),
            (x - CELL_SIZE * 3, y),
            (x - CELL_SIZE * 4, y)
        ]

    # =====================================
    # IA
    # =====================================

    def update_ai(self, enemy, food, walls):

        if not self.alive:
            return

        if self.controller != "ai":
            return

        if self.ai is None:
            return


        move = self.ai.get_move(
            self,
            enemy,
            food,
            walls
        )


        if move is not None:
            self.change_direction(move)

    # =====================================
    # DIRECCIÓN
    # =====================================

    def change_direction(self, direction):

        opposite = (
            -self.direction[0],
            -self.direction[1]
        )

        if direction != opposite:
            self.direction = direction

    # =====================================
    # MOVIMIENTO
    # =====================================

    def move(self):

        if not self.alive:
            return


        x, y = self.body[0]

        dx, dy = self.direction


        x += dx * CELL_SIZE
        y += dy * CELL_SIZE



        # ==========================
        # CHOQUE CON BORDE
        # ==========================

        if x < 0 or x >= WIDTH:
            self.die()
            return


        if y < 0 or y >= HEIGHT:
            self.die()
            return



        self.body.insert(
            0,
            (x,y)
        )


        self.body.pop()

    # =====================================
    # CRECER
    # =====================================

    def grow(self):

        self.body.append(self.body[-1])
        self.score += 1

    # =====================================
    # MUERTE
    # =====================================

    def die(self):

        self.alive = False

    # =====================================
    # COLISIONES
    # =====================================

    def check_collision(self):

        head = self.body[0]

        if head in self.body[1:]:

            self.die()
            return True

        return False

    def check_enemy_collision(self, enemy):

        if enemy is None:
            return


        if not self.alive:
            return


        cabeza = self.body[0]


        if cabeza in enemy.body:

            self.die()


    # =====================================
    # DIBUJAR
    # =====================================

    def draw(self, screen):

        body_color = self.color if self.alive else (120, 120, 120)

        # ---------- cuerpo ----------

        for x, y in self.body[1:]:

            pygame.draw.rect(
                screen,
                body_color,
                (
                    x + 2,
                    y + 2,
                    CELL_SIZE - 4,
                    CELL_SIZE - 4
                ),
                border_radius=9
            )

        # ---------- cabeza ----------

        hx, hy = self.body[0]

        pygame.draw.rect(
            screen,
            body_color,
            (
                hx + 1,
                hy + 1,
                CELL_SIZE - 2,
                CELL_SIZE - 2
            ),
            border_radius=11
        )

        self.draw_eyes(screen)
        self.draw_tongue(screen)

    # =====================================
    # OJOS
    # =====================================

    def draw_eyes(self, screen):

        hx, hy = self.body[0]

        cx = hx + CELL_SIZE // 2
        cy = hy + CELL_SIZE // 2

        dx, dy = self.direction

        if dx == 1:

            eyes = [
                (cx + 5, cy - 5),
                (cx + 5, cy + 5)
            ]

        elif dx == -1:

            eyes = [
                (cx - 5, cy - 5),
                (cx - 5, cy + 5)
            ]

        elif dy == -1:

            eyes = [
                (cx - 5, cy - 5),
                (cx + 5, cy - 5)
            ]

        else:

            eyes = [
                (cx - 5, cy + 5),
                (cx + 5, cy + 5)
            ]

        for ex, ey in eyes:

            pygame.draw.circle(
                screen,
                (255, 255, 255),
                (ex, ey),
                4
            )

            pygame.draw.circle(
                screen,
                (0, 0, 0),
                (ex, ey),
                2
            )

    # =====================================
    # LENGUA
    # =====================================

    def draw_tongue(self, screen):

        if not self.alive:
            return

        hx, hy = self.body[0]

        cx = hx + CELL_SIZE // 2
        cy = hy + CELL_SIZE // 2

        dx, dy = self.direction

        start = (
            cx + dx * 10,
            cy + dy * 10
        )

        end = (
            cx + dx * 18,
            cy + dy * 18
        )

        pygame.draw.line(
            screen,
            (240, 60, 90),
            start,
            end,
            2
        )

        pygame.draw.line(
            screen,
            (240, 60, 90),
            end,
            (end[0] + dy * 3, end[1] + dx * 3),
            2
        )

        pygame.draw.line(
            screen,
            (240, 60, 90),
            end,
            (end[0] - dy * 3, end[1] - dx * 3),
            2
        )