import pygame

from game.settings import WIDTH, HEIGHT, CELL_SIZE



class Snake:


    def __init__(self, name="Jugador", color=(45,220,60)):

        self.name = name
        self.color = color

        self.score = 0

        self.body = [
            (300,300),
            (275,300),
            (250,300),
            (225,300),
            (200,300)
        ]

        self.direction = (1,0)

        self.size = 24

        self.alive = True



    # =====================
    # MOVIMIENTO
    # =====================

    def move(self):

        if not self.alive:
            return


        x,y = self.body[0]

        dx,dy = self.direction


        new_x = x + dx * CELL_SIZE
        new_y = y + dy * CELL_SIZE



        # atravesar paredes

        if new_x >= WIDTH:
            new_x = 0

        elif new_x < 0:
            new_x = WIDTH - CELL_SIZE


        if new_y >= HEIGHT:
            new_y = 0

        elif new_y < 0:
            new_y = HEIGHT - CELL_SIZE



        self.body.insert(
            0,
            (new_x,new_y)
        )


        self.body.pop()





    # =====================
    # DIRECCION
    # =====================

    def change_direction(self,direction):

        opposite = (
            -self.direction[0],
            -self.direction[1]
        )


        if direction != opposite:

            self.direction = direction





    # =====================
    # CRECER
    # =====================

    def grow(self):

        self.body.append(
            self.body[-1]
        )

        self.score += 1





    # =====================
    # COLISION
    # =====================

    def check_collision(self):

        head = self.body[0]


        if head in self.body[1:]:

            self.die()

            return True


        return False




    def die(self):

        self.alive = False






    # =====================
    # DIBUJO GENERAL
    # =====================

    def draw(self,screen):

        self.draw_body(screen)

        self.draw_head(screen)

        self.draw_eyes(screen)

        self.draw_tongue(screen)





    # =====================
    # CUERPO
    # =====================

    def draw_body(self,screen):


        if self.alive:

            color = self.color

        else:

            color = (100,100,100)



        radius = self.size // 2



        # cuerpo redondo continuo

        for x,y in reversed(self.body[1:]):


            pygame.draw.circle(
                screen,
                color,
                (x,y),
                radius
            )



        # cola más pequeña


        tail_x,tail_y = self.body[-1]


        pygame.draw.circle(
            screen,
            color,
            (tail_x,tail_y),
            7
        )







    # =====================
    # CABEZA
    # =====================

    def draw_head(self,screen):


        x,y = self.body[0]


        if self.alive:

            color=self.color

        else:

            color=(100,100,100)



        pygame.draw.circle(
            screen,
            color,
            (x,y),
            self.size//2 + 4
        )



        # hocico

        dx,dy=self.direction


        pygame.draw.circle(
            screen,
            color,
            (
                x+dx*10,
                y+dy*10
            ),
            9
        )






    # =====================
    # OJOS
    # =====================

    def draw_eyes(self,screen):


        x,y=self.body[0]

        dx,dy=self.direction



        if dx == 1:

            eyes=[
                (x+8,y-7),
                (x+8,y+7)
            ]


        elif dx == -1:

            eyes=[
                (x-8,y-7),
                (x-8,y+7)
            ]


        elif dy == -1:

            eyes=[
                (x-7,y-8),
                (x+7,y-8)
            ]


        else:

            eyes=[
                (x-7,y+8),
                (x+7,y+8)
            ]



        for ex,ey in eyes:


            pygame.draw.circle(
                screen,
                (255,255,255),
                (ex,ey),
                5
            )


            pygame.draw.circle(
                screen,
                (0,0,0),
                (ex,ey),
                2
            )







    # =====================
    # LENGUA
    # =====================

    def draw_tongue(self,screen):


        if not self.alive:

            return



        x,y=self.body[0]

        dx,dy=self.direction



        start=(

            x+dx*18,

            y+dy*18

        )


        end=(

            x+dx*32,

            y+dy*32

        )



        pygame.draw.line(
            screen,
            (230,40,60),
            start,
            end,
            3
        )



        pygame.draw.line(
            screen,
            (230,40,60),
            end,
            (
                end[0]-dy*5,
                end[1]+dx*5
            ),
            2
        )


        pygame.draw.line(
            screen,
            (230,40,60),
            end,
            (
                end[0]+dy*5,
                end[1]-dx*5
            ),
            2
        )