from Modulo_juego import *
from datos_consola import *
from datos_pygame import *
from copy import deepcopy
from modulo_pygame import *
from imagenes_renderizaciones import *
import pygame
pygame.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Trivia")
fuente_subtitulos = pygame.font.SysFont("Comic Sans MS",45)
fuente_pregunta = pygame.font.SysFont("Arial",30)
fuente_opciones = pygame.font.SysFont("Cooper Black", 20)
estilo_texto_valores = {"fuente":fuente_subtitulos, "color": COLOR_NEGRO }
estilo_texto_opciones = {"fuente": fuente_opciones, "color":COLOR_NEGRO}
fuente_score = pygame.font.SysFont("Comic Sans MS",40)

pygame.mixer.music.load("y2mate.mp3")

timer_segundos = pygame.USEREVENT
reloj = pygame.time.Clock()

imagen_texto_cronometro = fuente_subtitulos.render(str(cronometro),True,COLOR_NEGRO)
imagen_texto_nombre = fuente_subtitulos.render("Nombre",True, COLOR_NEGRO)
imagen_texto_puntuacion = fuente_subtitulos.render("Puntuacion",True, COLOR_NEGRO)
imagen_texto_nombre_usuario = fuente_subtitulos.render(nombre_usuario,True,COLOR_NEGRO)
imagen_texto_exit = fuente_pregunta.render("Exit",True, COLOR_NEGRO)
imagen_texto_jugar = fuente_subtitulos.render("J u g a r", True , COLOR_NEGRO,)
imagen_texto_score = fuente_subtitulos.render("S c o r e", True, COLOR_NEGRO)
imagen_texto_salir = fuente_subtitulos.render("S a l i r", True, COLOR_NEGRO)
imagen_texto_peticion_nombre = fuente_subtitulos.render(MENSAJE_PEDIR_NOMBRE ,True,COLOR_NEGRO)
imagen_texto_fin_juego = fuente_subtitulos.render(MENSAJE_FIN_PROGRAMA,True,COLOR_NEGRO)

rect_opcion_fin_juego = imagen_casillero_negro.get_rect()
rect_opcion_jugar = imagen_rectangulo_verde.get_rect()
rect_opcion_score = imagen_rectangulo_amarillo.get_rect() 
rect_opcion_salir = imagen_rectangulo_rojo.get_rect() 
rect_opcion_a = imagen_rectangulo_verde.get_rect()
rect_opcion_b = imagen_rectangulo_verde.get_rect()
rect_opcion_c = imagen_rectangulo_verde.get_rect()
rect_opcion_volver_menu = imagen_texto_exit.get_rect()
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

configuracion_cronometro = {"fondo":{IMAGEN: casillero_negro, UBICACION: (0,400)},
                            "texto":{IMAGEN: imagen_texto_cronometro, UBICACION: (40,400)}}

configuracion_score = {"texto_salir":{IMAGEN: imagen_texto_exit, UBICACION: (0,0)},
                       "texto_nombre":{IMAGEN:imagen_texto_nombre, UBICACION: (30,30)},
                       "texto_puntaje":{IMAGEN: imagen_texto_puntuacion, UBICACION: (500, 30)}}

configuracion_menu = {"portada_juego":{IMAGEN:portada, UBICACION: (50,0)},
                      "fondo_jugar":{IMAGEN:imagen_rectangulo_verde, UBICACION: rect_opcion_jugar},
                      "texto_jugar":{IMAGEN:imagen_texto_jugar, UBICACION:(rect_opcion_jugar.x + 10 ,rect_opcion_jugar.y)},
                      "fondo_score":{IMAGEN:imagen_rectangulo_amarillo, UBICACION:rect_opcion_score},
                      "texto_score":{IMAGEN:imagen_texto_score, UBICACION:(rect_opcion_score.x +10, rect_opcion_score.y)},
                      "fondo_salir":{IMAGEN:imagen_rectangulo_rojo, UBICACION: rect_opcion_salir},
                      "texto_salir":{IMAGEN:imagen_texto_salir, UBICACION:(rect_opcion_salir.x + 10, rect_opcion_salir.y)}}

configuracion_pantalla_fin_juego = {"fondo":{IMAGEN:casillero_blanco,UBICACION:(150,100)},
                                    "mensaje_fin":{IMAGEN:imagen_texto_fin_juego,UBICACION:(180,100)},
                                    "nombre_usuario":{UBICACION:(180,200)},
                                    "mensaje":{IMAGEN:imagen_texto_puntuacion,UBICACION:(170,300)},
                                    "puntuacion":{UBICACION:(400,400)}}

configuracion_pantalla_escribiendo = {"mensaje_peticion":{IMAGEN: imagen_texto_peticion_nombre, UBICACION: (200,50)},
                                      "nombre_usuario":{IMAGEN: imagen_texto_nombre_usuario, UBICACION: (190,190)}}

