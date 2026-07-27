from game.settings import WIDTH, HEIGHT, CELL_SIZE


class SimpleAI:
    """
    IA básica:
    - Busca la comida.
    - Evita retroceder.
    - Evita su propio cuerpo.
    - Evita el cuerpo enemigo.
    - Evita paredes (si están activadas).
    """

    def __init__(self, wrap=True):
        # wrap=True -> atraviesa paredes
        # wrap=False -> las paredes matan
        self.wrap = wrap

    def get_move(self, snake, enemy, food):

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # No retroceder
        opposite = (
            -snake.direction[0],
            -snake.direction[1]
        )

        valid = []

        for d in directions:

            if d == opposite:
                continue

            if self.is_safe(snake, enemy, d):
                valid.append(d)

        if not valid:
            return snake.direction

        head_x, head_y = snake.body[0]
        food_x, food_y = food

        # Elegir la dirección que más acerque a la comida
        best = valid[0]
        best_distance = 999999

        for d in valid:

            nx = head_x + d[0] * CELL_SIZE
            ny = head_y + d[1] * CELL_SIZE

            if self.wrap:

                if nx < 0:
                    nx = WIDTH - CELL_SIZE

                elif nx >= WIDTH:
                    nx = 0

                if ny < 0:
                    ny = HEIGHT - CELL_SIZE

                elif ny >= HEIGHT:
                    ny = 0

            distance = abs(food_x - nx) + abs(food_y - ny)

            if distance < best_distance:

                best_distance = distance
                best = d

        return best

    def is_safe(self, snake, enemy, direction):

        x, y = snake.body[0]

        nx = x + direction[0] * CELL_SIZE
        ny = y + direction[1] * CELL_SIZE

        # ---------- PAREDES ----------

        if self.wrap:

            if nx < 0:
                nx = WIDTH - CELL_SIZE

            elif nx >= WIDTH:
                nx = 0

            if ny < 0:
                ny = HEIGHT - CELL_SIZE

            elif ny >= HEIGHT:
                ny = 0

        else:

            if nx < 0:
                return False

            if ny < 0:
                return False

            if nx >= WIDTH:
                return False

            if ny >= HEIGHT:
                return False

        pos = (nx, ny)

        # ---------- CUERPO PROPIO ----------

        if pos in snake.body[:-1]:
            return False

        # ---------- ENEMIGO ----------

        if enemy is not None:

            if pos in enemy.body:
                return False

        return True