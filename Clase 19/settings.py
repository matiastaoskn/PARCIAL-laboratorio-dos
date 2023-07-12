import pygame

def rescalarar_img(lista_imagenes, tamaño):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []

    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

def obtener_rectangulos(principal)-> dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 6, principal.width, 6)
    diccionario["right"] = pygame.Rect(principal.right -2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 6)
    return diccionario

#Personaje
personaje_quieto = [pygame.image.load("Recursos\Quieto/0.png")]
personaje_camina_derecha = [
                    pygame.image.load("Recursos/Camina/Adelante/1.png"),
                    pygame.image.load("Recursos/Camina/Adelante/2.png"),
                    pygame.image.load("Recursos/Camina/Adelante/3.png"),
                    pygame.image.load("Recursos/Camina/Adelante/4.png"),
                    ]
personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha, True, False)
personaje_salta_derecha = [pygame.image.load("Recursos\Salta_derecha/0.png"),
                           #pygame.image.load("Recursos\Salta_derecha/1.png")
                            ]
personaje_salta_izquierda = [pygame.image.load("Recursos\Salta_izquierda/0.png"),
                             #pygame.image.load("Recursos\Salta_izquierda/1.png")
                             ]
personaje_golpe_derecha = [pygame.image.load("Recursos/ataca/1.png"),
                     pygame.image.load("Recursos/ataca/2.png"),
                     pygame.image.load("Recursos/ataca/3.png"),
                     pygame.image.load("Recursos/ataca/4.png"),
                     pygame.image.load("Recursos/ataca/5.png"),
                     pygame.image.load("Recursos/ataca/6.png")]
personaje_golpe_izquierda = girar_imagenes(personaje_golpe_derecha, True, False)

#Enemigo
enemigo_camina_derecha =  [
                pygame.image.load("Recursos\Camina\Adelante\Enemigo1/1.png"),
                pygame.image.load("Recursos\Camina\Adelante\Enemigo1/2.png"),
                pygame.image.load("Recursos\Camina\Adelante\Enemigo1/3.png"),
                pygame.image.load("Recursos\Camina\Adelante\Enemigo1/4.png"),
                   
                pygame.image.load("Recursos\Camina\Adelante\Enemigo1/5.png")
                ]
enemigo_camina_izquierda = girar_imagenes(enemigo_camina_derecha, True, False)
enemigo_quieto = [pygame.image.load("Recursos\Quieto/0.png")]
enemigo_ataca_derecha = [pygame.image.load("Recursos\Ataca\Enemigos/1.png"),
                 pygame.image.load("Recursos\Ataca\Enemigos/2.png"),
                 pygame.image.load("Recursos\Ataca\Enemigos/3.png"),
                 pygame.image.load("Recursos\Ataca\Enemigos/4.png"),
                 pygame.image.load("Recursos\Ataca\Enemigos/5.png"),
                 pygame.image.load("Recursos\Ataca\Enemigos/6.png")]
enemigo_ataca_izquierda = girar_imagenes(enemigo_ataca_derecha, True, False)
enemigo_daño = [pygame.image.load("Recursos\Daño/0.png")]
#Boss
#Nivel Uno
enemigos_boss_uno_camina_derecha = [pygame.image.load("Recursos\Boss/nivel_uno\corre/0.png"),
                                    pygame.image.load("Recursos\Boss/nivel_uno\corre/1.png"),
                                    pygame.image.load("Recursos\Boss/nivel_uno\corre/2.png"),
                                    pygame.image.load("Recursos\Boss/nivel_uno\corre/3.png"),
                                    pygame.image.load("Recursos\Boss/nivel_uno\corre/4.png"),
                                    pygame.image.load("Recursos\Boss/nivel_uno\corre/5.png"),
                                    pygame.image.load("Recursos\Boss/nivel_uno\corre/6.png"),]
enemigos_boss_uno_camina_izquierda = girar_imagenes(enemigos_boss_uno_camina_derecha, True, False)
enemigos_boss_uno_ulti = [pygame.image.load(r"Recursos\Boss/nivel_uno/ulti/0.png"),
                          pygame.image.load(r"Recursos\Boss/nivel_uno/ulti/1.png"),
                          pygame.image.load(r"Recursos\Boss/nivel_uno/ulti/2.png"),
                          pygame.image.load(r"Recursos\Boss/nivel_uno/ulti/3.png"),
                          pygame.image.load(r"Recursos\Boss/nivel_uno/ulti/4.png"),
                          pygame.image.load(r"Recursos\Boss/nivel_uno/ulti/5.png"),
                          pygame.image.load(r"Recursos\Boss/nivel_uno/ulti/6.png")]
