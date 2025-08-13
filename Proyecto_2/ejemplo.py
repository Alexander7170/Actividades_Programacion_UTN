import pygame
from analisis import *
from data import *
from renderizar import *
pygame.init()
pantalla = pygame.display.set_mode((1200,800))
flag = True
fondo = pygame.image.load("Imagenes/carta.png")
{"estilos":{"username":{"fuente": "Arial", 
                        "color": "negro",                     "tamaño": 30}}}



data_logica_cartas = get_data_logica_cartas()
guardar_progreso("data_game",data_logica_cartas)
img_cartas = get_img_cartas(data_logica_cartas)
tiempo = pygame.time.Clock()
flag_2 = False
while flag:
    pantalla.fill((0,0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            flag = False

    
    tiempo.tick(60)
    pygame.display.flip()
    