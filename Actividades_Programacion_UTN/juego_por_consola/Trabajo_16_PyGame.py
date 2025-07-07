from Modulo_juego import *
from constantes_juego_consola import *
from constantes_pygame import *
from copy import deepcopy
from modulo_pygame import *
from importaciones_imagenes import *
import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Trivia")
fuente_subtitulos = pygame.font.SysFont("Comic Sans MS",50)
fuente_titulo = pygame.font.SysFont("Cooper Black",60)
fuente_pregunta = pygame.font.SysFont("Arial",30)
fuente_opciones = pygame.font.SysFont("Cooper Black", 25)
estilo_texto_valores = {"fuente":fuente_subtitulos, "color": COLOR_NEGRO }
estilo_texto_opciones = {"fuente": fuente_opciones, "color":COLOR_NEGRO}
fuente_score = pygame.font.SysFont("Comic Sans MS",40)
pygame.mixer.music.load("y2mate.mp3")



nombre_usuario = ""
opcion_usuario = ""
ubicacion_pregunta = (100,500)
cronometro = 0
imagen_texto_cronometro = fuente_subtitulos.render(str(cronometro),True,COLOR_NEGRO)

imagen_texto_nombre = fuente_titulo.render("Nombre",True, COLOR_NEGRO)
imagen_texto_puntuacion = fuente_titulo.render("Puntuacion",True, COLOR_NEGRO)
imagen_texto_nombre_usuario = fuente_subtitulos.render(nombre_usuario,True,COLOR_NEGRO)
imagen_texto_exit = fuente_pregunta.render("Exit",True, COLOR_NEGRO)
imagen_texto_jugar = fuente_subtitulos.render("J u g a r", True , COLOR_NEGRO,)
imagen_texto_score = fuente_subtitulos.render("S c o r e", True, COLOR_NEGRO)
imagen_texto_salir = fuente_subtitulos.render("S a l i r", True, COLOR_NEGRO)
imagen_texto_peticion_nombre = fuente_subtitulos.render(MENSAJE_PEDIR_NOMBRE ,True,COLOR_NEGRO)
imagen_texto_fin_juego = fuente_subtitulos.render(MENSAJE_FIN_PROGRAMA,True,COLOR_NEGRO)
imagen_texto_mensaje_casillero = fuente_subtitulos.render(MENSAJE_INFORMAR_CASILLERO,True,COLOR_NEGRO)
rect_opcion_fin_juego = imagen_casillero_negro.get_rect()
rect_opcion_jugar = imagen_rectangulo_verde.get_rect()
rect_opcion_score = imagen_rectangulo_amarillo.get_rect() 
rect_opcion_salir = imagen_rectangulo_rojo.get_rect() 
rect_opcion_a = imagen_rectangulo_verde.get_rect()
rect_opcion_b = imagen_rectangulo_verde.get_rect()
rect_opcion_c = imagen_rectangulo_verde.get_rect()

rect_opcion_volver_menu = imagen_casillero_negro.get_rect()

rect_opcion_a.topleft = (20,600)
rect_opcion_b.topleft = (320,600)
rect_opcion_c.topleft = (620,600)
rect_opcion_jugar.topleft = (320,320) 
rect_opcion_score.topleft = (320,420)
rect_opcion_salir.topleft = (320,520)

rect_opcion_volver_menu.topleft = (0,0)

ancho_imagen_casillero_azul = casillero_azul.get_width()
alto_imagen_casillero_azul = casillero_azul.get_height()

punto_origen_tablero = {"eje_x":120, "eje_y": 400}
distancia_entre_casilleros = {"distancia_x":ancho_imagen_casillero_azul, "distancia_y": alto_imagen_casillero_azul}
imagenes_casilleros = {"casillero_azul": casillero_azul, "casillero_verde":casillero_verde, "casillero_rojo": casillero_rojo, "casillero_amarillo":casillero_amarillo}

configuracion_cronometro = [{IMAGEN: casillero_negro, UBICACION: (0,400)},
                            {IMAGEN: imagen_texto_cronometro, UBICACION: (0,400)}]

clave_imagen_texto_pregunta = "imagen_texto_pregunta"
clave_imagen_texto_opcion = "imagen_texto_opcion"

