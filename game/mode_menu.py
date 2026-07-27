import pygame
from game.settings import *


class ModeMenu:

    def __init__(self):

        self.screen = pygame.display.get_surface()

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont(
            "arial",
            35
        )

        self.title_font = pygame.font.SysFont(
            "arial",
            60,
            bold=True
        )

        self.running = True
        self.result = None

        self.buttons = []

        self.modes = [
            "Solo",
            "Duo"
        ]


    def draw_background(self):

        self.screen.fill(
            (100,72,46)
        )


    def draw_button(self,text,y):

        rect = pygame.Rect(
            WIDTH//2-200,
            y,
            400,
            60
        )


        pygame.draw.rect(
            self.screen,
            (160,120,70),
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



    def draw(self):

        self.draw_background()


        title = self.title_font.render(
            "MODO",
            True,
            WHITE
        )


        self.screen.blit(
            title,
            (
                WIDTH//2-title.get_width()//2,
                70
            )
        )


        self.buttons=[]


        y=250


        for mode in self.modes:


            rect=self.draw_button(
                mode,
                y
            )


            self.buttons.append(
                (
                    rect,
                    mode
                )
            )


            y+=100




    def events(self,event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button==1:


                mouse=pygame.mouse.get_pos()


                for rect,mode in self.buttons:


                    if rect.collidepoint(mouse):

                        self.result=mode

                        self.running=False




    def run(self):

        self.running=True


        while self.running:


            self.clock.tick(60)


            for event in pygame.event.get():


                if event.type == pygame.QUIT:

                    pygame.quit()
                    raise SystemExit


                self.events(event)



            self.draw()


            pygame.display.flip()



        return self.result