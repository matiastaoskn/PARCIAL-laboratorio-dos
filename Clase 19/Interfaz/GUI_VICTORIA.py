import pygame
from pygame.locals import *

class InterfazNombre:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((400, 200))
        self.reloj = pygame.time.Clock()
        self.nombre = ""

        self.font = pygame.font.Font(None, 32)
        self.texto_intro = self.font.render("Ingrese su nombre:", True, (255, 255, 255))
        self.texto_nombre = self.font.render(self.nombre, True, (255, 255, 255))

        self.input_rect = pygame.Rect(50, 100, 300, 32)
        self.color_activo = pygame.Color("lightskyblue3")
        self.color_inactivo = pygame.Color("gray15")
        self.color_actual = self.color_inactivo

        self.ingresando_nombre = True

    def run(self):
        while self.ingresando_nombre:
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    self.ingresando_nombre = False
                if evento.type == KEYDOWN:
                    if evento.key == K_RETURN:
                        self.ingresando_nombre = False
                    elif evento.key == K_BACKSPACE:
                        self.nombre = self.nombre[:-1]
                    else:
                        self.nombre += evento.unicode

            self.texto_nombre = self.font.render(self.nombre, True, (255, 255, 255))
            self.pantalla.fill((0, 0, 0))

            pygame.draw.rect(self.pantalla, self.color_actual, self.input_rect, 2)
            self.pantalla.blit(self.texto_intro, (50, 50))
            self.pantalla.blit(self.texto_nombre, (self.input_rect.x + 5, self.input_rect.y + 5))

            pygame.display.flip()
            self.reloj.tick(30)

        pygame.quit()