configuracion_preguntas_opciones = {
    "pregunta":{"imagen_fondo":imagen_marco_pregunta, "ubicacion_fondo": (50,500)},
    "opcion_a":{"imagen_fondo":imagen_rectangulo_amarillo, "ubicacion_fondo": rect_opcion_a},
    "opcion_b":{"imagen_fondo":imagen_rectangulo_amarillo, "ubicacion_fondo":rect_opcion_b},
    "opcion_c":{"imagen_fondo":imagen_rectangulo_amarillo, "ubicacion_fondo":rect_opcion_c}}

configuracion_pantalla_escribiendo = [{IMAGEN: imagen_texto_peticion_nombre, UBICACION: (200,50)},
                                      {IMAGEN: imagen_texto_nombre_usuario, UBICACION: (190,190)}]

configuracion_menu = [{"imagen_fondo":portada, "ubicacion_fondo": (50,0)},
                      {"imagen_fondo":imagen_rectangulo_verde,"imagen_texto": imagen_texto_jugar, "ubicacion_fondo": rect_opcion_jugar},
                      {"imagen_fondo":imagen_rectangulo_amarillo, "imagen_texto":imagen_texto_score, "ubicacion_fondo":rect_opcion_score},
                      {"imagen_fondo":imagen_rectangulo_rojo, "imagen_texto": imagen_texto_salir, "ubicacion_fondo":rect_opcion_salir}]

timer_segundos = pygame.USEREVENT
reloj = pygame.time.Clock()

rects = {OPCION_JUGAR: rect_opcion_jugar, OPCION_SCORE: rect_opcion_score, OPCION_SALIR:rect_opcion_salir, 
        OPCION_A: rect_opcion_a, OPCION_B: rect_opcion_b, OPCION_C:rect_opcion_c, OPCION_VOLVER_MENU:rect_opcion_volver_menu}

estado_pantalla = {CORRER_JUEGO:True, VIENDO_MENU: False, VIENDO_SCORE: False, JUGANDO: False, ESCRIBIENDO_NOMBRE: True }

inicializacion = {VIENDO_MENU: False, VIENDO_SCORE:False, JUGANDO:False}

