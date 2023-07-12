import pygame
from settings import *
import random
import time


class Personaje:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad_personaje):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        #Movimiento
        self.contador_pasos = 0
        self.accion = "quieto"
        self.animaciones = animaciones
        self.rescalar_animaciones()
        self.esta_saltando = False

        #Colision
        self.rectangulo_personaje = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo_personaje.x = posicion_inicial[0]
        self.rectangulo_personaje.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo_personaje)
        
        #Vida
        self.vida_del_personaje = 3

        #Salto
        self.desplazamiento_y = 0
        self.velocidad = velocidad_personaje
        self.que_hace = "quieto"
        self.esta_disparando = False
        self.puede_saltar = True
        self.direccion = ""

        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15

        #Atacar
        self.acumulador_puntos = 0
        self.golpe_realizado = False
        self.duracion_temporizador = 5
        self.tiempo_inicial = pygame.time.get_ticks()

        self.duracion_temporizador_escudo = 10
        self.tiempo_inicial_escudo = pygame.time.get_ticks()

        self.escudo_activado = False

    def rescalar_animaciones(self):
        for clave in self.animaciones:
            rescalarar_img(self.animaciones[clave], (self.ancho, self.alto))
    
    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self, velocidad):
        #Se mueve el personaje
        for lado in self.lados:
            self.lados[lado].x += velocidad
    
    def dispara_bola(self, bala, enemigo):
        bala.rectangulo_bala.x = self.rectangulo_personaje.right
        bala.rectangulo_bala.y = self.rectangulo_personaje.y

    def golpear_enemigo(self, enemigo, lista_enemigos, lista_bosses):
            if(len(lista_enemigos) != 0):
                for enemigo in lista_enemigos:
                    if self.lados["main"].colliderect(enemigo.lados['main']) and self.golpe_realizado == False:
                        enemigo.vida_enemigo -= 1
                        enemigo.que_hace = "dañado"
                    if enemigo.vida_enemigo <= 0:
                        lista_enemigos.remove(enemigo)
                        self.acumulador_puntos += 100
 
            for boss in lista_bosses:  
                if boss.realiza_ulti == False: 
                    if(self.lados["main"].colliderect(boss.lados_boss['main']) and self.golpe_realizado == False):
                        boss.vida_boss -= 1
                        boss.que_hace = "dañado"
                    if boss.vida_boss < 0:
                        lista_bosses.remove(boss)
                        self.acumulador_puntos += 200
                        boss.boss_muerto = True
                            
    def aplicar_gravedad(self, pantalla, piso, lista_plataformas):
        if self.esta_saltando:
            if self.direccion == "izquierda":
                self.animar(pantalla, "salta_izquierda")
            else:
                self.animar(pantalla, "salta_derecha")

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        if self.lados["bottom"].colliderect(piso["main"]):
            self.desplazamiento_y = 0
            self.esta_saltando = False
            self.lados["main"].bottom = piso["main"].top + 5
            self.puede_saltar = True
        else:
            self.esta_saltando = True
        
        for plataforma in lista_plataformas:
            if self.lados["bottom"].colliderect(plataforma.rect) and self.desplazamiento_y >= 0:
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = plataforma.rect.top + 5
                self.puede_saltar = True
                break

    def update(self, pantalla, piso, lista_plataformas, enemigo, lista_enemigos, lista_bala, lista_medickit, lista_bosses, lista_escudo):
        
        
        self.tiempo_actual_escudo = pygame.time.get_ticks()
        self.tiempo_transcurrido_segundos_escudo = (self.tiempo_actual_escudo - self.tiempo_inicial_escudo) / 1000

        if self.escudo_activado:
            if self.tiempo_transcurrido_segundos_escudo >= self.duracion_temporizador_escudo:
                self.escudo_activado = False
        for escudo in lista_escudo:
            if self.lados["main"].colliderect(escudo.lados_escudo['main']):
                lista_escudo.remove(escudo)
                self.escudo_activado = True
                golpe_efecto = pygame.mixer.Sound("Recursos\Musica\SONIDOS\moneda.mp3")
                golpe_efecto.play()

        for kit in lista_medickit:
            if(self.lados["main"].colliderect(kit.lados_kits['main'])):
                if(self.vida_del_personaje < 3):
                    self.vida_del_personaje = 3
                    lista_medickit.remove(kit)
                    golpe_efecto = pygame.mixer.Sound("Recursos\Musica\SONIDOS\moneda.mp3")
                    golpe_efecto.play()

        self.tiempo_actual = pygame.time.get_ticks()
        self.tiempo_transcurrido_segundos = (self.tiempo_actual - self.tiempo_inicial) / 1000 

        if self.tiempo_transcurrido_segundos >= self.duracion_temporizador:
            self.golpe_realizado = False
            self.tiempo_inicial = self.tiempo_actual

        for bala in lista_bala:
            bala.rectangulo_bala.x += bala.velocidad_bala
            if self.que_hace == "dispara":
                self.dispara_bola(bala, enemigo)

        if self.que_hace == "golpea":
            if(self.direccion == "derecha"):
                self.animar(pantalla, "golpea_derecha")
            else:
                self.animar(pantalla, "golpea_izquierda")
            self.golpear_enemigo(enemigo, lista_enemigos, lista_bosses)
        


        elif self.que_hace == "izquierda":
            if not self.esta_saltando:
                self.animar(pantalla, "camina_izquierda")
            self.mover(self.velocidad * -1)
            self.direccion = "izquierda"

        elif self.que_hace == "quieto":
            if not self.esta_saltando:
                self.animar(pantalla, "quieto")

        elif self.que_hace == "salta":
           if not self.esta_saltando and self.puede_saltar:
            self.esta_saltando = True
            self.desplazamiento_y = self.potencia_salto 
            self.puede_saltar = False
        
        elif self.que_hace == "derecha":
            if not self.esta_saltando:
                self.animar(pantalla, "camina_derecha")
            self.mover(self.velocidad)
            self.direccion = "derecha"
        
        

        self.aplicar_gravedad(pantalla, piso, lista_plataformas)


