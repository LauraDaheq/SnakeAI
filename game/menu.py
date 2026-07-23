import pygame


class Menu:


    def __init__(self):

        self.screen = pygame.display.get_surface()


        self.WIDTH = self.screen.get_width()
        self.HEIGHT = self.screen.get_height()



        self.title_font = pygame.font.SysFont(
            "arial",
            75,
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


        self.color_selected = 0


        self.mode = "Solo"


        self.running = True





    # ======================
    # BOTONES
    # ======================

    def draw_button(
        self,
        text,
        rect,
        mouse,
        selected=False
    ):


        if rect.collidepoint(mouse):

            color = (90,90,100)

        else:

            color = (55,55,65)



        if selected:

            color = (40,130,70)



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



        label = self.font.render(
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





    # ======================
    # MENU PRINCIPAL
    # ======================

    def run(self):


        clock = pygame.time.Clock()



        while self.running:


            mouse = pygame.mouse.get_pos()



            for event in pygame.event.get():



                if event.type == pygame.QUIT:

                    pygame.quit()
                    exit()




                # teclado nombre

                if event.type == pygame.KEYDOWN:


                    if event.key == pygame.K_BACKSPACE:


                        self.name = self.name[:-1]



                    elif event.key == pygame.K_RETURN:


                        if self.name == "":

                            self.name="Jugador"


                        self.running=False



                    elif len(self.name)<12:


                        if event.unicode.isprintable():

                            self.name += event.unicode





                # clicks

                if event.type == pygame.MOUSEBUTTONDOWN:



                    # colores

                    for i in range(4):


                        circle = pygame.Rect(

                            320+i*90,
                            330,
                            55,
                            55
                        )



                        if circle.collidepoint(event.pos):

                            self.color_selected=i





                    # modo

                    solo_button = pygame.Rect(
                        250,
                        470,
                        220,
                        65
                    )


                    multi_button = pygame.Rect(
                        530,
                        470,
                        220,
                        65
                    )



                    if solo_button.collidepoint(event.pos):

                        self.mode="Solo"



                    if multi_button.collidepoint(event.pos):

                        self.mode="Multijugador"





                    # jugar

                    play_button = pygame.Rect(
                        360,
                        570,
                        280,
                        75
                    )



                    if play_button.collidepoint(event.pos):


                        if self.name=="":

                            self.name="Jugador"



                        self.running=False





            # ======================
            # DIBUJO
            # ======================


            # fondo

            self.screen.fill(
                (20,80,55)
            )



            # panel

            pygame.draw.rect(
                self.screen,
                (30,30,40),
                pygame.Rect(
                    150,
                    25,
                    700,
                    650
                ),
                border_radius=35
            )




            # titulo

            title=self.title_font.render(
                "SNAKE AI",
                True,
                (255,255,255)
            )


            self.screen.blit(
                title,
                (
                    300,
                    60
                )
            )




            # nombre

            name_label=self.font.render(
                "Nombre",
                True,
                (255,255,255)
            )


            self.screen.blit(
                name_label,
                (
                    240,
                    170
                )
            )



            pygame.draw.rect(
                self.screen,
                (55,55,65),
                pygame.Rect(
                    240,
                    215,
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
                    225
                )
            )





            # colores

            color_text=self.font.render(
                "Color",
                True,
                (255,255,255)
            )


            self.screen.blit(
                color_text,
                (
                    240,
                    300
                )
            )



            for i,c in enumerate(self.colors):


                x=340+i*90
                y=345



                pygame.draw.circle(
                    self.screen,
                    c[1],
                    (x,y),
                    25
                )



                if i==self.color_selected:


                    pygame.draw.circle(
                        self.screen,
                        (255,255,255),
                        (x,y),
                        33,
                        3
                    )



                txt=self.small_font.render(
                    c[0],
                    True,
                    (255,255,255)
                )


                self.screen.blit(
                    txt,
                    (
                        x-txt.get_width()/2,
                        380
                    )
                )





            # preview serpiente

            preview=self.colors[self.color_selected][1]



            pygame.draw.circle(
                self.screen,
                preview,
                (700,335),
                18
            )


            pygame.draw.circle(
                self.screen,
                preview,
                (670,335),
                15
            )


            pygame.draw.circle(
                self.screen,
                preview,
                (645,335),
                12
            )





            # botones modo


            self.draw_button(
                "🐍 Solo",
                pygame.Rect(
                    250,
                    470,
                    220,
                    65
                ),
                mouse,
                self.mode=="Solo"
            )



            self.draw_button(
                "🐍🐍 Duo",
                pygame.Rect(
                    530,
                    470,
                    220,
                    65
                ),
                mouse,
                self.mode=="Multijugador"
            )





            self.draw_button(
                "JUGAR",
                pygame.Rect(
                    360,
                    570,
                    280,
                    75
                ),
                mouse
            )





            pygame.display.update()


            clock.tick(60)




        return (

            self.name,

            self.colors[self.color_selected][1],

            self.mode

        )