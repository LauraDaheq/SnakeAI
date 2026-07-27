import pygame
import random


from game.snake import Snake
from game.menu import Menu
from game.game_over import GameOver
from game.ai_snake import AIController



pygame.init()


# =====================
# CONFIGURACIÓN
# =====================

WIDTH = 1000
HEIGHT = 700

CELL_SIZE = 25


screen = pygame.display.set_mode(
    (
        WIDTH,
        HEIGHT
    )
)


pygame.display.set_caption(
    "Snake AI"
)


clock = pygame.time.Clock()


font = pygame.font.SysFont(
    "arial",
    30
)



# =====================
# CREAR PAREDES
# =====================


def create_walls(amount, forbidden=None):

    if forbidden is None:
        forbidden = []


    walls = []


    while len(walls) < amount:


        x = random.randrange(
            0,
            WIDTH // CELL_SIZE
        ) * CELL_SIZE


        y = random.randrange(
            0,
            HEIGHT // CELL_SIZE
        ) * CELL_SIZE



        pos = (
            x,
            y
        )


        if (
            pos not in forbidden
            and pos not in walls
        ):

            walls.append(pos)


    return walls





# =====================
# DIBUJAR PAREDES
# =====================


def draw_walls(screen, walls):


    for wall in walls:


        pygame.draw.rect(
            screen,
            (70,70,70),
            (
                wall[0],
                wall[1],
                CELL_SIZE,
                CELL_SIZE
            )
        )


        pygame.draw.rect(
            screen,
            (150,150,150),
            (
                wall[0]+3,
                wall[1]+3,
                CELL_SIZE-6,
                CELL_SIZE-6
            )
        )





# =====================
# COLISIÓN PARED
# =====================


def check_wall_collision(
    snake,
    walls
):

    if snake.body[0] in walls:

        snake.die()






# =====================
# CREAR COMIDA
# =====================


def create_food(
    walls,
    snakes
):

    while True:


        x = random.randrange(
            0,
            WIDTH // CELL_SIZE
        ) * CELL_SIZE


        y = random.randrange(
            0,
            HEIGHT // CELL_SIZE
        ) * CELL_SIZE



        food = (
            x,
            y
        )



        occupied = []


        for snake in snakes:

            occupied += snake.body




        if (
            food not in walls
            and food not in occupied
        ):

            return food






# =====================
# DIBUJAR COMIDA
# =====================


def draw_food(
    screen,
    food
):

    x = food[0] + CELL_SIZE//2

    y = food[1] + CELL_SIZE//2



    pygame.draw.ellipse(
        screen,
        (120,20,20),
        pygame.Rect(
            x-9,
            y+7,
            18,
            5
        )
    )



    pygame.draw.ellipse(
        screen,
        (220,40,40),
        pygame.Rect(
            x-10,
            y-11,
            20,
            22
        )
    )



    pygame.draw.circle(
        screen,
        (255,170,170),
        (
            x-5,
            y-5
        ),
        3
    )



    pygame.draw.line(
        screen,
        (90,50,20),
        (
            x,
            y-11
        ),
        (
            x+3,
            y-18
        ),
        3
    )


    pygame.draw.ellipse(
        screen,
        (40,180,60),
        pygame.Rect(
            x+2,
            y-18,
            8,
            5
        )
    )

# =====================
# INICIAR PARTIDA
# =====================


def start_game():


    menu = Menu()


    name1, color1, mode, difficulty = menu.run()



    # =====================
    # DIFICULTAD
    # =====================


    if difficulty == "Facil":

        FPS = 8
        wall_amount = 15


    elif difficulty == "Intermedio":

        FPS = 12
        wall_amount = 40


    elif difficulty == "Dificil":

        FPS = 15
        wall_amount = 70


    else:

        FPS = 10
        wall_amount = 25





    # =====================
    # CREAR SNAKE 1
    # =====================


    snake1 = Snake(
        name=name1,
        color=color1
    )


    snake1.body = [

        (300,300),
        (275,300),
        (250,300),
        (225,300),
        (200,300)

    ]


    snake2 = None



    ai1 = None
    ai2 = None





    # =====================
    # JUGAR SOLO HUMANO
    # =====================

    if mode == "Humano solo":

        snake1.controller = "human"

        snake2 = None



    # =====================
    # JUGAR SOLO IA
    # =====================

    elif mode == "IA sola":

        snake1.controller = "ai"

        ai1 = AIController()

        snake1.ai = ai1

        snake2 = None






    # =====================
    # HUMANO VS HUMANO
    # =====================


    elif mode == "Humano vs Humano":



        snake2 = Snake(
            name="Jugador 2",
            color=(40,120,255)
        )


        snake2.body = [

            (700,400),
            (725,400),
            (750,400),
            (775,400),
            (800,400)

        ]


        snake2.direction = (-1,0)






    # =====================
    # HUMANO VS IA
    # =====================


    elif mode == "Humano vs IA":



        snake2 = Snake(

            name="IA",

            color=(230,50,50),

            controller="ai"

        )


        snake2.body = [

            (700,400),
            (725,400),
            (750,400),
            (775,400),
            (800,400)

        ]



        snake2.direction = (-1,0)



        ai2 = AIController()


        snake2.ai = ai2







    # =====================
    # IA VS IA
    # =====================


    elif mode == "IA vs IA":



        snake1.controller = "ai"



        ai1 = AIController()


        snake1.ai = ai1






        snake2 = Snake(

            name="IA 2",

            color=(230,50,50),

            controller="ai"

        )



        snake2.body = [

            (700,400),
            (725,400),
            (750,400),
            (775,400),
            (800,400)

        ]



        snake2.direction = (-1,0)



        ai2 = AIController()


        snake2.ai = ai2





    # =====================
    # PAREDES
    # =====================


    forbidden = list(
        snake1.body
    )



    if snake2:

        forbidden += snake2.body




    walls = create_walls(

        wall_amount,

        forbidden

    )





    # =====================
    # COMIDA
    # =====================


    snakes = [

        snake1

    ]



    if snake2:

        snakes.append(
            snake2
        )



    food = create_food(

        walls,

        snakes

    )




    return (

        snake1,

        snake2,

        food,

        walls,

        FPS,

        ai1,

        ai2

    )

