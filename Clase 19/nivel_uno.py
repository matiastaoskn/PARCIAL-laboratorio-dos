from nivel import *
from class_personaje import *
from class_enemigo import *
from class_plataforma import *
from animaciones import *
from Interfaz.GUI_form_contenedor_nivel import *


import pygame, sys

class NivelUno(Nivel):
    def __init__(self, pantalla):
        self.lista_balas = []
        self.nivel_uno = True
        self.nivel_dos = False
        self.nivel_tres = False

        # Funciones

        W, H = 1400, 900
        TAMAÑO_PANTALLA = (W, H)
        FPS = 30
        velocidad_personaje = 20
        velocidad_enemigo = 4

        pygame.init()

        RELOJ = pygame.time.Clock()
        PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)

        # FONDO
        fondo = pygame.image.load("Recursos\Menu\chinafondo.jpg")
        fondo = pygame.transform.scale(fondo, (1600,1100))

        # Personaje
        posicion_inicial = (H / 2 - 50, 620)
        tamaño = (110, 120)

        #Enemigos
        posicion_inicial_enemigo_1 = (H / 2 + 150, 180)
        posicion_inicial_enemigo_2 = (H / 2 - 450, 200)
        posicion_inicial_enemigo_3 = (H / 2 + 650, 180)
        posicion_inicial_enemigo_4 = (H / 2 - 180, 400)

        tamaño_enemigo = (110, 150)

        # Crear personaje
        mi_personaje = Personaje(tamaño, diccionario_animaciones_personaje, posicion_inicial, velocidad_personaje)
        rectangulo_personaje = mi_personaje.lados
    
        self.disparos = False

        # Crear enemigo
        enemigo1 = Enemigos(tamaño_enemigo, animaciones_enemigo, posicion_inicial_enemigo_1, velocidad_enemigo, False)
        enemigo2 = Enemigos(tamaño_enemigo, animaciones_enemigo, posicion_inicial_enemigo_2, velocidad_enemigo, False)
        enemigo3 = Enemigos(tamaño_enemigo, animaciones_enemigo, posicion_inicial_enemigo_3, velocidad_enemigo, False)
        enemigo4 = Enemigos(tamaño_enemigo, animaciones_enemigo, posicion_inicial_enemigo_4, velocidad_enemigo, False)
        
        
        lista_enemigos = []
        lista_enemigos.append(enemigo1)
        lista_enemigos.append(enemigo2)
        lista_enemigos.append(enemigo3)
        lista_enemigos.append(enemigo4)

        #Boss
        tamaño_boss = (150, 150)
        lista_bosses = []
        boss = BossFinal(tamaño_boss, animaciones_boss_uno, 120, 650, velocidad_enemigo=10)
        lista_bosses.append(boss)
        
        self.puntos = 0

        # Piso
        piso = pygame.Rect(0, 60, W, 20)
        piso.top = H - 90

        Plataforma
        lista_plataformas = []


        def crear_plataforma(x, y, width, height, path_image):
            plataforma = Plataforma(x, y, width, height, path_image)
            lista_plataformas.append(plataforma)

        self.path_image = "Recursos\Plataformas\plataforma1.png"

        plataformas = [
            #Primera
            crear_plataforma(x=910, y=H - 340, width=500, height=80, path_image = self.path_image),
            #Primera-arriba
            crear_plataforma(x=910, y=H - 560, width=500, height=80, path_image = self.path_image),
            #Medio
            crear_plataforma(x=500, y=H - 220, width=300, height=80, path_image = self.path_image),
            #Medio-Arriba
            crear_plataforma(x=500, y=H - 460, width=300, height=80, path_image = self.path_image),
            #Izquierda
            crear_plataforma(x=-30, y=H - 340, width=400, height=80, path_image = self.path_image),
            #Izquierda-arriba
            crear_plataforma(x=-30, y=H - 560, width=400, height=80, path_image = self.path_image),
        ]
        

        #Rectangulos-bordes
        lista_rectangulos = []
        lista_lados_rectangulos = []

        def crear_rectangulo(x, y, width, height):
            rectangulo = Rectangulo(x,y,width,height)
            lista_rectangulos.append(rectangulo)

            lados_rectangulo = rectangulo.lados_rectangulo
            lista_lados_rectangulos.append(lados_rectangulo)
            
        rectangulos = [
            crear_rectangulo(x=320, y=H - 450, width=50, height=50),
            crear_rectangulo(x=900, y=H - 450, width=50, height=50),
            crear_rectangulo(x=320, y=H - 650, width=50, height=50),
            crear_rectangulo(x=900, y=H - 650, width=50, height=50)
        ]
        

  
        #Corazones
        corazones = Corazones(w=160, h=50)

        #Medickit
        lista_medikits = []
        medikit_uno = MedicKit(60, 60, 620, 580)
        medikit_dos = MedicKit(60, 60, 1200, 400)
        lista_medikits.append(medikit_uno)
        lista_medikits.append(medikit_dos)

        #Colision Piso
        lados_piso = obtener_rectangulos(piso)


        # RECTANGULO-PERSONAJE
        x_inicial = H / 2 - 400
        y_inicial = 750
        self.lista_plataformas_impulso = []

        self.puede_saltar = False

        super().__init__(pantalla, mi_personaje, lista_plataformas, lista_enemigos, lista_rectangulos, lista_lados_rectangulos,lados_piso, fondo, corazones, rectangulo_personaje, lista_medikits, lista_bosses, self.puntos, self.nivel_uno, self.lista_balas, self.disparos, self.lista_plataformas_impulso, self.puede_saltar, self.nivel_dos, self.nivel_tres)