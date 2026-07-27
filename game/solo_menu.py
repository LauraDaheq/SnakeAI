import pygame
from game.settings import *


class SoloMenu:


    def __init__(self):

        self.screen = pygame.display.get_surface()

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont(
            "arial",
            35
        )

        self.title_font = pygame.font.SysFont(
            "arial",
            55,
            bold=True
        )

        self.running=True

        self.result=None

        self.buttons=[]


        self.modes=[

            "Humano solo",

            "IA sola"

        ]



    def draw(self):

        self.screen.fill(
            (100,72,46)
        )


        title=self.title_font.render(
            "JUGAR SOLO",
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


        self.buttons=[]


        y=250


        for mode in self.modes:


            rect=pygame.Rect(
                WIDTH//2-220,
                y,
                440,
                60
            )


            pygame.draw.rect(
                self.screen,
                (160,120,70),
                rect,
                border_radius=12
            )


            img=self.font.render(
                mode,
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


            self.buttons.append(
                (
                    rect,
                    mode
                )
            )


            y+=100



    def run(self):


        while self.running:


            self.clock.tick(60)


            for event in pygame.event.get():


                if event.type==pygame.QUIT:

                    pygame.quit()
                    raise SystemExit


                if event.type==pygame.MOUSEBUTTONDOWN:


                    for rect,mode in self.buttons:


                        if rect.collidepoint(
                            pygame.mouse.get_pos()
                        ):

                            self.result=mode

                            self.running=False



            self.draw()

            pygame.display.flip()



        return self.result