# =====================
# CREAR PARTIDA
# =====================


snake1, snake2, food, walls, FPS, ai1, ai2 = start_game()



running = True




# =====================
# LOOP PRINCIPAL
# =====================


while running:


    # =====================
    # EVENTOS
    # =====================


    for event in pygame.event.get():


        if event.type == pygame.QUIT:

            running = False



        if event.type == pygame.KEYDOWN:


            # =====================
            # JUGADOR 1
            # =====================


            if snake1.controller == "human":


                if event.key == pygame.K_d:

                    snake1.change_direction(
                        (1,0)
                    )


                elif event.key == pygame.K_a:

                    snake1.change_direction(
                        (-1,0)
                    )


                elif event.key == pygame.K_w:

                    snake1.change_direction(
                        (0,-1)
                    )


                elif event.key == pygame.K_s:

                    snake1.change_direction(
                        (0,1)
                    )




            # =====================
            # JUGADOR 2
            # =====================


            if snake2 and snake2.controller == "human":


                if event.key == pygame.K_RIGHT:

                    snake2.change_direction(
                        (1,0)
                    )


                elif event.key == pygame.K_LEFT:

                    snake2.change_direction(
                        (-1,0)
                    )


                elif event.key == pygame.K_UP:

                    snake2.change_direction(
                        (0,-1)
                    )


                elif event.key == pygame.K_DOWN:

                    snake2.change_direction(
                        (0,1)
                    )





    # =====================
    # IA PIENSA
    # =====================


    if snake1.alive and snake1.controller == "ai":


        snake1.update_ai(

            snake2,

            food,

            walls

        )




    if snake2 and snake2.alive and snake2.controller == "ai":


        snake2.update_ai(

            snake1,

            food,

            walls

        )






    # =====================
    # MOVIMIENTO
    # =====================


    if snake1.alive:

        snake1.move()



    if snake2 and snake2.alive:

        snake2.move()






    # =====================
    # PAREDES
    # =====================


    if snake1.alive:

        check_wall_collision(

            snake1,

            walls

        )



    if snake2 and snake2.alive:

        check_wall_collision(

            snake2,

            walls

        )






    # =====================
    # COLISION CUERPO
    # =====================


    snake1.check_collision()



    if snake2:

        snake2.check_collision()





    # =====================
    # COMIDA SNAKE 1
    # =====================


    if snake1.alive and snake1.body[0] == food:


        snake1.grow()



        food = create_food(

            walls,

            [

                snake1

            ]
            +
            (
                [snake2]

                if snake2

                else []

            )

        )







    # =====================
    # COMIDA SNAKE 2
    # =====================


    if snake2 and snake2.alive and snake2.body[0] == food:


        snake2.grow()



        food = create_food(

            walls,

            [

                snake1,

                snake2

            ]

        )







    # =====================
    # CHOQUE ENTRE SNAKES
    # =====================


    if snake2:

        cabeza1 = snake1.body[0]

        cabeza2 = snake2.body[0]


        if cabeza1 == cabeza2:

            snake1.die()
            snake2.die()


        elif cabeza1 in snake2.body:

            snake1.die()


        elif cabeza2 in snake1.body:

            snake2.die()

    # =====================
    # GAME OVER
    # =====================


    if (

        not snake1.alive

        or

        (snake2 and not snake2.alive)

    ):



        if snake2:


            if snake1.alive:

                winner = f"{snake1.name} gana"


            elif snake2.alive:

                winner = f"{snake2.name} gana"


            else:

                winner = "Empate"



        else:


            winner = f"{snake1.name} perdió"





        over = GameOver()


        option = over.run(
            winner
        )


        if option == "restart":

            snake1, snake2, food, walls, FPS, ai1, ai2 = start_game()


        elif option == "menu":

            snake1, snake2, food, walls, FPS, ai1, ai2 = start_game()


        elif option == "exit":

            running = False

    # =====================
    # DIBUJO
    # =====================


    screen.fill(
        (110,82,52)
    )



    # =====================
    # CUADRÍCULA
    # =====================


    for x in range(
        0,
        WIDTH,
        CELL_SIZE
    ):


        pygame.draw.line(
            screen,
            (130,100,70),
            (x,0),
            (x,HEIGHT)
        )




    for y in range(
        0,
        HEIGHT,
        CELL_SIZE
    ):


        pygame.draw.line(
            screen,
            (130,100,70),
            (0,y),
            (WIDTH,y)
        )





    # =====================
    # DIBUJAR ELEMENTOS
    # =====================


    draw_walls(
        screen,
        walls
    )



    draw_food(
        screen,
        food
    )



    snake1.draw(
        screen
    )



    if snake2:

        snake2.draw(
            screen
        )





    # =====================
    # PUNTAJES
    # =====================


    text = font.render(

        f"{snake1.name}: {snake1.score}",

        True,

        (255,255,255)

    )


    screen.blit(
        text,
        (20,20)
    )





    if snake2:


        text2 = font.render(

            f"{snake2.name}: {snake2.score}",

            True,

            (255,255,255)

        )


        screen.blit(

            text2,

            (750,20)

        )






    pygame.display.update()



    clock.tick(
        FPS
    )





pygame.quit()