from modulo import *
import pygame
pygame.init()

pygame.display.set_caption("Trivia")
pantalla = pygame.display.set_mode((900,700))
fondo_inicio_pantalla = pygame.image.load("Imagenes/fondo_inicio_pantalla.png")
velocidad_juego = pygame.time.Clock()
datos_escribiendo = obtener_datos_escribiendo()

pygame.mixer.music.load("pretty-afternoon.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

estado_juego = {"correr_juego" : True, "pantalla_actual":"escribiendo", "actualizar_datos":True}

inicializacion = {"jugando":True, "viendo_menu": True, "viendo_score":True}
while estado_juego["correr_juego"]:

    lista_eventos = pygame.event.get()
    analizar_correr_juego(estado_juego,lista_eventos)
    pantalla.blit(fondo_inicio_pantalla,(0,0))

    if estado_juego ["pantalla_actual"] == "escribiendo":
        pantalla_escribiendo(pantalla, estado_juego, datos_escribiendo,lista_eventos)

    elif estado_juego["pantalla_actual"] == "viendo_menu":
        if inicializacion["viendo_menu"]:
            imagenes_fijas_menu = obtener_imagenes_pantalla_menu()
            rects_menu = obtener_rects_menu(imagenes_fijas_menu)
            inicializacion["viendo_menu"] = False
        pantalla_menu(pantalla, estado_juego, imagenes_fijas_menu, rects_menu, lista_eventos)

    elif estado_juego["pantalla_actual"] == "jugando":
        if inicializacion["jugando"]:
            imagenes_fijas_jugando = obtener_imagenes_fijas_jugando()
            rects_jugando = obtener_rects_jugando(imagenes_fijas_jugando)
            inicializacion["jugando"] = False
        if estado_juego["actualizar_datos"]:
            datos_jugando = obtener_datos_jugando(datos_escribiendo, imagenes_fijas_jugando)
            estado_juego["actualizar_datos"] = False
        pantalla_jugando(pantalla,estado_juego,datos_jugando,imagenes_fijas_jugando,rects_jugando,lista_eventos)

    elif estado_juego["pantalla_actual"] == "viendo_score":
        if inicializacion["viendo_score"]:
            imagenes_fijas_score = obtener_imagenes_fijas_score()
            rect_score = obtener_rects_score(imagenes_fijas_score)
            estado_juego["inicializacion"] = False
        if estado_juego["actualizar_datos"]:
            datos_score = obtener_datos_score("score.csv")
            estado_juego["actualizar_datos"] = False
        pantalla_score(pantalla,estado_juego,datos_score,imagenes_fijas_score,rect_score,lista_eventos)

    velocidad_juego.tick(60)
    pygame.display.flip()
pygame.mixer.music.stop()
pygame.quit()