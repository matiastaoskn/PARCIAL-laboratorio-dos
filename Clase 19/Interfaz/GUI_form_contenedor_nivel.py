import pygame
import sqlite3
from pygame.locals import *
from Interfaz.GUI_form_menu_score import *
from Interfaz.GUI_form import *
from Interfaz.GUI_button_image import *
from Interfaz.GUI_form_final import *
from Interfaz.GUI_VICTORIA import *

class FormContenedorNivel(Form):
    def __init__(self, pantalla: pygame.Surface, nivel, form_menu_play):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), "black" )
        self.form_menu_play  = form_menu_play
        nivel._slave = self._slave
        self.nivel = nivel
        self.fondo = pygame.image.load("Recursos\Menu\Botones/niveles.png")
        self.fondo = pygame.transform.scale(self.fondo, (1400, 900))
        self.score = 0
        self._btn_home = Button_Image(screen = self._slave,
                master_x = self._x,
                master_y = self._y,
                x = self._w - 100,
                y = self._h - 100,
                w = 50,
                h = 50,
                onclick = self.btn_home_click,
                onclick_param = "",
                path_image = "Recursos\Menu\Botones\settings.png")    
        self.lista_widgets.append(self._btn_home)


    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.partida_ganada()
        self.draw()
        

    #MENU NIVELES
    def btn_home_click(self, param):
        fondo = pygame.image.load("Recursos\Menu\Botones/niveles.png")
        fondo = pygame.transform.scale(fondo, (1400, 900))
        self.nivel._slave.blit(fondo, (0,0))
        #self.show_dialog()
        self.end_dialog()


    #Termina la partida
    def partida_ganada(self):
        if self.nivel.partida_ganada == True:
            self.score += self.nivel.jugador.acumulador_puntos
            score = self.score 
            with sqlite3.connect("score.db") as conexion:
                try:
                    conexion.execute("INSERT INTO Score (score) VALUES (?)", (score,))
                    print("Inserción exitosa")
                except Exception as e:
                    print("Error score:", str(e))
            fondo = pygame.image.load("Recursos\Menu\Botones/niveles.png")
            fondo = pygame.transform.scale(fondo, (1400, 900))
            self.nivel._slave.blit(fondo, (0,0))
        
            self.end_dialog()
  
        elif self.nivel.tiempo_restante < 0 or self.nivel.jugador.vida_del_personaje == 0:
            self.score += self.nivel.jugador.acumulador_puntos 
            score = self.score
            with sqlite3.connect("score.db") as conexion:
                try:
                    conexion.execute("INSERT INTO Score (score) VALUES (?)", (score,))
                    print("Inserción exitosa")
                except Exception as e:
                    print("Error score:", str(e))

            self.end_dialog()




    
