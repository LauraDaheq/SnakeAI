from game.settings import (
    WIDTH,
    HEIGHT,
    CELL_SIZE
)


class AIController:

    def __init__(self):
        self.last_move = None


    # ======================================
    # ELEGIR MOVIMIENTO
    # ======================================

    def get_move(self, snake, enemy, food, walls):

        movimientos = [

            (1, 0),    # derecha
            (-1, 0),   # izquierda
            (0, 1),    # abajo
            (0, -1)    # arriba

        ]


        mejor_movimiento = None
        mejor_puntaje = -999999



        for movimiento in movimientos:


            # Evitar devolverse

            if movimiento == (
                -snake.direction[0],
                -snake.direction[1]
            ):
                continue



            cabeza = snake.body[0]


            nueva_posicion = (

                cabeza[0] + movimiento[0] * CELL_SIZE,

                cabeza[1] + movimiento[1] * CELL_SIZE

            )



            # Si es una posición mortal, ignorar

            if not self.safe(
                nueva_posicion,
                snake,
                enemy,
                walls
            ):
                continue



            puntaje = 0



            # =================================
            # 1. BUSCAR ESPACIO PARA SOBREVIVIR
            # =================================

            espacio = self.calculate_space(

                nueva_posicion,

                snake,

                enemy,

                walls

            )


            puntaje += espacio * 30



            # =================================
            # 2. EVITAR ENEMIGO
            # =================================

            if enemy is not None:


                enemigo_futuro = self.predict_enemy(
                    enemy
                )


                if nueva_posicion == enemigo_futuro:

                    puntaje -= 2000



                distancia_enemy = self.distance(

                    nueva_posicion,

                    enemy.body[0]

                )


                if distancia_enemy < CELL_SIZE * 5:

                    puntaje -= 500



            # =================================
            # 3. ATAQUE SI ES GRANDE
            # =================================

            if enemy is not None:


                if snake.score >= 3:


                    distancia_enemy = self.distance(

                        nueva_posicion,

                        enemy.body[0]

                    )


                    if distancia_enemy < CELL_SIZE * 10:

                        puntaje += 700



            # =================================
            # 4. COMIDA
            # =================================

            distancia_comida = self.distance(

                nueva_posicion,

                food

            )


            # La comida ayuda pero no manda

            puntaje += max(
                0,
                800 - distancia_comida
            )



            # Elegir mejor opción

            if puntaje > mejor_puntaje:

                mejor_puntaje = puntaje

                mejor_movimiento = movimiento



        return mejor_movimiento



    # ======================================
    # DISTANCIA
    # ======================================

    def distance(self, a, b):

        return abs(
            a[0] - b[0]
        ) + abs(
            a[1] - b[1]
        )



    # ======================================
    # SIGUIENTE POSICIÓN
    # ======================================

    def next_position(self, head, direction):

        x, y = head

        dx, dy = direction


        return (

            x + dx * CELL_SIZE,

            y + dy * CELL_SIZE

        )



    # ======================================
    # COMPROBAR SI ES SEGURO
    # ======================================

    def safe(self, pos, snake, enemy, walls):

        x, y = pos


        # Bordes

        if x < 0 or x >= WIDTH:

            return False


        if y < 0 or y >= HEIGHT:

            return False



        # Paredes

        if pos in walls:

            return False



        # Cuerpo propio

        if pos in snake.body[:-1]:

            return False



        # Cuerpo enemigo

        if enemy is not None:

            if pos in enemy.body:

                return False



        return True



    # ======================================
    # CALCULAR ESPACIO DISPONIBLE
    # ======================================

    def calculate_space(self, start, snake, enemy, walls):


        visitados = set()

        cola = [start]



        while cola:


            posicion = cola.pop(0)



            if posicion in visitados:

                continue



            if not self.safe(

                posicion,

                snake,

                enemy,

                walls

            ):

                continue



            visitados.add(posicion)



            x, y = posicion



            vecinos = [

                (
                    x + CELL_SIZE,
                    y
                ),

                (
                    x - CELL_SIZE,
                    y
                ),

                (
                    x,
                    y + CELL_SIZE
                ),

                (
                    x,
                    y - CELL_SIZE
                )

            ]



            cola.extend(vecinos)



        return len(visitados)



    # ======================================
    # PREDECIR ENEMIGO
    # ======================================

    def predict_enemy(self, enemy):


        if enemy is None:

            return None



        cabeza = enemy.body[0]

        dx, dy = enemy.direction



        return (

            cabeza[0] + dx * CELL_SIZE,

            cabeza[1] + dy * CELL_SIZE

        )