configuracion_preguntas_opciones = {
    "pregunta":{"imagen_fondo":imagen_marco_pregunta, "ubicacion_fondo": (10,500), "ubicacion_texto":(80,500)},
    "opcion_a":{"imagen_fondo":imagen_rectangulo_amarillo, "ubicacion_fondo": rect_opcion_a, "ubicacion_texto":(rect_opcion_a.x + 20, rect_opcion_a.y+20)},
    "opcion_b":{"imagen_fondo":imagen_rectangulo_amarillo, "ubicacion_fondo":rect_opcion_b, "ubicacion_texto":(rect_opcion_b.x + 20, rect_opcion_b.y+20)},
    "opcion_c":{"imagen_fondo":imagen_rectangulo_amarillo, "ubicacion_fondo":rect_opcion_c, "ubicacion_texto":(rect_opcion_c.x + 20, rect_opcion_c.y+20)}}

rects = {OPCION_JUGAR: rect_opcion_jugar, OPCION_SCORE: rect_opcion_score, OPCION_SALIR:rect_opcion_salir, 
        OPCION_A: rect_opcion_a, OPCION_B: rect_opcion_b, OPCION_C:rect_opcion_c, OPCION_VOLVER_MENU:rect_opcion_volver_menu}
estado_pantalla = {CORRER_JUEGO:True, VIENDO_MENU: False, VIENDO_SCORE: False, JUGANDO: False, ESCRIBIENDO_NOMBRE: True }
inicializacion = {VIENDO_MENU: False, VIENDO_SCORE:False, JUGANDO:False}

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
                configuracion_pantalla_escribiendo["nombre_usuario"][IMAGEN] = fuente_subtitulos.render(nombre_usuario,True,COLOR_NEGRO)     
        imprimir_menu_escribir(pantalla, configuracion_pantalla_escribiendo ,COLOR_NEGRO,)

    if estado_pantalla[VIENDO_MENU]:
        if inicializacion[VIENDO_MENU]:
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
            inicializacion[VIENDO_MENU] = False
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = evento.pos
                cambiar_estado_pantalla_click(rects, posicion_click, estado_pantalla, inicializacion)
        imprimir_configuracion(pantalla, configuracion_menu)

    if estado_pantalla[JUGANDO]:

        if inicializacion[JUGANDO]:
            cambiar_pregunta = True
            puso_una_opcion_a_pregunta = False
            indice_usuario = PUNTO_DE_PARTIDA
            respuesta_usuario = ""
            cronometro = 0
            fin_juego = False
            configuracion_cronometro["texto"][IMAGEN] = fuente_subtitulos.render(str(cronometro),True,COLOR_NEGRO)
            copia_preguntas = deepcopy(preguntas)
            pygame.time.set_timer(timer_segundos,1000)
            inicializacion[JUGANDO] = False

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = evento.pos
                respuesta_usuario = cambiar_string_click(rects, posicion_click, respuesta_usuario)
                estado_pantalla[VIENDO_MENU] = verificar_colicion_con_click(rects[OPCION_VOLVER_MENU],posicion_click)
                if estado_pantalla[VIENDO_MENU]:
                    pygame.time.set_timer(timer_segundos, 0)
                    estado_pantalla[JUGANDO] = False
                    guardar_score(nombre_usuario,indice_usuario)

                if respuesta_usuario != "" and fin_juego == False and estado_pantalla[VIENDO_MENU] == False:
                    puso_una_opcion_a_pregunta = True

            if evento.type == timer_segundos:
                cronometro += 1
                configuracion_cronometro["texto"][IMAGEN] = fuente_subtitulos.render(str(cronometro),True,COLOR_NEGRO)
        
        if cambiar_pregunta:
            pregunta = buscar_pregunta(copia_preguntas)
            eliminar_una_pregunta(copia_preguntas,pregunta)
            imagenes_pregunta_opciones = renderizar_valores_dic(pregunta,CLAVE_RESPUESTA_CORRECTA,fuente_opciones,COLOR_NEGRO)
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
            if fin_juego == True:
                configuracion_pantalla_fin_juego["nombre_usuario"][IMAGEN] = configuracion_pantalla_escribiendo["nombre_usuario"][IMAGEN]
                configuracion_pantalla_fin_juego["puntuacion"][IMAGEN] = fuente_subtitulos.render(str(indice_usuario),True,COLOR_NEGRO)
            else:
                cambiar_pregunta = True
                respuesta_usuario = ""
                cronometro = 0
                configuracion_cronometro["texto"][IMAGEN] = fuente_subtitulos.render(str(cronometro),True,COLOR_NEGRO)
                pygame.time.set_timer(timer_segundos, 1000)
            
        pantalla.blit(imagen_texto_exit,(rect_opcion_fin_juego))
        imprimir_configuracion(pantalla, configuracion_cronometro)
        imprimir_tablero_pygame(pantalla,TABLERO,imagenes_casilleros,punto_origen_tablero,distancia_entre_casilleros,6,indice_usuario,estilo_texto_valores)
        imprimir_opciones_y_pregunta(pantalla, configuracion_preguntas_opciones)
        if fin_juego:
            imprimir_configuracion(pantalla, configuracion_pantalla_fin_juego)   
        
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
        imprimir_configuracion(pantalla,configuracion_score)
    reloj.tick(60)
    pygame.display.flip()
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()