enemigos_boss_uno_dañado = [pygame.image.load(r"Recursos\Boss/nivel_uno\dañado/0.png")]


#Enemigo2
enemigo_dos_camina_derecha = [pygame.image.load("Recursos\Camina\Adelante\Enemigo2/1.png"),
                              pygame.image.load("Recursos\Camina\Adelante\Enemigo2/2.png"),
                              pygame.image.load("Recursos\Camina\Adelante\Enemigo2/3.png"),
                              pygame.image.load("Recursos\Camina\Adelante\Enemigo2/4.png"),
                              pygame.image.load("Recursos\Camina\Adelante\Enemigo2/5.png"),
                              pygame.image.load("Recursos\Camina\Adelante\Enemigo2/6.png"),
                              pygame.image.load("Recursos\Camina\Adelante\Enemigo2/7.png")]
enemigo_dos_camina_izquierda = girar_imagenes(enemigo_dos_camina_derecha, True, False)
enemigo_dos_quieto = [pygame.image.load("Recursos\Quieto/0.png")]
enemigo_dos_ataca_derecha = [pygame.image.load("Recursos\Ataca\Enemigo2/1.png"),
                             pygame.image.load("Recursos\Ataca\Enemigo2/2.png"),
                             pygame.image.load("Recursos\Ataca\Enemigo2/3.png"),
                             pygame.image.load("Recursos\Ataca\Enemigo2/4.png"),
                             pygame.image.load("Recursos\Ataca\Enemigo2/5.png"),
                             pygame.image.load("Recursos\Ataca\Enemigo2/6.png"),
                             pygame.image.load("Recursos\Ataca\Enemigo2/7.png")]
enemigo_dos_ataca_izquierda = girar_imagenes(enemigo_dos_ataca_derecha, True, False)
enemigo_dos_daño = [pygame.image.load("Recursos\Daño/nivel_Dos/0.png")]
#Boss
#Nivel Dos
enemigos_boss_dos_camina_derecha = [pygame.image.load("Recursos\Boss/nivel_dos\RUN\RUN_000.png"),
                                    pygame.image.load("Recursos\Boss/nivel_dos\RUN\RUN_001.png"),
                                    pygame.image.load("Recursos\Boss/nivel_dos\RUN\RUN_002.png"),
                                    pygame.image.load("Recursos\Boss/nivel_dos\RUN\RUN_003.png"),
                                    pygame.image.load("Recursos\Boss/nivel_dos\RUN\RUN_004.png"),
                                    pygame.image.load("Recursos\Boss/nivel_dos\RUN\RUN_005.png"),
                                    pygame.image.load("Recursos\Boss/nivel_dos\RUN\RUN_006.png"),
                                    ]
enemigos_boss_dos_camina_izquierda = girar_imagenes(enemigos_boss_dos_camina_derecha, True, False)
enemigos_boss_dos_ataca_derecha = [pygame.image.load("Recursos\Boss/nivel_dos\ATTAK\ATTAK_000.png"),
                                    pygame.image.load("Recursos\Boss/nivel_dos\ATTAK\ATTAK_001.png"),
                                    pygame.image.load("Recursos\Boss/nivel_dos\ATTAK\ATTAK_002.png"),
                                    pygame.image.load("Recursos\Boss/nivel_dos\ATTAK\ATTAK_003.png"),
                                    pygame.image.load("Recursos\Boss/nivel_dos\ATTAK\ATTAK_004.png"),
                                    pygame.image.load("Recursos\Boss/nivel_dos\ATTAK\ATTAK_005.png"),
                                    pygame.image.load("Recursos\Boss/nivel_dos\ATTAK\ATTAK_006.png")
                                    ]
enemigos_boss_dos_ataca_izquierda = girar_imagenes(enemigos_boss_dos_ataca_derecha, True, False)
enemigos_boss_dos_ulti = [pygame.image.load("Recursos\Boss/nivel_dos\HURT\HURT_000.png"),
                          pygame.image.load("Recursos\Boss/nivel_dos\HURT\HURT_001.png"),
                          pygame.image.load("Recursos\Boss/nivel_dos\HURT\HURT_002.png"),
                          pygame.image.load("Recursos\Boss/nivel_dos\HURT\HURT_003.png"),
                          pygame.image.load("Recursos\Boss/nivel_dos\HURT\HURT_004.png"),
                          pygame.image.load("Recursos\Boss/nivel_dos\HURT\HURT_005.png"),
                          pygame.image.load("Recursos\Boss/nivel_dos\HURT\HURT_006.png")
                          ]
enemigos_boss_dos_dañado = [pygame.image.load("Recursos\Boss/nivel_dos\dañado/0.png")]

