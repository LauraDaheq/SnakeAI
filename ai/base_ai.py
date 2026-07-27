class BaseAI:

    def get_move(self, snake, enemy, food):
        """
        Debe devolver una dirección:

        (1,0)
        (-1,0)
        (0,1)
        (0,-1)
        """
        raise NotImplementedError