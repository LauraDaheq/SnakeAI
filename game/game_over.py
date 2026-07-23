import pygame


class GameOver:


    def __init__(self):

        self.screen = pygame.display.get_surface()


        self.width = self.screen.get_width()
        self.height = self.screen.get_height()


        self.title_font = pygame.font.SysFont(
            "arial",
            75,
            bold=True
        )


        self.font = pygame.font.SysFont(
            "arial",
            35
        )



    # -------------------------
    # BOTON
    # -------------------------

    def draw_button(
        self,
        text,
        rect,
        mouse
    ):


        if rect.collidepoint(mouse):

            color = (90,90,100)

        else:

            color = (50,50,60)



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
                rect.centerx - label.get_width()/2,
                rect.centery - label.get_height()/2
            )
        )





    # -------------------------
    # PANTALLA GAME OVER
    # -------------------------

    def run(
        self,
        winner_text
    ):


        clock = pygame.time.Clock()



        while True:



            mouse = pygame.mouse.get_pos()



            for event in pygame.event.get():


                if event.type == pygame.QUIT:

                    pygame.quit()
                    exit()



                if event.type == pygame.MOUSEBUTTONDOWN:



                    restart_button = pygame.Rect(

                        260,
                        480,
                        220,
                        75

                    )



                    menu_button = pygame.Rect(

                        520,
                        480,
                        220,
                        75

                    )



                    if restart_button.collidepoint(
                        event.pos
                    ):

                        return "restart"




                    if menu_button.collidepoint(
                        event.pos
                    ):

                        return "menu"






            # -----------------
            # DIBUJO
            # -----------------


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
                    100,
                    700,
                    500

                ),

                border_radius=35

            )




            title = self.title_font.render(

                "GAME OVER",

                True,

                (255,80,80)

            )


            self.screen.blit(

                title,

                (

                    260,
                    170

                )

            )





            winner = self.font.render(

                winner_text,

                True,

                (255,255,255)

            )


            self.screen.blit(

                winner,

                (

                    500 - winner.get_width()/2,

                    300

                )

            )





            self.draw_button(

                "REINICIAR",

                pygame.Rect(

                    260,
                    480,
                    220,
                    75

                ),

                mouse

            )




            self.draw_button(

                "MENU",

                pygame.Rect(

                    520,
                    480,
                    220,
                    75

                ),

                mouse

            )





            pygame.display.update()



            clock.tick(60)