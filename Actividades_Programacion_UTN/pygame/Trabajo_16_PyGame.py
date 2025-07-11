from datos_pygame import *
from consola.Modulo_juego import *
from modulo_pygame import *
from trivia import *
from copy import deepcopy
from configuraciones import *
import pygame

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Trivia")

tiempo_segundos = pygame.USEREVENT
velocidad_juego = pygame.time.Clock()

pygame.mixer.music.load("pretty-afternoon.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

configuracion_pantalla_escribiendo = obtener_configuracion_peticion()
configuracion_texto_nombre = obtener_configuracion_texto_nombre(nombre_usuario)
estado_pantalla = {CORRER_JUEGO:True, VIENDO_MENU: False, VIENDO_SCORE: False, JUGANDO: False, ESCRIBIENDO_NOMBRE: True }
inicializacion = {VIENDO_MENU: True, VIENDO_SCORE:False, JUGANDO:False}

while estado_pantalla[CORRER_JUEGO]:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            estado_pantalla[CORRER_JUEGO] = False
            estado_pantalla[ESCRIBIENDO_NOMBRE] = False
    
    pantalla.blit(fondo_inicio_pantalla,(0,0))

    if estado_pantalla[ESCRIBIENDO_NOMBRE]:
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                nombre_usuario = analizar_tecla(evento,nombre_usuario,MAXIMO_CARACTERES,estado_pantalla)
                configuracion_texto_nombre = obtener_configuracion_texto_nombre(nombre_usuario)
        imprimir_configuracion(pantalla, configuracion_texto_nombre)
        imprimir_configuracion(pantalla, configuracion_pantalla_escribiendo)

    if estado_pantalla[VIENDO_MENU]:
        if inicializacion[VIENDO_MENU]:
            rects_menu = get_rects_menu()
            configuracion_pantalla_menu = obtener_configuracion_menu(rects_menu)
            inicializacion[VIENDO_MENU] = False
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                cambiar_estado_pantalla_click(rects_menu, evento, estado_pantalla, inicializacion)
        imprimir_configuracion(pantalla, configuracion_pantalla_menu)

    if estado_pantalla[JUGANDO]:
        if inicializacion[JUGANDO]:
            elegir_pregunta = True
            fin_juego = False
            indice_usuario = PUNTO_DE_PARTIDA
            respuesta_usuario = ""
            cronometro = 0
            rects_jugar = get_rects_jugar()
            configuracion_pantalla_juego_fijo = obtener_configuracion_juego_fijo(rects_jugar)
            configuracion_cronometro = obtener_configuracion_texto_cronometro(str(cronometro))
            copia_preguntas = deepcopy(preguntas)
            pygame.time.set_timer(tiempo_segundos,1000)
            
            configuracion_tablero = obtener_configuracion_tablero(TABLERO,indice_usuario)
            inicializacion[JUGANDO] = False

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                respuesta_usuario, coliciono = analizar_collidepoint_jugar(rects_jugar, estado_pantalla, evento, respuesta_usuario)
                if estado_pantalla[VIENDO_MENU]:
                    pygame.time.set_timer(tiempo_segundos, 0)
                    guardar_score(nombre_usuario,indice_usuario)
            if evento.type == tiempo_segundos:
                cronometro += 1
                configuracion_cronometro = obtener_configuracion_texto_cronometro(str(cronometro))

        if not fin_juego:

            if elegir_pregunta:
                pregunta = manejar_pregunta(copia_preguntas)
                configuracion_preguntas = obtener_configuracion_preguntas_texto(pregunta,rects_jugar)
                elegir_pregunta = False

            if coliciono or cronometro == TIEMPO_MAXIMO:
                acerto = verificar_respuesta(pregunta,respuesta_usuario,CLAVE_RESPUESTA_CORRECTA)
                indice_usuario = jugar_turno(indice_usuario,TABLERO,acerto)
                fin_juego = verificar_fin_juego(indice_usuario,TABLERO,copia_preguntas)
                coliciono = False
                elegir_pregunta = True
                cronometro = 0
                configuracion_tablero = obtener_configuracion_tablero(TABLERO,indice_usuario)
                configuracion_cronometro = obtener_configuracion_texto_cronometro(str(cronometro))
                pygame.time.set_timer(tiempo_segundos, 0)
                if fin_juego:
                    configuracion_pantalla_fin_juego = obtener_configuracion_fin_juego(nombre_usuario,str(indice_usuario))
                else:
                    pygame.time.set_timer(tiempo_segundos, 1000)
            imprimir_configuracion(pantalla,configuracion_pantalla_juego_fijo)
            imprimir_configuracion(pantalla, configuracion_cronometro)
            imprimir_configuracion(pantalla,configuracion_tablero)
            imprimir_configuracion(pantalla, configuracion_preguntas)
        else:
            imprimir_configuracion(pantalla, configuracion_pantalla_fin_juego)   
        
    if estado_pantalla[VIENDO_SCORE]:
        if inicializacion[VIENDO_SCORE]:
            imagenes_score = manejar_score("score.csv")
            rects_score = get_rects_score()
            configuracion_score = obtener_configuracion_score(rects_score)
            inicializacion[VIENDO_SCORE] = False
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                analizar_collidepoint_score(rects_score,estado_pantalla,evento)
        imprimir_score(pantalla,imagenes_score,COLOR_NEGRO)
        imprimir_configuracion(pantalla,configuracion_score)
    velocidad_juego.tick(FPS)
    pygame.display.flip()
pygame.mixer.music.stop()
pygame.quit()