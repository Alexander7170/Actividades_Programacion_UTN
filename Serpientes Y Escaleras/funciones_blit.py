import pygame
pygame.init()

COLOR_NEGRO = (0,0,0)
def imprimir_configuracion(pantalla:pygame.Surface, configuracion:dict):
    """
    Funcion que imprime en una superficie, las imagenes de configuracion con sus respectivas ubicaciones ya definidas
    
    parametros:
        pantalla: la superficie donde fundiremos las imagenes con sus ubicaciones y la linea y el rect
        configuracion: una lista donde sus elementos son diccionarios, los cuales cada diccionario
                    tiene sus respectivas imagenes, con sus respectivas coordenadas de fundicion en pantalla
    """
    for opcion in configuracion:
        pantalla.blit(configuracion[opcion]["imagen_fondo"],configuracion[opcion]["ubicacion_fondo"])
        pantalla.blit(configuracion[opcion]["imagen_texto"], configuracion[opcion]["ubicacion_texto"])

def ver_pantalla_menu(pantalla:pygame.Surface, imagenes:dict, rects:dict):
    pantalla.blit(imagenes["imagen_portada"],(0,0))
    pantalla.blit(imagenes["imagen_jugar"],rects["rect_jugar"])
    pantalla.blit(imagenes["imagen_score"],rects["rect_score"])
    pantalla.blit(imagenes["imagen_salir"],rects["rect_salir"])

def ver_pantalla_fin_juego(pantalla:pygame.Surface,datos:dict,imagenes_fijas:dict):
    pantalla.blit(imagenes_fijas["texto_fin_juego"],(280,100))
    pantalla.blit(datos["imagenes_fin_juego"]["texto_nombre"],(150,200))
    pantalla.blit(datos["imagenes_fin_juego"]["texto_puntuacion"],(150,300))

def ver_pantalla_jugando(pantalla:pygame.Surface, datos:dict, imagenes_fijas:dict, rects:dict):
    pregunta_opciones = datos["imagen_pregunta_opciones"]
    pantalla.blit(imagenes_fijas["fondo_cronometro"],(0,500))
    pantalla.blit(imagenes_fijas["fondo_opcion"], rects["opcion_a"])
    pantalla.blit(imagenes_fijas["fondo_opcion"], rects["opcion_b"])
    pantalla.blit(imagenes_fijas["fondo_opcion"], rects["opcion_c"])
    pantalla.blit(imagenes_fijas["fondo_pregunta"],(100,500))
    pantalla.blit(datos["imagen_texto_cronometro"],(20,500))
    pantalla.blit(pregunta_opciones["texto_pregunta"],(140,520))
    pantalla.blit(pregunta_opciones["texto_opcion_a"],(rects["opcion_a"].x + 10, rects["opcion_a"].y + 10))
    pantalla.blit(pregunta_opciones["texto_opcion_b"],(rects["opcion_b"].x + 10, rects["opcion_b"].y + 10))
    pantalla.blit(pregunta_opciones["texto_opcion_c"],(rects["opcion_c"].x + 10, rects["opcion_c"].y + 10))
    imprimir_configuracion(pantalla,datos["configuracion_tablero"])

def ver_pantalla_escribiendo(pantalla:pygame.Surface, datos:dict):
    pantalla.blit(datos["fondo_nombre_us"],(200,100))
    pantalla.blit(datos["texto_peticion"],(240,20))
    pantalla.blit(datos["imagen_texto_nombre_us"],(250,100))

def ver_pantalla_score(pantalla:pygame.Surface, datos:dict, imagenes_fijas:dict, rect:pygame.Surface):
    pygame.draw.line(pantalla,COLOR_NEGRO,(0,100),(900,100),4)
    pygame.draw.line(pantalla,COLOR_NEGRO,(400,0),(400,700),4)

    matriz_imagenes = datos["matriz_imagenes"]
    ubicaciones_matriz = datos["matriz_ubicaciones"]

    for i in range(len(matriz_imagenes)):
        for j in range(len(matriz_imagenes[i])):
            pantalla.blit(matriz_imagenes[i][j],ubicaciones_matriz[i][j])
    pantalla.blit(imagenes_fijas["texto_nombre"],(40,50))
    pantalla.blit(imagenes_fijas["volver_menu"],rect)
    pantalla.blit(imagenes_fijas["texto_puntuacion"], (500,50))