#Enemigo3
enemigo_tres_camina_derecha = [pygame.image.load("Recursos\Camina\Adelante\Enemigo3/1.png"),
                              pygame.image.load("Recursos\Camina\Adelante\Enemigo3/2.png"),
                              pygame.image.load("Recursos\Camina\Adelante\Enemigo3/3.png"),
                              pygame.image.load("Recursos\Camina\Adelante\Enemigo3/4.png"),
                              pygame.image.load("Recursos\Camina\Adelante\Enemigo3/5.png"),]
enemigo_tres_camina_izquierda = girar_imagenes(enemigo_tres_camina_derecha, True, False)
enemigo_tres_quieto = [pygame.image.load("Recursos\Quieto/0.png")]
enemigo_tres_ataca_derecha = [pygame.image.load("Recursos\Ataca\enemigo3/1.png"),
                              pygame.image.load("Recursos\Ataca\enemigo3/2.png"),
                              pygame.image.load("Recursos\Ataca\enemigo3/3.png"),
                              pygame.image.load("Recursos\Ataca\enemigo3/4.png"),
                              pygame.image.load("Recursos\Ataca\enemigo3/5.png"),]
enemigo_tres_ataca_izquierda = girar_imagenes(enemigo_tres_ataca_derecha, True, False)
enemigo_tres_daño = [pygame.image.load("Recursos\Daño/nivel_tres/0.png")]

#Boss
#Nivel Tres
enemigos_boss_tres_camina_derecha = [pygame.image.load("Recursos\Boss/nivel_tres\RUN\RUN_000.png"),
                                     pygame.image.load("Recursos\Boss/nivel_tres\RUN\RUN_001.png"),
                                     pygame.image.load("Recursos\Boss/nivel_tres\RUN\RUN_002.png"),
                                     pygame.image.load("Recursos\Boss/nivel_tres\RUN\RUN_003.png"),
                                     pygame.image.load("Recursos\Boss/nivel_tres\RUN\RUN_004.png"),
                                     pygame.image.load("Recursos\Boss/nivel_tres\RUN\RUN_005.png"),
                                     pygame.image.load("Recursos\Boss/nivel_tres\RUN\RUN_006.png"),]
enemigos_boss_tres_camina_izquierda = girar_imagenes(enemigos_boss_tres_camina_derecha, True, False)
enemigos_boss_tres_ataca_derecha = [pygame.image.load("Recursos\Boss/nivel_tres\ATTAK\ATTAK_000.png"),
                                    pygame.image.load("Recursos\Boss/nivel_tres\ATTAK\ATTAK_001.png"),
                                    pygame.image.load("Recursos\Boss/nivel_tres\ATTAK\ATTAK_002.png"),
                                    pygame.image.load("Recursos\Boss/nivel_tres\ATTAK\ATTAK_003.png"),
                                    pygame.image.load("Recursos\Boss/nivel_tres\ATTAK\ATTAK_004.png"),
                                    pygame.image.load("Recursos\Boss/nivel_tres\ATTAK\ATTAK_005.png"),
                                    pygame.image.load("Recursos\Boss/nivel_tres\ATTAK\ATTAK_006.png")]
enemigos_boss_tres_ataca_izquierda = girar_imagenes(enemigos_boss_tres_ataca_derecha, True, False)
enemigos_boss_tres_ulti = [pygame.image.load("Recursos\Boss/nivel_tres\HURT\HURT_000.png"),
                          pygame.image.load("Recursos\Boss/nivel_tres\HURT\HURT_001.png"),
                          pygame.image.load("Recursos\Boss/nivel_tres\HURT\HURT_002.png"),
                          pygame.image.load("Recursos\Boss/nivel_tres\HURT\HURT_003.png"),
                          pygame.image.load("Recursos\Boss/nivel_tres\HURT\HURT_004.png"),
                          pygame.image.load("Recursos\Boss/nivel_tres\HURT\HURT_005.png"),
                          pygame.image.load("Recursos\Boss/nivel_tres\HURT\HURT_006.png"),]
enemigos_boss_tres_dañado = [pygame.image.load("Recursos\Boss/nivel_tres\dañado/0.png")]

corazones_0 = ("Recursos/Corazones/4.png")
corazones_3 = ("Recursos\Corazones\corazones.png")
corazones_2 = ("Recursos\Corazones/2.png")
corazones_1 = ("Recursos\Corazones/3.png")

flecha_derecha = [pygame.image.load("Recursos\Menu\espada.png")]
flecha_izquierda = [pygame.image.load("Recursos\Menu\espada_izquierda.png")]


