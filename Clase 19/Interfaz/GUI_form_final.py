import pygame
from pygame.locals import *

from Interfaz.GUI_button import *
from Interfaz.GUI_slider import *
from Interfaz.GUI_textbox import *
from Interfaz.GUI_label import *
from Interfaz.GUI_form import *
from Interfaz.GUI_button_image import *
from Interfaz.GUI_form_menu_score import *


class FormFinal(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.screen = screen
        self._lax = x
        self.lay = y
        self.volumen = 0.2
        self.flag_play = True
        pygame.mixer.init()

        ##Controles
        self.txtbox = TextBox(self.screen, x, y, 50, 50, 200, 30, "gray", "white", "red", "Blue", 2, font= "Comic Sans", font_size=15, font_color="black")
        self.btn_tabla = Button_Image(self.screen, x,y, 550, 800, 250, 80, "Recursos\Menu\Botones\score.png", self.btn_tabla_click, "x" )
        self.btn_options = Button_Image(self.screen, x,y, 550, 700, 250, 80, "Recursos\Menu\Botones\opcions.png", self.btn_tabla_opciones_click, "a")

        #Agrego controles
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_options)
        
        self.render()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
        
        self.render()
        self.draw()

 

    def btn_play_click(self, texto):
        nombre = self.txtbox.get_text()
        print(nombre)

    
    def btn_tabla_click(self, texto):
        dic_score = [{"Jugador": "Gio", "Score": 1000},
                     {"Jugador": "Matias", "Score": 100},
                     {"Jugador": "Mica", "Score": 50}
                     ]
        form_puntaje = FormMenu(self._master, 
                                450,
                                200,
                                500,
                                550,
                                (200, 0, 220), 
                                "White",
                                True,
                                "Interfaz\Window.png",
                                dic_score,
                                100,
                                10,
                                10
                                )
        
        self.show_dialog(form_puntaje)

    def btn_tabla_opciones_click(self, texto):
        dic_score = [{"Jugador": "Gio", "Score": 1000},
                        {"Jugador": "Matias", "Score": 100},
                        {"Jugador": "Mica", "Score": 50}
                        ]
        form_puntaje = FormMenu(self._master, 
                                450,
                                200,
                                500,
                                550,
                                (200, 0, 220), 
                                "White",
                                True,
                                "Interfaz\Window.png",
                                dic_score,
                                100,
                                10,
                                10
                                )
        self.show_dialog(form_puntaje)

    def render(self):
        image = pygame.image.load("Recursos\Menu\RYU.png")
        image = pygame.transform.scale(image, (1400, 900))
        self._slave.blit(image, (0, 0))
        # 
    