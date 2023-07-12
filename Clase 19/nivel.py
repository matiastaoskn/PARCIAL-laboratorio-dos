import pygame, sys
from pygame.locals import *
from modo import *
from animaciones import *
from class_personaje import *
from class_enemigo import *
from Interfaz.GUI_form import *

from Interfaz.GUI_form_contenedor_nivel import *
from Interfaz.GUI_label import *
from Interfaz.GUI_slider import *



class Nivel(Form):
    def __init__(self, pantalla, personaje_principal, lista_plataformas, lista_enemigos, lista_rectangulos, lados_rectangulos, piso, imagen_fondo, corazones, rectangulo_personaje, medikit, lista_bosses, puntos_nivel_uno, nivel_uno, lista_escudos, disparos, lista_plataformas_impulso, puede_saltar, nivel_dos, nivel_tres): 
        self._slave = pantalla
        self.jugador = personaje_principal
        self.velocidad_jugador = 10
        self.imagen_fondo = imagen_fondo
        self.corazones = corazones
        self.lista_plataformas = lista_plataformas
        self.lista_enemigos = lista_enemigos
        self.lista_rectangulos = lista_rectangulos
        self.lados_rectangulos = lados_rectangulos
        self.rectangulo_personaje = rectangulo_personaje
        self.piso = piso
        self.lista_balas_personaje = []
        self.lista_balas_enemigo = []
        self.lista_bosses = lista_bosses
        self.lista_escudos = lista_escudos
        for boss in self.lista_bosses:
            self.boss = boss
        self.disparos = disparos
        self.puede_saltar = puede_saltar
        self.medikit = medikit
        self.score = puntos_nivel_uno + 5
        self.lista_plataformas_impulso = lista_plataformas_impulso
        self.nivel_uno_activado = nivel_uno

        self.nivel_dos_activado = nivel_dos
        self.nivel_tres_activado = nivel_tres
        self.tiempo_inicial = 80
        self.tiempo_restante = self.tiempo_inicial
        self.fuente = pygame.font.SysFont(None, 138)
        self.color_texto = ("black")
        self.pos_texto = (1400 // 2, 900 - 750)
        self.RELOJ = pygame.time.Clock()  
        self.lista_eventos = pygame.event.get()

        #Tiempo
        self.duracion_temporizador = 6
        self.tiempo_inicial = pygame.time.get_ticks()

        self.pause = False
        self.acumulador_pause = 0
        self.tiempo_ultimo_disparo = 0


        self.volumen = 0.1
        #HUB
        self.hub_image = pygame.image.load("Recursos\Menu\Botones\hub.png")
        self.hub_image = pygame.transform.scale(self.hub_image, (400, 90))
        self.menu_image = pygame.image.load("Recursos\Menu\Botones\eleccion.png")
        self.menu_image = pygame.transform.scale(self.menu_image, (330, 330))

        # #Musica
        pygame.mixer.init()

        self.partida_ganada = False



        if(self.nivel_uno_activado == True):
            pygame.mixer.music.load("Recursos\Musica/nivel_uno_musica.mp3")
            pygame.mixer.music.play(-1)
        
        if(self.nivel_dos_activado == True):
            self.nivel_uno_activado = False
            pygame.mixer.music.load("Recursos\Musica/nivel_dos_musica.mp3")
            pygame.mixer.music.play(-1)
        


    def update(self, lista_eventos):
        
        self.tiempo_actual = pygame.time.get_ticks()
        self.tiempo_transcurrido_segundos = (self.tiempo_actual - self.tiempo_inicial) / 1000 

        if(self.disparos == True):
            if self.tiempo_transcurrido_segundos >= self.duracion_temporizador:
                for enemigo in self.lista_enemigos:
                    self.crear_bala_enemigo(enemigo)
                    enemigo.que_hace = "disparar"
                self.tiempo_inicial = self.tiempo_actual




        pygame.mixer.music.set_volume(self.volumen)

        self.RELOJ.tick(60)  

        if self.boss.vida_boss < 0:
            pygame.mixer.music.pause()
            self.partida_ganada = True

        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_TAB:
                cambiar_modo()
        
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE]):
            self.pause = True

        COLOR_FONDO_PAUSA = ("white")
        COLOR_BOTON_PAUSA = ("black")
        TEXTO_BOTON_PAUSA = "Pausa"
        FUENTE_BOTON = pygame.font.SysFont(None, 30)

        COLOR_FONDO_MUSICA = ("white")
        COLOR_BOTON_MUSICA = ("black")
        TEXTO_BOTON_MUSICA = "Musica"


        COLOR_FONDO_MUSICA_BAJAR = ("white")
        COLOR_BOTON_MUSICA_BAJAR = ("black")
        TEXTO_BOTON_MUSICA_BAJAR = "-"


        COLOR_FONDO_MUSICA_SUBIR = ("white")
        COLOR_BOTON_MUSICA_SUBIR = ("black")
        TEXTO_BOTON_MUSICA_SUBIR = "+"

        
        COLOR_FONDO_FONDO = ("white")
        COLOR_BOTON_FONDO = ("white")
        TEXTO_BOTON_FONDO = ""


        
        boton_rect_FONDO = pygame.Rect(505, 330, 300, 300)
        boton_rect_PAUSA = pygame.Rect(620, 400, 100, 50)
        boton_rect_MUSICA = pygame.Rect(620, 460, 100, 50)
        boton_rect_RESTA = pygame.Rect(570, 520, 100, 50)
        boton_rect_SUMAR = pygame.Rect(680, 520, 100, 50)

        if self.pause:
            self._slave.blit(self.menu_image, boton_rect_FONDO)

            pygame.draw.rect(self._slave, COLOR_BOTON_PAUSA, boton_rect_PAUSA)
            texto_boton = FUENTE_BOTON.render(TEXTO_BOTON_PAUSA, True, COLOR_FONDO_PAUSA)
            texto_rect = texto_boton.get_rect(center=boton_rect_PAUSA.center)
            self._slave.blit(texto_boton, texto_rect)

            pygame.draw.rect(self._slave, COLOR_BOTON_MUSICA, boton_rect_MUSICA)
            texto_boton = FUENTE_BOTON.render(TEXTO_BOTON_MUSICA, True, COLOR_FONDO_MUSICA)
            texto_rect = texto_boton.get_rect(center=boton_rect_MUSICA.center)
            self._slave.blit(texto_boton, texto_rect)

            pygame.draw.rect(self._slave, COLOR_BOTON_MUSICA_BAJAR, boton_rect_RESTA)
            texto_boton = FUENTE_BOTON.render(TEXTO_BOTON_MUSICA_BAJAR, True, COLOR_FONDO_MUSICA_BAJAR)
            texto_rect = texto_boton.get_rect(center=boton_rect_RESTA.center)
            self._slave.blit(texto_boton, texto_rect)

            pygame.draw.rect(self._slave, COLOR_BOTON_MUSICA_SUBIR, boton_rect_SUMAR)
            texto_boton = FUENTE_BOTON.render(TEXTO_BOTON_MUSICA_SUBIR, True, COLOR_FONDO_MUSICA_SUBIR)
            texto_rect = texto_boton.get_rect(center=boton_rect_SUMAR.center)
            self._slave.blit(texto_boton, texto_rect)
        
            for evento in lista_eventos:
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Verificar si se hizo clic izquierdo
                    if self.pause and boton_rect_PAUSA.collidepoint(evento.pos):
                        self.pause = False
                    
                    if boton_rect_RESTA.collidepoint(evento.pos):
                        self.volumen -= 0.1
                    if boton_rect_SUMAR.collidepoint(evento.pos):
                        self.volumen += 0.1
        

        if self.pause == False:
            self.leer_inputs()
            self.actualizar_pantalla()
            self.dibujar_rectangulos()
        else:
            self.nivel_uno = True

        # Cronometro
        self.tiempo_restante -= self.RELOJ.get_time() / 1000


        pygame.display.update() 

    def actualizar_pantalla(self):
            
        
        # Fondo
        self._slave.blit(self.imagen_fondo, (0, 0))
        
        # Plataformas
        for plataforma in self.lista_plataformas:
            self._slave.blit(plataforma.image, plataforma.rect)

        #Plataformas Impulso
        for plataforma_impulso in self.lista_plataformas_impulso:
            plataforma_impulso.update_plataforma_impulso(self.jugador)
            self._slave.blit(plataforma_impulso.image, plataforma_impulso.rect_impulso)

        for bala in self.lista_balas_personaje:
            bala.bala_update(self.jugador, self.lista_balas_personaje, self.lista_enemigos, self.lista_bosses)
            self._slave.blit(bala.image, bala.rectangulo_bala)
        
        for bala in self.lista_balas_enemigo:
            bala.bala_update(self.jugador, self.lista_balas_enemigo, self.lista_enemigos, self.jugador.escudo_activado)
            self._slave.blit(bala.image, bala.rectangulo_bala)

        enemigos = None
        #enemigo
        for enemigo in self.lista_enemigos:
                enemigos = enemigo
                enemigo.updateEnemigo(self._slave, self.piso, self.lista_plataformas, self.jugador, self.lados_rectangulos, self.rectangulo_personaje, self.lista_enemigos)


        # Personaje
        self.jugador.update(self._slave, self.piso, self.lista_plataformas, enemigos, self.lista_enemigos, self.lista_balas_personaje, self.medikit, self.lista_bosses, self.lista_escudos)

        #HUB
        self._slave.blit(self.hub_image, (520, 0))
        #Corazones
        self._slave.blit(self.corazones.image, (590,22))
        if self.jugador.vida_del_personaje == 3:
            self.corazones.cargar_imagen(corazones_3)
        elif self.jugador.vida_del_personaje == 2:
            self.corazones.cargar_imagen(corazones_2)
        elif self.jugador.vida_del_personaje == 1:
            self.corazones.cargar_imagen(corazones_1)
        else:
            self.corazones.cargar_imagen(corazones_0)

        
        self.texto = self.fuente.render(str(int(self.tiempo_restante)), True, self.color_texto) 
        self.texto_rect = self.texto.get_rect(center=self.pos_texto)
        self._slave.blit(self.texto, self.texto_rect)

        for kit in self.medikit:
            self._slave.blit(kit.image, (kit.rectangulo_medickits.x, kit.rectangulo_medickits.y))       

        for escudo in self.lista_escudos:
            self._slave.blit(escudo.image, (escudo.rectangulo_escudo.x, escudo.rectangulo_escudo.y))

        for boss in self.lista_bosses:
            #llamamos al update boss

            if(len(self.lista_enemigos) == 0):
                boss.updateBoss(self._slave, self.piso, self.lista_plataformas, self.jugador, self.lados_rectangulos, self.rectangulo_personaje, self.puede_saltar)

    def crear_bala_personaje(self):
        self.bala = balas_aire_personaje(50, 50, self.jugador)
        self.lista_balas_personaje.append(self.bala) 
    

    def crear_bala_enemigo(self,enemigo):
        self.bala = balas_aire_enemigo(50, 50, enemigo)
        self.lista_balas_enemigo.append(self.bala) 
    


    def leer_inputs(self):
        self.jugador.colision_detectada = False

        for lado in self.jugador.lados:
            rectangulo = self.jugador.lados[lado]
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_RIGHT] and  rectangulo.right < 1300 - self.velocidad_jugador):
            self.jugador.que_hace = "derecha"
            if(keys[pygame.K_SPACE]):
                self.jugador.que_hace = "golpea"
                golpe_efecto = pygame.mixer.Sound("Recursos/Musica/SONIDOS/golpe_efecto.mp3")
                golpe_efecto.play()
        elif (keys[pygame.K_LEFT] and rectangulo.left > self.velocidad_jugador):
            self.jugador.que_hace = "izquierda"
            if(keys[pygame.K_SPACE]):
                self.jugador.que_hace = "golpea"
                golpe_efecto = pygame.mixer.Sound("Recursos/Musica/SONIDOS/golpe_efecto.mp3")
                golpe_efecto.play()

        elif keys[pygame.K_UP]:
            if not self.jugador.esta_saltando:
                self.jugador.que_hace = "salta"
        else:
            self.jugador.que_hace = "quieto"

        if pygame.mouse.get_pressed()[0]:
                if self.jugador.que_hace != "dispara":
                    tiempo_actual = pygame.time.get_ticks()
                    if tiempo_actual - self.tiempo_ultimo_disparo >= 2000:  # Verificar si han pasado al menos 2 segundos (2000 ms)
                        self.jugador.que_hace = "dispara"
                        self.crear_bala_personaje()
                        self.tiempo_ultimo_disparo = tiempo_actual
        
    def dibujar_rectangulos(self):

        if get_modo():
            
            for boss in self.lista_bosses:
                for lado in boss.lados_boss:  
                    pygame.draw.rect(self._slave, "yellow", boss.lados_boss[lado], 3)

            for kit in self.medikit:
                for lado in kit.lados_kits:
                    pygame.draw.rect(self._slave, "yellow", kit.lados_kits[lado], 3)

            for bala in self.lista_balas_enemigo:
                for lado in bala.lados_bala:   
                    pygame.draw.rect(self._slave, ("yellow"), bala.lados_bala[lado], width=3)

            for bala in self.lista_balas_personaje:   
                for lado in bala.lados_bala:   
                    pygame.draw.rect(self._slave, ("yellow"), bala.lados_bala[lado], width=3)

            for rectangulo in self.lista_rectangulos:
                pygame.draw.rect(self._slave, (255, 0, 0), rectangulo.rect, width=3)

            for enemigo in self.lista_enemigos:
                for lado in enemigo.lados:
                    pygame.draw.rect(self._slave, "Blue", enemigo.lados[lado], 2)

            for plataforma in self.lista_plataformas:
                pygame.draw.rect(self._slave, (255, 0, 0), plataforma.rect, width=3)

            for lado in self.piso:
                pygame.draw.rect(self._slave, "Blue", self.piso[lado], 2)

            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "yellow", self.jugador.lados[lado], 3)