class Corazones():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.corazones = corazones_3
        self.image = pygame.image.load(self.corazones)
        self.image = pygame.transform.scale(self.image, (w, h))
        
    def cargar_imagen(self, imagen):
        self.imagen = imagen
        self.image = pygame.image.load(self.imagen)
        self.image = pygame.transform.scale(self.image, (self.w, self.h))

class balas_aire_personaje():
    def __init__(self, w, h, jugador):
        self.w = w
        self.h = h

        self.image = pygame.image.load("Recursos\Menu\espada.png")
        self.image = pygame.transform.scale(self.image, (w, h))
        self.velocidad_bala = 10
        
        #Colision
        self.rectangulo_bala = self.image.get_rect()
        self.rectangulo_bala.x = jugador.rectangulo_personaje.x + 40
        self.rectangulo_bala.y = jugador.rectangulo_personaje.y
        self.lados_bala = obtener_rectangulos(self.rectangulo_bala)


    def mover(self):
        self.rectangulo_bala.x += self.velocidad_bala

    def golpear_enemigo(self, lista_enemigos, lista_bosses, lista_balas):
        if(len(lista_enemigos) != 0):
            for bala in lista_balas:
                for enemigo in lista_enemigos:
                    if self.lados_bala["main"].colliderect(enemigo.lados['main']):
                        enemigo.vida_enemigo -= 1
                        enemigo.que_hace = "dañado"
                        lista_balas.remove(bala)
                    if enemigo.vida_enemigo <= 0:
                        lista_enemigos.remove(enemigo)
        for bala in lista_balas:
            for boss in lista_bosses:  
                if boss.realiza_ulti == False: 
                    if(self.lados_bala["main"].colliderect(boss.lados_boss['main'])):
                        boss.vida_boss -= 1
                        boss.que_hace = "dañado"
                        lista_balas.remove(bala)
                    if boss.vida_boss < 0:
                        lista_bosses.remove(boss)

    def bala_update(self, personaje, lista_balas, lista_enemigos, lista_bosses):
        if(personaje.que_hace == "dispara" and personaje.direccion == "izquierda"):
                self.velocidad_bala = -13
                self.image = pygame.image.load("Recursos\Menu\espada_izquierda.png")
                self.image = pygame.transform.scale(self.image, (self.w, self.h))
        
        self.golpear_enemigo(lista_enemigos, lista_bosses, lista_balas)
        self.mover()
    
        if self.rectangulo_bala.right < 0 or self.rectangulo_bala.left > 1400:
            lista_balas.remove(self)

