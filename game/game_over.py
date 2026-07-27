import pygame

from game.settings import *


class GameOver:


    def __init__(self):

        self.screen = pygame.display.get_surface()

        self.clock = pygame.time.Clock()


        self.big = pygame.font.SysFont(
            "arial",
            60,
            bold=True
        )


        self.font = pygame.font.SysFont(
            "arial",
            35
        )


        self.running = True

        self.result = None


        self.restart_button = None
        self.menu_button = None
        self.exit_button = None



    # ==================================
    # BOTON
    # ==================================

    def button(self,text,y):

        rect = pygame.Rect(
            WIDTH//2-180,
            y,
            360,
            60
        )


        mouse = pygame.mouse.get_pos()


        color = (160,120,70)


        if rect.collidepoint(mouse):

            color = (235,190,80)



        pygame.draw.rect(
            self.screen,
            color,
            rect,
            border_radius=12
        )


        pygame.draw.rect(
            self.screen,
            BLACK,
            rect,
            3,
            border_radius=12
        )


        img = self.font.render(
            text,
            True,
            BLACK
        )


        self.screen.blit(
            img,
            (
                rect.centerx-img.get_width()//2,
                rect.centery-img.get_height()//2
            )
        )


        return rect



    # ==================================
    # DIBUJAR
    # ==================================

    def draw(self,winner):


        self.screen.fill(
            (30,30,30)
        )


        title = self.big.render(
            winner,
            True,
            WHITE
        )


        self.screen.blit(
            title,
            (
                WIDTH//2-title.get_width()//2,
                80
            )
        )



        self.restart_button = self.button(
            "REINICIAR",
            250
        )


        self.menu_button = self.button(
            "MENU PRINCIPAL",
            340
        )


        self.exit_button = self.button(
            "SALIR",
            430
        )





    # ==================================
    # EVENTOS
    # ==================================

    def events(self,event):


        if event.type == pygame.MOUSEBUTTONDOWN:


            if event.button == 1:


                mouse = pygame.mouse.get_pos()



                if self.restart_button.collidepoint(mouse):

                    self.result = "restart"

                    self.running=False



                elif self.menu_button.collidepoint(mouse):

                    self.result = "menu"

                    self.running=False



                elif self.exit_button.collidepoint(mouse):

                    self.result = "exit"

                    self.running=False





        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_r:

                self.result="restart"

                self.running=False



            elif event.key == pygame.K_ESCAPE:

                self.result="exit"

                self.running=False





    # ==================================
    # RUN
    # ==================================

    def run(self,winner):


        self.running=True


        while self.running:


            self.clock.tick(60)



            for event in pygame.event.get():


                if event.type == pygame.QUIT:

                    pygame.quit()

                    raise SystemExit



                self.events(event)



            self.draw(winner)



            pygame.display.flip()



        return self.result