import pygame
from settings import *

class Plataforma():
    def __init__(self, x, y, width, height, path_image):
        super().__init__()
        self.image = pygame.image.load(path_image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y


class Rectangulo():
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y
        self.lados_rectangulo = obtener_rectangulos(self.rect)


class impulso():
    def __init__(self, x, y, width, height, path_image):
        super().__init__()
        self.image = pygame.image.load(path_image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect_impulso = pygame.Rect(x, y, width, height)
        self.lados_impulso = obtener_rectangulos(self.rect_impulso)
        self.rect_impulso.x = x
        self.rect_impulso.y = y

    def update_plataforma_impulso(self, personaje):
        if(self.lados_impulso["main"].colliderect(personaje.lados["main"])):
            personaje.desplazamiento_y -= 5
