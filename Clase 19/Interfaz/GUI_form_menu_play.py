import pygame
from pygame.locals import *

from Interfaz.GUI_button_image import *
from Interfaz.GUI_form import *
from Interfaz.GUI_form_contenedor_nivel import *
from Interfaz.GUI_manejador_niveles import *

class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, active):
        super().__init__(screen, x, y, w, h, active)
        fondo = pygame.image.load("Recursos\Menu\Botones/niveles.png")
        fondo = pygame.transform.scale(fondo, (1400, 900))
        screen.blit(fondo, (0,0))

        self.manejador_niveles = ControlNiveles(self._master)
        menu = pygame.image.load("Recursos\Menu\Botones\eleccion.png")
        menu = pygame.transform.scale(menu, (500,500))
        self._slave.blit(menu, (0,0))
        self.slave = self._slave

        self.puntos = 0
        
  

        self._btn_level_1 = Button_Image(screen = self._slave,
                        x = 100,
                        y = 100,  
                        master_x = x,
                        master_y = y,
                        w = 130,
                        h = 150,
                        onclick = self.entrar_nivel,
                        onclick_param = "nivel_uno",
                        path_image = "Recursos/Niveles/nivel1.jpg")
                        
        self._btn_level_2 = Button_Image(screen = self._slave,
                            x = 250,
                            y = 100,
                            master_x = x,
                            master_y = y,
                            w = 130,
                            h = 150,
                            onclick = self.entrar_nivel,
                            onclick_param = "nivel_dos",
                            path_image = "Recursos/Niveles/nivel2.jpg")
                
        self._btn_level_3 = Button_Image(screen = self._slave,
                            x = 100,
                            y = 250,
                            master_x = x,
                            master_y = y,
                            w = 130,
                            h = 150,
                            color_background = (255, 0, 0),
                            color_border = (255, 0, 255),
                            onclick = self.entrar_nivel,
                            onclick_param = "nivel_tres",
                            text = "",
                            font = "Verdane",
                            font_size = 15,
                            font_color = (0, 255, 0),
                            path_image = "Recursos/Niveles/nivel3.jpg")
        

        self._btn_home = Button_Image(screen = self._slave,
                        x = 350,
                        y = 370,
                        master_x = x,
                        master_y = y,
                        w = 50,
                        h = 50,
                        onclick = self.btn_home_click,
                        onclick_param = "",
                        path_image = "Recursos\Menu\Botones\settings.png") 

        
                  
        
        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)
        self.lista_widgets.append(self._btn_level_3)

        self.lista_widgets.append(self._btn_home)
        

    def on(self, parametro):
        print("hola", parametro)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self, nombre_nivel):
        print("entre")
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        self.puntos = nivel.score
        self.partida_ganada = nivel.nivel_uno

        form_contenedor_nivel = FormContenedorNivel(self._master, nivel, FormMenuPlay)
        self.show_dialog(form_contenedor_nivel)

    def btn_home_click(self, param):
        self.end_dialog()


