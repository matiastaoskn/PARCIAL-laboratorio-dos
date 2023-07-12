import pygame
from pygame.locals import *

from Interfaz.GUI_button import *
from Interfaz.GUI_slider import *
from Interfaz.GUI_textbox import *
from Interfaz.GUI_label import *
from Interfaz.GUI_form import *
from Interfaz.GUI_button_image import *
from Interfaz.GUI_form_menu_score import *
from Interfaz.GUI_form_menu_play import *

import sqlite3

class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.screen = screen
        self._lax = x
        self.lay = y
        self.volumen = 0.2
        self.flag_play = True
        self.flag_opciones = False
        pygame.mixer.init()

        ##Controles
        self.txtbox = TextBox(self._slave, x, y, 110, 800, 180, 40, "white", "white", "black", "Blue", 2, font= "Comic Sans", font_size=15, font_color="black")
        self.btn_tabla = Button_Image(self._slave, x,y, 580, 800, 250, 80, "Recursos\Menu\Botones\score.png", self.btn_tabla_opciones_click, "x" )
        self.btn_settings = Button_Image(self._slave, x,y, 580, 700, 250, 80, "Recursos\Menu\Botones\play.png", self.btn_jugar_click, "a")
        

        self.label_volumen = Label(self._slave, 1310, 785, 50, 50, "20%", "Comic Sans", 15, "White", "Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 1050, 800, 250, 15, self.volumen, "green", "White")


        #Agrego controles
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_settings)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)


        pygame.mixer.music.load("Recursos\Musica\MENU_MUSICA.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        
        self.render()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def btn_jugar_click(self, param):
        nombre = self.txtbox.get_text()

        with sqlite3.connect("nombres.db") as conexion:
            try:
                conexion.execute("INSERT INTO Jugador (jugador) VALUES (?)", (nombre,))
                print("Inserción exitosa")
            except Exception as e:
                print("Error nombre:", str(e))    

        frm_jugar = FormMenuPlay(screen=self._master, 
                                 x = self._master.get_width() / 2 - 250,
                                 y = self._master.get_height() /2 -220,
                                 w = 500,
                                 h = 500,
                                 active = True)
        pygame.mixer.music.pause()
        self.show_dialog(frm_jugar)

    def btn_play_click(self, texto): 

        if self.flag_play:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
 
        self.flag_play = not self.flag_play

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
    
    def btn_tabla_opciones_click(self, texto):
        lista_nombres = []
        lista_score = []
        with sqlite3.connect("nombres.db") as conexion:
                cursor = conexion.execute("SELECT * FROM jugador ORDER BY id DESC LIMIT 3")
                print("Consulta exitosa")

                for fila in cursor:  # Acceder al valor de la columna "Jugador"
                    lista_nombres.append(fila[1])
                print(lista_nombres)

        with sqlite3.connect("score.db") as conexion:
                cursor = conexion.execute("SELECT * FROM score ORDER BY id DESC LIMIT 3")

                for fila in cursor:  # Acceder al valor de la columna "Jugador"
                    lista_score.append(fila[1])
                print(lista_score)


                dic_score = [
                    {"Jugador": lista_nombres[0], "Score": lista_score[0]},
                    {"Jugador": lista_nombres[1], "Score": lista_score[0]},
                    {"Jugador": lista_nombres[2], "Score": lista_score[0]}
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
                    # Realizar operaciones adicionales con el dic_score

    def render(self):
        image = pygame.image.load("Recursos\Menu\RYU.png")
        image = pygame.transform.scale(image, (1400, 900))
        self._slave.blit(image, (0, 0))
        
    
