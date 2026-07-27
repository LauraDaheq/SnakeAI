from heapq import heappush, heappop

from game.settings import WIDTH, HEIGHT, CELL_SIZE


class AStarAI:

    def __init__(self, wrap=True):
        self.wrap = wrap

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(self, node):

        x, y = node

        moves = [
            (CELL_SIZE, 0),
            (-CELL_SIZE, 0),
            (0, CELL_SIZE),
            (0, -CELL_SIZE)
        ]

        result = []

        for dx, dy in moves:

            nx = x + dx
            ny = y + dy

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

                if nx < 0 or nx >= WIDTH:
                    continue

                if ny < 0 or ny >= HEIGHT:
                    continue

            result.append((nx, ny))

        return result

    def get_move(self, snake, enemy, food):

        start = snake.body[0]
        goal = food

        blocked = set(snake.body[:-1])

        if enemy:
            blocked.update(enemy.body)

        path = self.find_path(start, goal, blocked)

        if len(path) < 2:
            return snake.direction

        next_cell = path[1]

        dx = next_cell[0] - start[0]
        dy = next_cell[1] - start[1]

        # Corrección cuando atraviesa paredes

        if self.wrap:

            if dx > CELL_SIZE:
                dx = -CELL_SIZE

            elif dx < -CELL_SIZE:
                dx = CELL_SIZE

            if dy > CELL_SIZE:
                dy = -CELL_SIZE

            elif dy < -CELL_SIZE:
                dy = CELL_SIZE

        if dx > 0:
            return (1, 0)

        if dx < 0:
            return (-1, 0)

        if dy > 0:
            return (0, 1)

        return (0, -1)

    def find_path(self, start, goal, blocked):

        frontier = []

        heappush(frontier, (0, start))

        came_from = {}

        cost_so_far = {}

        came_from[start] = None
        cost_so_far[start] = 0

        while frontier:

            _, current = heappop(frontier)

            if current == goal:
                break

            for nxt in self.neighbors(current):

                if nxt in blocked and nxt != goal:
                    continue

                new_cost = cost_so_far[current] + 1

                if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:

                    cost_so_far[nxt] = new_cost

                    priority = new_cost + self.heuristic(goal, nxt)

                    heappush(frontier, (priority, nxt))

                    came_from[nxt] = current

        if goal not in came_from:
            return [start]

        path = []

        node = goal

        while node is not None:

            path.append(node)

            node = came_from[node]

        path.reverse()

        return path