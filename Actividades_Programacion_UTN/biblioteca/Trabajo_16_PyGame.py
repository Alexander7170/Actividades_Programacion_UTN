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

colisiono.colliderect(con_este)
"""
ANCHO_VENTANA = 500

LARGO_VENTANA = 500
iniciar_juego = True
