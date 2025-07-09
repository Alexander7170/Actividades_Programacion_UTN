from modulo_consola import *
from datos_pygame import *
from modulo_pygame import *
from trivia import *
from imagenes_importadas import *
from copy import deepcopy
import pygame

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Trivia")
pygame.mixer.music.load("y2mate.mp3")

fuente_mediana = pygame.font.SysFont("Arial",30)
fuente_pequeña = pygame.font.SysFont("Cooper Black", 20)
fuente_grande = pygame.font.SysFont("Comic Sans MS",40)

estilo_texto_valores = {"fuente":fuente_grande, "color": COLOR_NEGRO }
estilo_texto_opciones = {"fuente": fuente_pequeña, "color":COLOR_NEGRO}

tiempo_segundos = pygame.USEREVENT

velocidad_juego = pygame.time.Clock()

imagen_texto_cronometro = fuente_grande.render(str(cronometro),True,COLOR_NEGRO)
imagen_texto_nombre = fuente_grande.render("Nombre",True, COLOR_NEGRO)
imagen_texto_puntuacion = fuente_grande.render("Puntuacion:",True, COLOR_NEGRO)
imagen_texto_nombre_usuario = fuente_grande.render(nombre_usuario,True,COLOR_NEGRO)
imagen_texto_exit = fuente_mediana.render("Exit",True, COLOR_NEGRO)
imagen_texto_jugar = fuente_grande.render("J u g a r", True , COLOR_NEGRO,)
imagen_texto_score = fuente_grande.render("S c o r e", True, COLOR_NEGRO)
imagen_texto_salir = fuente_grande.render("S a l i r", True, COLOR_NEGRO)
imagen_texto_peticion_nombre = fuente_grande.render(MENSAJE_PEDIR_NOMBRE ,True,COLOR_NEGRO)
imagen_texto_fin_juego = fuente_grande.render(MENSAJE_FIN_PROGRAMA,True,COLOR_NEGRO)

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



punto_origen_tablero = {EJE_X:120, EJE_Y: 400}
distancia_entre_casilleros = {EJE_X:ancho_imagen_casillero_azul, EJE_Y: alto_imagen_casillero_azul}
imagenes_casilleros = {"casillero_azul": casillero_azul, "casillero_verde":casillero_verde, "casillero_rojo": casillero_rojo, "casillero_amarillo":casillero_amarillo}

configuracion_cronometro = {
    "sector_cronometro":{IMAGEN_FONDO: casillero_negro, UBICACION_FONDO: (0,400),
                        IMAGEN_TEXTO: imagen_texto_cronometro, UBICACION_TEXTO: (40,400)}}

configuracion_score = {"texto_salir":{IMAGEN_FONDO: imagen_texto_exit, UBICACION_FONDO: (0,0)},
                       "texto_nombre":{IMAGEN_FONDO:imagen_texto_nombre, UBICACION_FONDO: (30,30)},
                       "texto_puntaje":{IMAGEN_FONDO: imagen_texto_puntuacion, UBICACION_FONDO: (500, 30)}}

configuracion_pantalla_menu = {
    "sector_portada":{IMAGEN_FONDO:portada, UBICACION_FONDO: (50,0)},
    "sector_jugar":{IMAGEN_FONDO:imagen_rectangulo_verde, UBICACION_FONDO: rect_opcion_jugar,
                    IMAGEN_TEXTO:imagen_texto_jugar, UBICACION_TEXTO:(rect_opcion_jugar.x + 10 ,rect_opcion_jugar.y)},
    "sector_score":{IMAGEN_FONDO:imagen_rectangulo_amarillo, UBICACION_FONDO:rect_opcion_score,
                    IMAGEN_TEXTO:imagen_texto_score, UBICACION_TEXTO:(rect_opcion_score.x +10, rect_opcion_score.y)},
    "sector_salir":{IMAGEN_FONDO:imagen_rectangulo_rojo, UBICACION_FONDO: rect_opcion_salir,
                    IMAGEN_TEXTO:imagen_texto_salir, UBICACION_TEXTO:(rect_opcion_salir.x + 10, rect_opcion_salir.y)}}

