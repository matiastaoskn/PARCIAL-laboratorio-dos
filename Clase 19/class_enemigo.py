import pygame
from settings import *
from class_personaje import *
from nivel import *
import random
import time


class Enemigos(Personaje):
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad_enemigo, disparos):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
    
        self.contador_pasos = 0
        self.accion = "camina_derecha"
        self.animaciones = animaciones
        self.rescalar_animaciones()
        self.esta_saltando = False
 
        self.rectangulo_enemigo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo_enemigo.x = posicion_inicial[0]
        self.rectangulo_enemigo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo_enemigo)

        #Salto
        self.desplazamiento_y = 0
        self.velocidad_enemigo = velocidad_enemigo
        self.que_hace = "quieto"
        self.puede_saltar = True
        self.direccion = 1
        self.sentido = ""

        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15

        #Atacar
        self.vida_enemigo = 3
        self.golpe_realizado = False
        self.duracion_temporizador = 8
        self.tiempo_inicial = pygame.time.get_ticks()

        self.disparos = disparos
        
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
        if(self.que_hace != "golpear"):
            for lado in self.lados:
                self.lados[lado].x += velocidad

    def aplicar_gravedad(self, piso, lista_plataformas):
        if self.esta_saltando:
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

    def golpear_personaje_derecha(self, personaje, pantalla, rectangulo_personaje):
        if self.lados["right"].colliderect(personaje.lados["main"]) and self.golpe_realizado == False:
            self.golpe_realizado = True
            self.animar(pantalla, "ataca_derecha")
            self.personaje_golpeada(rectangulo_personaje, personaje)

    def golpear_personaje_izquierda(self, personaje, pantalla, rectangulo_personaje):
        if self.lados["left"].colliderect(personaje.lados["main"]) and self.golpe_realizado == False:
            self.golpe_realizado = True
            self.animar(pantalla, "ataca_derecha")
            self.personaje_golpeada(rectangulo_personaje, personaje)
            
    def personaje_golpeada(self, rectangulo_personaje, personaje):
        personaje.vida_del_personaje -= 1
        for lado in rectangulo_personaje:
            if self.que_hace == "camina_derecha":
                rectangulo_personaje["main"].x += 20
                rectangulo_personaje["bottom"].x += 20
                rectangulo_personaje["left"].x += 20
                rectangulo_personaje["top"].x += 20
                rectangulo_personaje["right"].x += 20

                rectangulo_personaje["main"].y -= 5
                rectangulo_personaje["bottom"].y -= 5
                rectangulo_personaje["left"].y -= 5
                rectangulo_personaje["top"].y -= 5
                rectangulo_personaje["right"].y -= 5
            else:
                rectangulo_personaje["main"].x -= 20
                rectangulo_personaje["bottom"].x -= 20
                rectangulo_personaje["left"].x -= 20
                rectangulo_personaje["top"].x -= 20
                rectangulo_personaje["right"].x -= 20

                rectangulo_personaje["main"].y -= 5
                rectangulo_personaje["bottom"].y -= 5
                rectangulo_personaje["left"].y -= 5
                rectangulo_personaje["top"].y -= 5
                rectangulo_personaje["right"].y -= 5

    def updateEnemigo(self, pantalla, piso, lista_plataformas, personaje, lados_rectangulos, rectangulo_personaje, lista_enemigos):
        self.tiempo_actual = pygame.time.get_ticks()
        self.tiempo_transcurrido_segundos = (self.tiempo_actual - self.tiempo_inicial) / 1000 
        
        if(self.golpe_realizado == True):
            if self.tiempo_transcurrido_segundos >= self.duracion_temporizador:
                print("pasaron 5 seugnos")
                self.golpe_realizado = False
                self.tiempo_inicial = self.tiempo_actual

        if self.que_hace == "dañado":
            self.animar(pantalla, "enemigo_dañado")

        elif self.que_hace == "quieto":
            self.animar(pantalla, "quieto")

        elif self.que_hace == "camina_derecha":
            self.animar(pantalla, "camina_derecha")

        elif self.que_hace == "camina_izquierda":
            self.animar(pantalla, "camina_izquierda")

        elif self.que_hace == "golpeando":
            self.animar(pantalla, "ataca_derecha")
        
        elif self.que_hace == "disparar":
            self.animar(pantalla, "ataca_derecha")
        


        for lado in self.lados:
            rectangulo = self.lados[lado]

            if self.lados["main"].colliderect(lados_rectangulos[0]["right"]) and self.direccion == 1 :
                print("toque")
                self.direccion = -1
                self.mover(self.velocidad_enemigo * -1)
                self.que_hace = "camina_izquierda"
                self.sentido = "izquierda"

            if self.lados["main"].colliderect(lados_rectangulos[1]["main"]) and self.direccion == -1 :
                self.direccion = 1
                self.mover(self.velocidad_enemigo * 1)
                self.que_hace = "camina_derecha"
                self.sentido = "derecha"

            if self.lados["main"].colliderect(lados_rectangulos[2]["right"]) and self.direccion == -1 :
                self.direccion = 1
                self.mover(self.velocidad_enemigo * 1)
                self.que_hace = "camina_derecha"
                self.sentido = "derecha"
            


        if(rectangulo.right < 1280 - self.velocidad_enemigo and self.direccion == 1):
            self.mover(self.velocidad_enemigo)
            self.que_hace = "camina_derecha"
            self.sentido = "derecha"
            if(self.golpe_realizado == False):
                self.golpear_personaje_derecha(personaje, pantalla, rectangulo_personaje)
            
        if rectangulo.right >= 1280 - self.velocidad_enemigo and self.direccion == 1:
            self.direccion = -1
            self.mover(self.velocidad_enemigo * -1)
            self.que_hace = "camina_izquierda"
            self.sentido = "izquierda"
            if(self.golpe_realizado == False):
                self.golpear_personaje_izquierda(personaje, pantalla, rectangulo_personaje)

        elif rectangulo.left > self.velocidad_enemigo and self.direccion == -1:
            self.mover(self.velocidad_enemigo * -1)
            self.que_hace = "camina_izquierda"
            self.sentido = "izquierda"
            if(self.golpe_realizado == False):
                self.golpear_personaje_izquierda(personaje, pantalla, rectangulo_personaje)

        elif rectangulo.left <= self.velocidad_enemigo and self.direccion == -1:
            self.direccion = 1
            self.mover(self.velocidad_enemigo)
            self.que_hace = "camina_derecha"
            self.sentido = "derecha"
            if(self.golpe_realizado == False):
                self.golpear_personaje_derecha(personaje, pantalla, rectangulo_personaje)



        self.aplicar_gravedad(piso, lista_plataformas)


