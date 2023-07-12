import pygame
from pygame.locals import *
from nivel_uno import *
from nivel_dos import *
from nivel_tres import *
from nivel import *

class ControlNiveles:
    def __init__(self, pantalla) -> None:

        self._slave = pantalla
        self.niveles = {"nivel_uno": NivelUno, "nivel_dos": NivelDos, "nivel_tres": NivelTres}

    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)
    
