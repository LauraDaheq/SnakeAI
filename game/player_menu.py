import pygame


class PlayerMenu:


    def __init__(self):

        self.screen = pygame.display.get_surface()


        self.font_title = pygame.font.SysFont(
            "arial",
            65,
            bold=True
        )


        self.font = pygame.font.SysFont(
            "arial",
            32
        )


        self.small_font = pygame.font.SysFont(
            "arial",
            22
        )


        self.name = ""


        self.colors = [

            ("Verde",(45,220,60)),

            ("Azul",(40,120,255)),

            ("Rojo",(230,50,50)),

            ("Rosa",(255,150,180))

        ]


        self.color_selected = 1


        self.running = True





    def button(
        self,
        text,
        rect,
        mouse
    ):


        if rect.collidepoint(mouse):

            color=(90,90,100)

        else:

            color=(55,55,65)



        pygame.draw.rect(
            self.screen,
            color,
            rect,
            border_radius=18
        )


        pygame.draw.rect(
            self.screen,
            (220,220,220),
            rect,
            2,
            border_radius=18
        )


        label=self.font.render(
            text,
            True,
            (255,255,255)
        )


        self.screen.blit(
            label,
            (
                rect.centerx-label.get_width()/2,
                rect.centery-label.get_height()/2
            )
        )





    def run(self):


        clock=pygame.time.Clock()



        while self.running:


            mouse=pygame.mouse.get_pos()



            for event in pygame.event.get():



                if event.type == pygame.QUIT:

                    pygame.quit()
                    exit()



                if event.type == pygame.KEYDOWN:


                    if event.key == pygame.K_BACKSPACE:


                        self.name=self.name[:-1]



                    elif len(self.name)<12:


                        if event.unicode.isprintable():

                            self.name+=event.unicode





                if event.type == pygame.MOUSEBUTTONDOWN:



                    # colores

                    for i in range(4):


                        circle=pygame.Rect(

                            330+i*90,
                            340,
                            55,
                            55

                        )


                        if circle.collidepoint(event.pos):

                            self.color_selected=i





                    # continuar

                    button=pygame.Rect(

                        360,
                        540,
                        280,
                        75

                    )


                    if button.collidepoint(event.pos):


                        if self.name=="":

                            self.name="Jugador 2"



                        self.running=False





            # ----------------
            # DIBUJO
            # ----------------


            self.screen.fill(
                (20,80,55)
            )



            pygame.draw.rect(
                self.screen,
                (30,30,40),
                pygame.Rect(
                    160,
                    40,
                    680,
                    620
                ),
                border_radius=35
            )



            title=self.font_title.render(
                "JUGADOR 2",
                True,
                (255,255,255)
            )


            self.screen.blit(
                title,
                (
                    330,
                    80
                )
            )




            txt=self.font.render(
                "Nombre",
                True,
                (255,255,255)
            )


            self.screen.blit(
                txt,
                (
                    240,
                    190
                )
            )



            pygame.draw.rect(
                self.screen,
                (55,55,65),
                pygame.Rect(
                    240,
                    235,
                    420,
                    55
                ),
                border_radius=12
            )



            name=self.font.render(
                self.name,
                True,
                self.colors[self.color_selected][1]
            )


            self.screen.blit(
                name,
                (
                    260,
                    245
                )
            )





            color_text=self.font.render(
                "Color",
                True,
                (255,255,255)
            )


            self.screen.blit(
                color_text,
                (
                    240,
                    315
                )
            )




            for i,c in enumerate(self.colors):


                x=340+i*90


                pygame.draw.circle(
                    self.screen,
                    c[1],
                    (
                        x,
                        360
                    ),
                    25
                )



                if i==self.color_selected:


                    pygame.draw.circle(
                        self.screen,
                        (255,255,255),
                        (
                            x,
                            360
                        ),
                        33,
                        3
                    )



                label=self.small_font.render(
                    c[0],
                    True,
                    (255,255,255)
                )


                self.screen.blit(
                    label,
                    (
                        x-label.get_width()/2,
                        400
                    )
                )





            # vista previa

            color=self.colors[self.color_selected][1]


            pygame.draw.circle(
                self.screen,
                color,
                (620,470),
                18
            )


            pygame.draw.circle(
                self.screen,
                color,
                (590,470),
                15
            )





            self.button(
                "CONTINUAR",
                pygame.Rect(
                    360,
                    540,
                    280,
                    75
                ),
                mouse
            )





            pygame.display.update()


            clock.tick(60)





        return (

            self.name,

            self.colors[self.color_selected][1]

        )