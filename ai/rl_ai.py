import random

from ai.base_ai import BaseAI


class RLAgent(BaseAI):

    def __init__(self):

        self.actions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]


    def get_move(self, snake, enemy, food):

        valid = []

        opposite = (
            -snake.direction[0],
            -snake.direction[1]
        )

        for action in self.actions:

            if action != opposite:

                valid.append(action)

        return random.choice(valid)