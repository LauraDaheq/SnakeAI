import pygame
from game.settings import *


class DifficultyMenu:


    def __init__(self):

        self.screen = pygame.display.get_surface()

        self.clock = pygame.time.Clock()


        self.title_font = pygame.font.SysFont(
            "arial",
            60,
            bold=True
        )


        self.font = pygame.font.SysFont(
            "arial",
            32
        )


        self.small = pygame.font.SysFont(
            "arial",
            22
        )


        self.running = True

        self.result = None


        self.buttons=[]


        self.difficulties=[

            "Facil",

            "Intermedio",

            "Dificil"

        ]



    # ==========================
    # FONDO
    # ==========================

    def background(self):

        self.screen.fill(
            (100,72,46)
        )


        for x in range(
            0,
            WIDTH,
            CELL_SIZE
        ):

            pygame.draw.line(
                self.screen,
                (118,88,58),
                (x,0),
                (x,HEIGHT)
            )


        for y in range(
            0,
            HEIGHT,
            CELL_SIZE
        ):

            pygame.draw.line(
                self.screen,
                (118,88,58),
                (0,y),
                (WIDTH,y)
            )



    # ==========================
    # TITULO
    # ==========================

    def title(self,text):

        img=self.title_font.render(
            text,
            True,
            WHITE
        )


        self.screen.blit(
            img,
            (
                WIDTH//2-img.get_width()//2,
                70
            )
        )



    # ==========================
    # BOTON
    # ==========================

    def button(self,text,y):


        rect=pygame.Rect(

            WIDTH//2-200,

            y,

            400,

            65

        )


        mouse=pygame.mouse.get_pos()


        color=(160,120,70)


        if rect.collidepoint(mouse):

            color=(235,190,80)



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


        img=self.font.render(
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



    # ==========================
    # DIBUJAR
    # ==========================

    def draw(self):

        self.background()


        self.title(
            "DIFICULTAD"
        )


        self.buttons=[]


        y=220


        for diff in self.difficulties:


            rect=self.button(
                diff,
                y
            )


            self.buttons.append(
                (
                    rect,
                    diff
                )
            )


            y+=90



        info=self.small.render(

            "Selecciona una dificultad",

            True,

            WHITE

        )


        self.screen.blit(
            info,
            (
                WIDTH//2-info.get_width()//2,
                HEIGHT-50
            )
        )



    # ==========================
    # EVENTOS
    # ==========================

    def events(self,event):


        if event.type == pygame.MOUSEBUTTONDOWN:


            if event.button == 1:


                mouse=pygame.mouse.get_pos()



                for rect,diff in self.buttons:


                    if rect.collidepoint(mouse):


                        self.result=diff

                        self.running=False





    # ==========================
    # RUN
    # ==========================

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