class BossFinal:
    def __init__(self, tamaño_boss, animaciones, x, y, velocidad_enemigo):
        self.ancho = tamaño_boss[0]
        self.alto = tamaño_boss[1]
    
        self.contador_pasos = 0
        self.accion = "camina_derecha"
        self.animaciones = animaciones
        self.rescalar_animaciones()
        self.esta_saltando = False
 
        rectangulo_boss = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo_boss.x = x
        rectangulo_boss.y = y
        self.lados_boss = obtener_rectangulos(rectangulo_boss)

        #Salto
        self.desplazamiento_y = 0
        self.velocidad_enemigo = velocidad_enemigo
        self.que_hace = "quieto"
        self.puede_saltar = True
        self.direccion = 1

        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15

        #Atacar
        self.vida_boss = 30
        self.golpe_realizado = False
        self.realiza_ulti = False

        #Tiempo
        self.duracion_temporizador_golpe = 5
        self.duracion_temporizador_ulti = 6
        self.tiempo_inicial = pygame.time.get_ticks()
        self.ultima_ulti = pygame.time.get_ticks()

    def rescalar_animaciones(self):
        for clave in self.animaciones:
            rescalarar_img(self.animaciones[clave], (self.ancho, self.alto))

    def mover(self, velocidad):
        if(self.que_hace != "golpear"):
            for lado in self.lados_boss:
                self.lados_boss[lado].x += velocidad

    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados_boss["main"])
        self.contador_pasos += 1

    def golpear_personaje_derecha(self, personaje, pantalla, rectangulo_personaje):
        if self.lados_boss["right"].colliderect(personaje.lados["main"]) and self.golpe_realizado == False:
            self.golpe_realizado = True
            self.animar(pantalla, "ataca_derecha")
            self.personaje_golpeada(rectangulo_personaje, personaje)

    def golpear_personaje_izquierda(self, personaje, pantalla, rectangulo_personaje):
        if self.lados_boss["left"].colliderect(personaje.lados["main"]) and self.golpe_realizado == False:
            self.golpe_realizado = True
            self.animar(pantalla, "ataca_derecha")
            self.personaje_golpeada(rectangulo_personaje, personaje)

    def personaje_golpeada(self, rectangulo_personaje, personaje):
        personaje.vida_del_personaje -= 1
        for lado in rectangulo_personaje:
            if self.que_hace == "camina_derecha":
                rectangulo_personaje["main"].x += 20
                rectangulo_personaje["bottom"].x += 20
                rectangulo_personaje["left"].x += 20
                rectangulo_personaje["top"].x += 20
                rectangulo_personaje["right"].x += 20

                rectangulo_personaje["main"].y -= 5
                rectangulo_personaje["bottom"].y -= 5
                rectangulo_personaje["left"].y -= 5
                rectangulo_personaje["top"].y -= 5
                rectangulo_personaje["right"].y -= 5
            else:
                rectangulo_personaje["main"].x -= 20
                rectangulo_personaje["bottom"].x -= 20
                rectangulo_personaje["left"].x -= 20
                rectangulo_personaje["top"].x -= 20
                rectangulo_personaje["right"].x -= 20

                rectangulo_personaje["main"].y -= 5
                rectangulo_personaje["bottom"].y -= 5
                rectangulo_personaje["left"].y -= 5
                rectangulo_personaje["top"].y -= 5
                rectangulo_personaje["right"].y -= 5

    def aplicar_gravedad(self, piso, lista_plataformas):
        if self.esta_saltando:
            for lado in self.lados_boss:
                self.lados_boss[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        if self.lados_boss["bottom"].colliderect(piso["main"]):
            self.desplazamiento_y = 0
            self.esta_saltando = False
            self.lados_boss["main"].bottom = piso["main"].top + 5
            self.puede_saltar = True
        else:
            self.esta_saltando = True
        
        for plataforma in lista_plataformas:
            if self.lados_boss["bottom"].colliderect(plataforma.rect) and self.desplazamiento_y >= 0:
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados_boss["main"].bottom = plataforma.rect.top + 5
                self.puede_saltar = True
                break

    def updateBoss(self, pantalla, piso, lista_plataformas, personaje, lados_rectangulos, rectangulo_personaje, puede_saltar):

        #Tiempo
        self.tiempo_actual_golpe = pygame.time.get_ticks()
        self.tiempo_actual_ulti = pygame.time.get_ticks()
        self.tiempo_transcurrido_segundos = (self.tiempo_actual_golpe - self.tiempo_inicial) / 1000 
        self.tiempo_transcurrido_segundos = (self.tiempo_actual_ulti - self.tiempo_inicial) / 1000 
        




        if(self.realiza_ulti == False):
            if(self.golpe_realizado == True):
                if self.tiempo_transcurrido_segundos >= self.duracion_temporizador_golpe:
                    print("pasaron 5 seugnos")
                    self.golpe_realizado = False
                    self.tiempo_inicial = self.tiempo_actual_golpe

        if self.tiempo_transcurrido_segundos >= self.duracion_temporizador_ulti and not self.realiza_ulti:
            print("Hace ulti")
            self.realiza_ulti = True
            self.tiempo_inicial = self.tiempo_actual_ulti
            self.ultima_ulti = self.tiempo_actual_ulti

        if self.realiza_ulti:
            self.que_hace = "ulti"
            if self.lados_boss["main"].colliderect(personaje.lados["main"]):
                for lado in rectangulo_personaje:
                    if self.que_hace == "camina_derecha":
                        rectangulo_personaje["main"].x += 30
                        rectangulo_personaje["bottom"].x += 30
                        rectangulo_personaje["left"].x += 30
                        rectangulo_personaje["top"].x += 30
                        rectangulo_personaje["right"].x += 30

                        rectangulo_personaje["main"].y -= 5
                        rectangulo_personaje["bottom"].y -= 5
                        rectangulo_personaje["left"].y -= 5
                        rectangulo_personaje["top"].y -= 5
                        rectangulo_personaje["right"].y -= 5
                    else:
                        rectangulo_personaje["main"].x -= 30
                        rectangulo_personaje["bottom"].x -= 30
                        rectangulo_personaje["left"].x -= 30
                        rectangulo_personaje["top"].x -= 30
                        rectangulo_personaje["right"].x -= 30

                        rectangulo_personaje["main"].y -= 5
                        rectangulo_personaje["bottom"].y -= 5
                        rectangulo_personaje["left"].y -= 5
                        rectangulo_personaje["top"].y -= 5
                        rectangulo_personaje["right"].y -= 5

        if self.realiza_ulti and (self.tiempo_actual_ulti - self.ultima_ulti) / 1000 >= 4:
            print("Desactivando ulti")
            self.realiza_ulti = False

        if self.que_hace == "dañado":
            self.animar(pantalla, "boss_dañado")

        elif self.que_hace == "quieto":
            self.animar(pantalla, "quieto")

        elif self.que_hace == "camina_derecha":
            self.animar(pantalla, "camina_derecha")

        elif self.que_hace == "camina_izquierda":
            self.animar(pantalla, "camina_izquierda")

        elif self.que_hace == "golpeando":
            self.animar(pantalla, "ataca_derecha")

        elif self.que_hace == "ulti":
            self.animar(pantalla, "realiza_ulti")


        for lado in self.lados_boss:
            rectangulo = self.lados_boss[lado]

        numero_aleatorio = random.randrange(1, 10)
        if(puede_saltar == True):
            if(numero_aleatorio == 3):
                self.lados_boss["main"].y -= 45
                self.lados_boss["bottom"].y -= 45
                self.lados_boss["left"].y -= 45
                self.lados_boss["top"].y -= 45
                self.lados_boss["right"].y -= 45

        if(self.realiza_ulti == False):
            if self.lados_boss["main"].colliderect(lados_rectangulos[0]["right"]) and self.direccion == 1 :
                self.direccion = -1
                self.mover(self.velocidad_enemigo * -1)
                self.que_hace = "camina_izquierda"
            
            
            if self.lados_boss["main"].colliderect(lados_rectangulos[1]["main"]) and self.direccion == -1 :
                self.direccion = 1
                self.mover(self.velocidad_enemigo * 1)
                self.que_hace = "camina_derecha"


            if(rectangulo.right < 1280 - self.velocidad_enemigo and self.direccion == 1):
                self.mover(self.velocidad_enemigo)
                self.que_hace = "camina_derecha"
                if(self.golpe_realizado == False):
                    self.golpear_personaje_derecha(personaje, pantalla, rectangulo_personaje)
                
            if rectangulo.right >= 1280 - self.velocidad_enemigo and self.direccion == 1:
                self.direccion = -1
                self.mover(self.velocidad_enemigo * -1)
                self.que_hace = "camina_izquierda"
                if(self.golpe_realizado == False):
                    self.golpear_personaje_izquierda(personaje, pantalla, rectangulo_personaje)

            elif rectangulo.left > self.velocidad_enemigo and self.direccion == -1:
                self.mover(self.velocidad_enemigo * -1)
                self.que_hace = "camina_izquierda"
                if(self.golpe_realizado == False):
                    self.golpear_personaje_izquierda(personaje, pantalla, rectangulo_personaje)

            elif rectangulo.left <= self.velocidad_enemigo and self.direccion == -1:
                self.direccion = 1
                self.mover(self.velocidad_enemigo)
                self.que_hace = "camina_derecha"
                if(self.golpe_realizado == False):
                    self.golpear_personaje_derecha(personaje, pantalla, rectangulo_personaje)



        self.aplicar_gravedad(piso, lista_plataformas)