import pygame

from game.settings import *
from game.difficulty_menu import DifficultyMenu
from game.mode_menu import ModeMenu
from game.solo_menu import SoloMenu
from game.duo_menu import DuoMenu


COLORS = [

    ("Verde", (40,210,70)),
    ("Azul", (80,180,255)),
    ("Rosado", (255,140,210)),
    ("Rojo", (235,60,60))

]


class Menu:


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
            34
        )


        self.small = pygame.font.SysFont(
            "arial",
            22
        )


        self.name = ""

        self.color_index = 0

        self.state = "main"

        self.running = True

        self.result = None


        self.play_button = None
        self.controls_button = None
        self.exit_button = None
        self.start_button = None



    # ==========================
    # FONDO
    # ==========================

    def draw_background(self):

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

    def draw_title(self,text):

        shadow = self.big.render(
            text,
            True,
            (30,30,30)
        )


        self.screen.blit(
            shadow,
            (
                WIDTH//2-shadow.get_width()//2+4,
                54
            )
        )


        title = self.big.render(
            text,
            True,
            WHITE
        )


        self.screen.blit(
            title,
            (
                WIDTH//2-title.get_width()//2,
                50
            )
        )



    # ==========================
    # BOTON
    # ==========================

    def draw_button(self,text,y):

        rect = pygame.Rect(
            WIDTH//2-180,
            y,
            360,
            60
        )


        color = (
            160,
            120,
            70
        )


        if rect.collidepoint(
            pygame.mouse.get_pos()
        ):

            color = (
                235,
                190,
                80
            )


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

    # ==========================
    # MENU PRINCIPAL
    # ==========================

    def draw_main(self):

        self.draw_background()


        self.draw_title(
            "SNAKE AI"
        )


        self.play_button = self.draw_button(
            "JUGAR",
            220
        )


        self.controls_button = self.draw_button(
            "CONTROLES",
            310
        )


        self.exit_button = self.draw_button(
            "SALIR",
            400
        )



    def handle_main(self,event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse = pygame.mouse.get_pos()


                if self.play_button.collidepoint(mouse):

                    self.state = "player"



                elif self.controls_button.collidepoint(mouse):

                    self.state = "controls"



                elif self.exit_button.collidepoint(mouse):

                    pygame.quit()

                    raise SystemExit




    # ==========================
    # MENU JUGADOR
    # ==========================

    def draw_player(self):

        self.draw_background()


        self.draw_title(
            "JUGADOR"
        )


        text = self.font.render(
            "Escribe tu nombre",
            True,
            WHITE
        )


        self.screen.blit(
            text,
            (
                WIDTH//2-text.get_width()//2,
                140
            )
        )


        box = pygame.Rect(
            WIDTH//2-170,
            200,
            340,
            55
        )


        pygame.draw.rect(
            self.screen,
            WHITE,
            box,
            border_radius=8
        )


        pygame.draw.rect(
            self.screen,
            BLACK,
            box,
            2,
            border_radius=8
        )


        name = self.font.render(
            self.name,
            True,
            BLACK
        )


        self.screen.blit(
            name,
            (
                box.x+10,
                box.y+10
            )
        )



        title = self.font.render(
            "Selecciona color",
            True,
            WHITE
        )


        self.screen.blit(
            title,
            (
                WIDTH//2-title.get_width()//2,
                300
            )
        )



        self.color_buttons=[]


        start_x = WIDTH//2-170


        for i,(name,color) in enumerate(COLORS):

            rect = pygame.Rect(
                start_x+i*90,
                360,
                55,
                55
            )


            self.color_buttons.append(rect)


            pygame.draw.rect(
                self.screen,
                color,
                rect,
                border_radius=10
            )


            if i == self.color_index:

                pygame.draw.rect(
                    self.screen,
                    YELLOW,
                    rect,
                    4,
                    border_radius=10
                )



        self.start_button = self.draw_button(
            "INICIAR",
            520
        )



    def handle_player(self,event):


        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_BACKSPACE:

                self.name = self.name[:-1]


            elif len(self.name)<15:

                if event.unicode.isprintable():

                    self.name += event.unicode




        if event.type == pygame.MOUSEBUTTONDOWN:


            if event.button == 1:


                mouse = pygame.mouse.get_pos()



                for i,rect in enumerate(self.color_buttons):


                    if rect.collidepoint(mouse):

                        self.color_index=i




                if self.start_button.collidepoint(mouse):


                    if self.name.strip()=="":
                        
                        self.name="Jugador"



                    mode_menu = ModeMenu()

                    tipo = mode_menu.run()


                    if tipo == "Solo":

                        solo = SoloMenu()

                        mode = solo.run()


                    elif tipo == "Duo":

                        duo = DuoMenu()

                        mode = duo.run()



                    difficulty_menu = DifficultyMenu()

                    difficulty = difficulty_menu.run()



                    self.result = (

                        self.name,

                        COLORS[self.color_index][1],

                        mode,

                        difficulty

                    )


                    self.running=False

    # ==========================
    # CONTROLES
    # ==========================

    def draw_controls(self):

        self.draw_background()


        self.draw_title(
            "CONTROLES"
        )


        lines = [

            "Jugador 1",
            "W A S D",

            "",

            "Jugador 2",
            "Flechas",


        ]


        y = 180


        for line in lines:


            img = self.font.render(
                line,
                True,
                WHITE
            )


            self.screen.blit(
                img,
                (
                    WIDTH//2-img.get_width()//2,
                    y
                )
            )


            y += 45



        self.back_button = self.draw_button(
            "VOLVER",
            580
        )



    def handle_controls(self,event):


        if event.type == pygame.MOUSEBUTTONDOWN:


            if event.button == 1:


                if self.back_button.collidepoint(
                    pygame.mouse.get_pos()
                ):

                    self.state = "main"





    # ==========================
    # EJECUTAR MENU
    # ==========================

    def run(self):

        self.running=True


        while self.running:


            self.clock.tick(60)


            for event in pygame.event.get():


                if event.type == pygame.QUIT:

                    pygame.quit()

                    raise SystemExit



                # ESC

                if event.type == pygame.KEYDOWN:


                    if event.key == pygame.K_ESCAPE:


                        if self.state != "main":

                            self.state="main"


                        else:

                            pygame.quit()

                            raise SystemExit



                # ESTADOS

                if self.state == "main":

                    self.handle_main(event)


                elif self.state == "player":

                    self.handle_player(event)


                elif self.state == "controls":

                    self.handle_controls(event)




            # DIBUJO

            if self.state == "main":

                self.draw_main()



            elif self.state == "player":

                self.draw_player()



            elif self.state == "controls":

                self.draw_controls()



            pygame.display.flip()



        return self.result