configuracion_pantalla_fin_juego = [{IMAGEN:casillero_blanco,UBICACION:(150,100)},
                                    {IMAGEN:imagen_texto_fin_juego,UBICACION:(180,100)},
                                    {UBICACION:(180,200)},
                                    {IMAGEN:imagen_texto_mensaje_casillero,UBICACION:(170,300)},
                                    {UBICACION:(400,400)}]


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
                nombre_usuario = analizar_tecla(evento,nombre_usuario,MAXIMO_CARACTERES,estado_pantalla,inicializacion)
                configuracion_pantalla_escribiendo[1][IMAGEN] = fuente_subtitulos.render(nombre_usuario,True,COLOR_NEGRO)     
        imprimir_menu_escribir(pantalla, configuracion_pantalla_escribiendo ,COLOR_NEGRO,)

    if estado_pantalla[VIENDO_MENU]:
        if inicializacion[VIENDO_MENU]:
            pygame.mixer_music.play(1000)
            pygame.mixer_music.set_volume(0.1)
            inicializacion[VIENDO_MENU] = False
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = evento.pos
                cambiar_estado_pantalla_click(rects, posicion_click, estado_pantalla, inicializacion)
        imprimir_menu(pantalla, configuracion_menu)

    if estado_pantalla[JUGANDO]:

        if inicializacion[JUGANDO]:
            cambiar_pregunta = True
            puso_una_opcion_a_pregunta = False
            indice_usuario = PUNTO_DE_PARTIDA
            respuesta_usuario = ""
            cronometro = 0
            fin_juego = False
            imagen_texto_cronometro = fuente_subtitulos.render(str(cronometro),True,COLOR_NEGRO)
            copia_preguntas = deepcopy(preguntas)
            pygame.time.set_timer(timer_segundos,1000)
            inicializacion[JUGANDO] = False

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = evento.pos
                respuesta_usuario = cambiar_string_click(rects, posicion_click, respuesta_usuario)
                estado_pantalla[VIENDO_MENU] = verificar_colicion_con_click(rects[OPCION_VOLVER_MENU],posicion_click)
                if respuesta_usuario != "" and fin_juego == False and estado_pantalla[VIENDO_MENU] == False:
                    puso_una_opcion_a_pregunta = True

            if evento.type == timer_segundos:
                cronometro += 1
                configuracion_cronometro[1][IMAGEN] = fuente_subtitulos.render(str(cronometro),True,COLOR_NEGRO)
        
        if cambiar_pregunta:
            pregunta = buscar_pregunta(copia_preguntas)
            eliminar_una_pregunta(copia_preguntas,pregunta)
            imagenes_pregunta_opciones = renderizar_valores_dic(pregunta,CLAVE_RESPUESTA_CORRECTA,fuente_pregunta,COLOR_NEGRO)
            modificar_configuracion(configuracion_preguntas_opciones,imagenes_pregunta_opciones)
            cambiar_pregunta = False

        if puso_una_opcion_a_pregunta or cronometro == TIEMPO_MAXIMO:
            acerto = verificar_respuesta(pregunta,respuesta_usuario,CLAVE_RESPUESTA_CORRECTA)
            indice_usuario = mover_usuario(indice_usuario , acerto, MOVERSE_RESPUESTA_CORRECTA, MOVERSE_RESPUESTA_INCORRECTA)
            movimiento_adicional = buscar_movimiento_adicional(TABLERO,indice_usuario)
            indice_usuario = mover_adicional_usuario(indice_usuario,acerto,movimiento_adicional)
            puso_una_opcion_a_pregunta = False
            pygame.time.set_timer(timer_segundos, 0)
            fin_juego = verificar_fin_juego(indice_usuario,TABLERO,copia_preguntas)
            if fin_juego == True or estado_pantalla[VIENDO_MENU] == True:
                configuracion_pantalla_fin_juego[2][IMAGEN] = configuracion_pantalla_escribiendo[1][IMAGEN]
                configuracion_pantalla_fin_juego[4][IMAGEN] = fuente_subtitulos.render(str(indice_usuario),True,COLOR_NEGRO)
                guardar_score(nombre_usuario,indice_usuario)
            else:
                cambiar_pregunta = True
                respuesta_usuario = ""
                cronometro = 0
                imagen_texto_cronometro = fuente_subtitulos.render(str(cronometro),True,COLOR_NEGRO)
                configuracion_cronometro[1][IMAGEN] = imagen_texto_cronometro
                pygame.time.set_timer(timer_segundos, 1000)
            

        imprimir_configuracion(pantalla,configuracion_cronometro)
        imprimir_tablero_pygame(pantalla,TABLERO,imagenes_casilleros,punto_origen_tablero,distancia_entre_casilleros,6,indice_usuario,estilo_texto_valores)
        imprimir_opciones_y_pregunta(pantalla, configuracion_preguntas_opciones)
        if fin_juego:
            imprimir_configuracion(pantalla,configuracion_pantalla_fin_juego)
        if estado_pantalla[VIENDO_MENU] == True:
            estado_pantalla[JUGANDO] = False
        pantalla.blit(imagen_texto_exit,(rect_opcion_fin_juego))

    if estado_pantalla[VIENDO_SCORE]:
        if inicializacion[VIENDO_SCORE]:
            texto_score = leer_score("score.csv")
            ordenar_score_ascendentemente(texto_score)
            imagenes_score = renderizar_score(texto_score, fuente_score,COLOR_NEGRO)
            inicializacion[VIENDO_SCORE] = False
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = evento.pos
                estado_pantalla[VIENDO_MENU] = verificar_colicion_con_click(rects[OPCION_VOLVER_MENU],posicion_click)
                if estado_pantalla[VIENDO_MENU]:
                    estado_pantalla[VIENDO_SCORE] = False
        imprimir_score(pantalla,imagenes_score,(30,100),(400,40),COLOR_NEGRO)
        pantalla.blit(imagen_texto_nombre,(30,30))
        pantalla.blit(imagen_texto_puntuacion,(500,30))
        pantalla.blit(imagen_texto_exit,(rect_opcion_volver_menu))

    reloj.tick(60)
    pygame.display.flip()
pygame.mixer_music.stop()
pygame.quit()