configuracion_pantalla_fin_juego = {
    "sector_fin_juego":{IMAGEN_FONDO:casillero_blanco,UBICACION_FONDO:(150,100),
                        IMAGEN_TEXTO:imagen_texto_fin_juego,UBICACION_TEXTO:(180,100)},
    "sector_nombre_usuario":{UBICACION_TEXTO:(170,300)},
    "sector_msj_usuario":{IMAGEN_TEXTO:imagen_texto_puntuacion,UBICACION_TEXTO:(180,200)},
    "sector_puntuacion":{UBICACION_TEXTO:(500,200)},
    "sector_salir":{IMAGEN_TEXTO:imagen_texto_exit, UBICACION_TEXTO: (0,0)}}

configuracion_pantalla_escribiendo = {
    "sector_peticion":{IMAGEN_TEXTO: imagen_texto_peticion_nombre, UBICACION_TEXTO: (200,50)},
    "sector_nombre":{IMAGEN_TEXTO: imagen_texto_nombre_usuario, UBICACION_TEXTO: (190,190)}}

configuracion_preguntas_opciones = {
    "pregunta":{IMAGEN_FONDO:imagen_marco_pregunta,UBICACION_FONDO: (10,500),
                UBICACION_TEXTO:(80,500)},
    "opcion_a":{IMAGEN_FONDO:imagen_rectangulo_amarillo, UBICACION_FONDO : rect_opcion_a,
                UBICACION_TEXTO:(rect_opcion_a.x + 20, rect_opcion_a.y+20)},
    "opcion_b":{IMAGEN_FONDO:imagen_rectangulo_amarillo, UBICACION_FONDO:rect_opcion_b, 
                UBICACION_TEXTO:(rect_opcion_b.x + 20, rect_opcion_b.y+20)},
    "opcion_c":{IMAGEN_FONDO:imagen_rectangulo_amarillo, UBICACION_FONDO:rect_opcion_c, 
                UBICACION_TEXTO:(rect_opcion_c.x + 20, rect_opcion_c.y+20)}}


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
                configuracion_pantalla_escribiendo["sector_nombre"][IMAGEN_TEXTO] = fuente_grande.render(nombre_usuario,True,COLOR_NEGRO)     
        pygame.draw.line(pantalla,COLOR_NEGRO,(200,250),(600,250),5)
        pygame.draw.rect(pantalla,COLOR_NEGRO,(190,40,460,100),5)
        imprimir_configuracion(pantalla, configuracion_pantalla_escribiendo)

    if estado_pantalla[VIENDO_MENU]:
        if inicializacion[VIENDO_MENU]:
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
            inicializacion[VIENDO_MENU] = False

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = evento.pos
                cambiar_estado_pantalla_click(rects, posicion_click, estado_pantalla, inicializacion)
        imprimir_configuracion(pantalla, configuracion_pantalla_menu)

    if estado_pantalla[JUGANDO]:

        if inicializacion[JUGANDO]:
            cambiar_pregunta = True
            puso_una_opcion_a_pregunta = False
            indice_usuario = PUNTO_DE_PARTIDA
            respuesta_usuario = ""
            cronometro = 0
            fin_juego = False
            configuracion_cronometro["sector_cronometro"][IMAGEN_TEXTO] = fuente_grande.render(str(cronometro),True,COLOR_NEGRO)
            copia_preguntas = deepcopy(preguntas)
            pygame.time.set_timer(tiempo_segundos,1000)
            inicializacion[JUGANDO] = False

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = evento.pos
                respuesta_usuario = cambiar_string_click(rects, posicion_click, respuesta_usuario)
                estado_pantalla[VIENDO_MENU] = verificar_colicion_con_click(rects[OPCION_VOLVER_MENU],posicion_click)
                if estado_pantalla[VIENDO_MENU]:
                    pygame.time.set_timer(tiempo_segundos, 0)
                    estado_pantalla[JUGANDO] = False
                    guardar_score(nombre_usuario,indice_usuario)

                if respuesta_usuario != "" and fin_juego == False and estado_pantalla[VIENDO_MENU] == False:
                    puso_una_opcion_a_pregunta = True

            if evento.type == tiempo_segundos:
                cronometro += 1
                configuracion_cronometro["sector_cronometro"][IMAGEN_TEXTO] = fuente_grande.render(str(cronometro),True,COLOR_NEGRO)
        
        if cambiar_pregunta:
            pregunta = manejar_pregunta(copia_preguntas)
            imagenes_pregunta_opciones = renderizar_valores_dic(pregunta,CLAVE_RESPUESTA_CORRECTA,fuente_pequeña,COLOR_NEGRO)
            modificar_configuracion(configuracion_preguntas_opciones,imagenes_pregunta_opciones)
            cambiar_pregunta = False

        if puso_una_opcion_a_pregunta or cronometro == TIEMPO_MAXIMO:
            acerto = verificar_respuesta(pregunta,respuesta_usuario,CLAVE_RESPUESTA_CORRECTA)
            indice_usuario = mover_usuario(indice_usuario , TABLERO, acerto, MOVERSE_RESPUESTA_CORRECTA, MOVERSE_RESPUESTA_INCORRECTA)
            puso_una_opcion_a_pregunta = False
            pygame.time.set_timer(tiempo_segundos, 0)
            fin_juego = verificar_fin_juego(indice_usuario,TABLERO,copia_preguntas)
            if fin_juego == True:
                configuracion_pantalla_fin_juego["sector_nombre_usuario"][IMAGEN_TEXTO] = configuracion_pantalla_escribiendo["sector_nombre"][IMAGEN_TEXTO]
                configuracion_pantalla_fin_juego["sector_puntuacion"][IMAGEN_TEXTO] = fuente_grande.render(str(indice_usuario),True,COLOR_NEGRO)
            else:
                cambiar_pregunta = True
                respuesta_usuario = ""
                cronometro = 0
                configuracion_cronometro["sector_cronometro"][IMAGEN_TEXTO] = fuente_grande.render(str(cronometro),True,COLOR_NEGRO)
                pygame.time.set_timer(tiempo_segundos, 1000)
            
        if not fin_juego:
            imprimir_configuracion(pantalla, configuracion_cronometro)
            imprimir_tablero_pygame(pantalla,TABLERO,imagenes_casilleros,punto_origen_tablero,distancia_entre_casilleros,6,indice_usuario,estilo_texto_valores)
            imprimir_configuracion(pantalla, configuracion_preguntas_opciones)
        else:
            imprimir_configuracion(pantalla, configuracion_pantalla_fin_juego)   
        
    if estado_pantalla[VIENDO_SCORE]:

        if inicializacion[VIENDO_SCORE]:
            texto_score = leer_score("score.csv")
            ordenar_score_ascendentemente(texto_score)
            imagenes_score = renderizar_score(texto_score, fuente_grande,COLOR_NEGRO)
            inicializacion[VIENDO_SCORE] = False

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = evento.pos
                estado_pantalla[VIENDO_MENU] = verificar_colicion_con_click(rects[OPCION_VOLVER_MENU],posicion_click)
                if estado_pantalla[VIENDO_MENU]:
                    estado_pantalla[VIENDO_SCORE] = False
        imprimir_score(pantalla,imagenes_score,(30,100),(400,40),COLOR_NEGRO)
        imprimir_configuracion(pantalla,configuracion_score)
    velocidad_juego.tick(FPS)
    pygame.display.flip()
pygame.mixer.music.stop()
pygame.quit()