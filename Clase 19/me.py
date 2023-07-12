import pygame
from Interfaz.GUI_form_cajita import *
import sys

W, H = 1400, 900
TAMAÑO_PANTALLA = (W, H)
pantalla = pygame.display.set_mode((W, H))
FPS = 18
velocidad_personaje = 10
velocidad_enemigo = 8

form_prueba = FormMenuFinal(pantalla, 0, 0, W, H, "gold", "BLACK", 5, True)

pygame.init()
    
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
    

def abrir_menu(lista_eventos):
    form_prueba.update(lista_eventos)

while True:
    
    RELOJ.tick(FPS)

    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    abrir_menu(lista_eventos)

    pygame.display.update()
