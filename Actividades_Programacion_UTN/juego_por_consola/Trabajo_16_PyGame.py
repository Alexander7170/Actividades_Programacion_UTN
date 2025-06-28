from Modulo_juego import *
from Datos_juego_por_consola import *
from constantes import *
from colores import DARKKHAKI
import pygame
"""
blit: funde la imagen en una superficie
pygame.display.flip(): actualiza todos los cambios en la pantalla
pygame.display.set_caption("NOMbreJUEGO")
pygame.Rect
= imagen.get_rect() = obtiene el tamaño de la imagen
imagen_mosca.y = cambia coordenada y
imagen_mosca.x = 3 cambia coordenada x
imagen_mosca.height = 3 cambia ancho
imagen_mosca.y = 3 cambia alto
.pos = devuele de la lista de eventos, la posicion donde se hizo el click, en forma de tupla
escalar la imagen importada: pygame.transform.scale()
blit() funde
colisiono.colliderect(con_este)
"""
pygame.init()
COLOR_NEGRO = (0,0,0)

pantalla = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA]) #ABRO UNA VENTANA
icono = pygame.image.load("Imagenes/icono_juego.png") # ASIGNO NOMBRE DE LA VENTANA ABIERTA
icono = pygame.transform.scale(icono,(64,64))
pygame.display.set_icon(icono)

figura_titulo = pygame.image.load("Imagenes/Imagen_Titulo.png")
capsula_amarilla = pygame.image.load("Imagenes/figura_capsula_amarilla.png")
capsula_roja = pygame.image.load("Imagenes/figura_capsula_amarilla.png")
capsula_azul = pygame.image.load("Imagenes/figura_capsula_azul.png")
capsula_verde = pygame.image.load("Imagenes/figura_capsula_verde.png")
fondo_inicio_pantalla = pygame.image.load("Imagenes/fondo_inicio_pantalla.png")


fuente_subtitulos = pygame.font.SysFont("Comic Sans MS",50)
fuente_titulo = pygame.font.SysFont("Cooper Black",65)
fuentes = pygame.font.get_fonts()
texto_jugar = fuente_subtitulos.render("J u g a r", True , COLOR_NEGRO,)
texto_score = fuente_subtitulos.render("S c o r e", True, COLOR_NEGRO)
texto_salir = fuente_subtitulos.render("S a l i r", True, COLOR_NEGRO)

texto_titulo_a = fuente_titulo.render("Escaleras",True, COLOR_NEGRO)
texto_titulo_b = fuente_titulo.render("Y",True, COLOR_NEGRO)
texto_titulo_c = fuente_titulo.render("Serpientes",True, COLOR_NEGRO)

texto_pedir_nombre = fuente_subtitulos.render(MENSAJE_PEDIR_NOMBRE,True,COLOR_NEGRO)
rect_capsula_verde = capsula_verde.get_rect()

rect_capsula_amarilla = capsula_amarilla.get_rect() # # DEVUELVE UNA SUPERFICIE INVICIBLE, UNA ZONA CON UN ALTO Y ANCHO DE LA IMAGEN
rect_capsula_roja = capsula_roja.get_rect() # DEVUELVE UNA SUPERFICIE INVICIBLE, UNA ZONA CON UN ALTO Y ANCHO DE LA IMAGEN
rect_capsula_azul = capsula_azul.get_rect() # DEVUELVE UNA SUPERFICIE INVICIBLE, UNA ZONA CON UN ALTO Y ANCHO DE LA IMAGEN
rect_capsula_verde.x = 250 # UBICO ESA ZONA INVICIBLE EN LA COORDENADA X
rect_capsula_verde.y = 320 # UBICO ESA ZONA INVICIBLE EN LA COORDENADA Y
rect_capsula_amarilla.x = 250 # CAMBIO SU EJE X
rect_capsula_amarilla.y = 420 # UBICO ESA ZONA INVICIBLE EN LA COORDENADA Y
rect_capsula_roja.x = 250 # CAMBIO SU EJE X
rect_capsula_roja.y = 520 # UBICO ESA ZONA INVICIBLE EN LA COORDENADA Y
py

pygame.display.set_caption("Trivia")
correr_juego = True
while correr_juego:
    for event in pygame.event .get():
        if event.type == pygame.QUIT:
            correr_juego = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = event.pos
            if rect_capsula_verde.collidepoint(posicion_click):
                jugar = True
                escribiendo = True
                nombre = ""
                while jugar:
                    while escribiendo:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                jugar = False
                                escribiendo = False
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    escribiendo = False
                                    jugar = False
                                    print("nombre guardado")
                                elif event.key == pygame.K_BACKSPACE:
                                    print("borrado")
                                    nombre = nombre[0:-1]
                                elif len(nombre) <= 13:
                                    nombre += event.unicode
                            pantalla.blit(fondo_inicio_pantalla,(0,0))
                            pygame.draw.line(pantalla,COLOR_NEGRO,(200,250),(600,250),5)
                            pygame.draw.rect(pantalla,COLOR_GRIS,(190,40,460,100),5)
                            texto_nombre = fuente_subtitulos.render(nombre,True,(0,0,0))
                            pantalla.blit(texto_nombre,(200,180))
                            pantalla.blit(texto_pedir_nombre,(200,50))
                            pygame.display.flip()
            elif rect_capsula_amarilla.collidepoint(posicion_click):
                print("score")
            elif rect_capsula_roja.collidepoint(posicion_click):
                print("salir")
                correr_juego = False
    pantalla.blit(fondo_inicio_pantalla,(0,0))
    pantalla.blit(figura_titulo,(0,0))
    pantalla.blit(texto_titulo_a,(230,15))
    pantalla.blit(texto_titulo_b,(360,75))
    pantalla.blit(texto_titulo_c,(230,130))
    pantalla.blit(capsula_verde,(rect_capsula_verde)) # FUNDO LA IMAGEN, LA IMPRIMO EXACTAMENTE EN LA COORDENADA DONDE UBIQUE LA ZONA INVICIBLE
    pantalla.blit(capsula_amarilla,(rect_capsula_amarilla))
    pantalla.blit(capsula_roja,(rect_capsula_roja))
    pantalla.blit(texto_jugar,(320,320))
    pantalla.blit(texto_score,(320,420))
    pantalla.blit(texto_salir,(320,520))
    pygame.display.flip()

pygame.quit()