class balas_aire_enemigo():
    def __init__(self, w, h, enemigo):
        self.w = w
        self.h = h

        self.image = pygame.image.load("Recursos\Menu\espada.png")
        self.image = pygame.transform.scale(self.image, (w, h))
        self.velocidad_bala = 10
        
        #Colision
        self.rectangulo_bala = self.image.get_rect()
        self.rectangulo_bala.x = enemigo.rectangulo_enemigo.x + 40
        self.rectangulo_bala.y = enemigo.rectangulo_enemigo.y
        self.lados_bala = obtener_rectangulos(self.rectangulo_bala)


    def mover(self):
        self.rectangulo_bala.x += self.velocidad_bala

    def golpear_enemigo(self, personaje, lista_balas, escudo_activado):
            for bala in lista_balas:
                    if self.lados_bala["main"].colliderect(personaje.lados['main']):
                        if(escudo_activado == False):
                            golpe_efecto = pygame.mixer.Sound("Recursos\Musica\SONIDOS\MUERTE.mp3")
                            golpe_efecto.play()
                            personaje.vida_del_personaje -= 1
                            personaje.que_hace = "dañado"
                        lista_balas.remove(bala)

    def bala_update(self, personaje, lista_balas, lista_enemigos, escudo_activado):
        for enemigo in lista_enemigos:
            if(enemigo.que_hace == "disparar" and enemigo.sentido == "izquierda"):
                self.velocidad_bala = -13
                self.image = pygame.image.load("Recursos\Menu\espada_izquierda.png")
                self.image = pygame.transform.scale(self.image, (self.w, self.h))
            if(enemigo.que_hace == "disparar" and enemigo.sentido == "derecha"):
                self.velocidad_bala = 13
                self.image = pygame.image.load("Recursos\Menu\espada.png")
                self.image = pygame.transform.scale(self.image, (self.w, self.h))

        self.golpear_enemigo(personaje, lista_balas, escudo_activado)
        self.mover()
    
        if self.rectangulo_bala.right < 0 or self.rectangulo_bala.left > 1400:
            lista_balas.remove(self)

class MedicKit():
    def __init__(self, w, h, x, y):
        self.w = w
        self.h = h

        self.image = pygame.image.load("Recursos\Accesorios\medic_kit.png")
        self.image = pygame.transform.scale(self.image, (w, h))
        
        
        self.rectangulo_medickits = self.image.get_rect()
        self.rectangulo_medickits.x = x
        self.rectangulo_medickits.y = y
        self.lados_kits = obtener_rectangulos(self.rectangulo_medickits)

class Escudo():
    def __init__(self, w, h, x, y):
        self.w = w
        self.h = h

        self.image = pygame.image.load("Recursos\Corazones\escudo.png")
        self.image = pygame.transform.scale(self.image, (w, h))
        
        
        self.rectangulo_escudo = self.image.get_rect()
        self.rectangulo_escudo.x = x
        self.rectangulo_escudo.y = y
        self.lados_escudo = obtener_rectangulos(self.rectangulo_escudo)