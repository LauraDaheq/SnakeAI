import pygame
import random

from game.snake import Snake
from game.menu import Menu
from game.player_menu import PlayerMenu
from game.game_over import GameOver


pygame.init()


# =====================
# CONFIGURACIÓN
# =====================

WIDTH = 1000
HEIGHT = 700
CELL_SIZE = 25


screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
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
# CREAR COMIDA
# =====================

def create_food():

    x = random.randrange(
        0,
        WIDTH // CELL_SIZE
    ) * CELL_SIZE


    y = random.randrange(
        0,
        HEIGHT // CELL_SIZE
    ) * CELL_SIZE


    return (x,y)




# =====================
# DIBUJAR MANZANA
# =====================

def draw_food(screen, food):

    x = food[0] + CELL_SIZE//2
    y = food[1] + CELL_SIZE//2


    # sombra

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


    # cuerpo

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


    # brillo

    pygame.draw.circle(
        screen,
        (255,170,170),
        (x-5,y-5),
        3
    )


    # tallo

    pygame.draw.line(
        screen,
        (90,50,20),
        (x,y-11),
        (x+3,y-18),
        3
    )


    # hoja

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


    name1,color1,mode = menu.run()



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



    snake2=None



    if mode == "Multijugador":


        menu2=PlayerMenu()


        name2,color2=menu2.run()



        snake2=Snake(
            name=name2,
            color=color2
        )



        snake2.body=[

            (700,400),
            (725,400),
            (750,400),
            (775,400),
            (800,400)

        ]


        snake2.direction=(-1,0)




    food=create_food()


    FPS=7


    return snake1,snake2,food,FPS





# =====================
# PARTIDA
# =====================


snake1,snake2,food,FPS=start_game()


running=True



while running:



    # =====================
    # EVENTOS
    # =====================

    for event in pygame.event.get():


        if event.type == pygame.QUIT:

            running=False



        if event.type == pygame.KEYDOWN:



            # jugador 1 WASD

            if event.key == pygame.K_d:
                snake1.change_direction((1,0))

            elif event.key == pygame.K_a:
                snake1.change_direction((-1,0))

            elif event.key == pygame.K_w:
                snake1.change_direction((0,-1))

            elif event.key == pygame.K_s:
                snake1.change_direction((0,1))





            # jugador 2 flechas

            if snake2:


                if event.key == pygame.K_RIGHT:
                    snake2.change_direction((1,0))

                elif event.key == pygame.K_LEFT:
                    snake2.change_direction((-1,0))

                elif event.key == pygame.K_UP:
                    snake2.change_direction((0,-1))

                elif event.key == pygame.K_DOWN:
                    snake2.change_direction((0,1))






    # =====================
    # ACTUALIZAR
    # =====================


    snake1.move()


    if snake1.check_collision():

        pass



    if snake2:


        snake2.move()


        snake2.check_collision()





    # comer


    if snake1.alive and snake1.body[0] == food:

        snake1.grow()

        food=create_food()



    if snake2 and snake2.alive and snake2.body[0] == food:

        snake2.grow()

        food=create_food()





    # choque jugadores


    if snake2:


        if snake1.body[0] in snake2.body:

            snake1.die()


        if snake2.body[0] in snake1.body:

            snake2.die()






    # =====================
    # GAME OVER
    # =====================


    if not snake1.alive or (snake2 and not snake2.alive):


        if snake2:


            if snake1.alive:

                winner=f"{snake1.name} gana"


            elif snake2.alive:

                winner=f"{snake2.name} gana"


            else:

                winner="Empate"



        else:

            winner=f"{snake1.name} perdió"



        over=GameOver()


        result=over.run(winner)



        if result:

            snake1,snake2,food,FPS=start_game()






    # =====================
    # DIBUJAR
    # =====================


    screen.fill(
        (110,82,52)
    )



    # cuadricula

    for x in range(0,WIDTH,CELL_SIZE):

        pygame.draw.line(
            screen,
            (130,100,70),
            (x,0),
            (x,HEIGHT)
        )


    for y in range(0,HEIGHT,CELL_SIZE):

        pygame.draw.line(
            screen,
            (130,100,70),
            (0,y),
            (WIDTH,y)
        )



    draw_food(
        screen,
        food
    )


    snake1.draw(screen)



    if snake2:

        snake2.draw(screen)




    # puntos


    text=font.render(
        f"{snake1.name}: {snake1.score}",
        True,
        (255,255,255)
    )


    screen.blit(
        text,
        (20,20)
    )



    if snake2:

        text2=font.render(
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
        int(FPS)
    )



pygame.quit()