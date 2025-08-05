import pygame
from logica import *
from trivia import *
from funciones_blit import *
from copy import deepcopy
from renderizaciones import *
pygame.init()

def analizar_correr_juego(estado_juego:dict , eventos:list):
    """
    analiza si el usuario quiere cerrar la ventana
    """
    for evento in eventos:
        if evento.type == pygame.QUIT:
            estado_juego["correr_juego"] = False

#   PANTALLA INICIO

def obtener_datos_escribiendo()->dict:
    """
    carga los datos que se muestran y se usaran al principio del juego
    Devuelve un diccionario con esos datos
    """
    imagen_fondo_escribiendo = pygame.image.load("Imagenes/marco rectangulo.png")
    imagen_fondo_escribiendo = pygame.transform.scale(imagen_fondo_escribiendo,(400,60))
    nombre_usuario = ""
    imagen_texto_peticion = renderizar_valor("Dime tu nombre")     
    imagen_texto_nombre_us = renderizar_valor(nombre_usuario)
    return{"nombre_usuario": nombre_usuario,
    "fondo_nombre_us":imagen_fondo_escribiendo,
    "texto_peticion": imagen_texto_peticion,
    "max_caracteres": 15,
    "imagen_texto_nombre_us":imagen_texto_nombre_us} 

def analizar_tecla(evento:pygame.event.Event, datos, estado_juego:str):
    """
    Funcion que analiza la tecla presionada, actualizando los datos y el estado_juego
    
    """
    tecla = evento.key
    if tecla == pygame.K_RETURN:
        estado_juego["pantalla_actual"] = "viendo_menu"
    elif tecla == pygame.K_BACKSPACE:
        datos["nombre_usuario"] = datos["nombre_usuario"][0:-1]
        estado_juego["actualizar_datos"] = True
    elif len(datos["nombre_usuario"]) <= datos["max_caracteres"]:
        estado_juego["actualizar_datos"] = True
        datos["nombre_usuario"] += evento.unicode
    datos["imagen_texto_nombre_us"] = renderizar_valor(datos["nombre_usuario"])

def pantalla_escribiendo(pantalla:pygame.Surface, estado_juego, datos:dict, eventos:list):
    """
    Funcion donde analiza los eventos en la pantalla escribiendo y muetra esa pantalla
    """
    for evento in eventos:
        if evento.type == pygame.KEYDOWN:
            analizar_tecla(evento, datos, estado_juego)
    ver_pantalla_escribiendo(pantalla,datos)

#   PANTALLA MENU

def pantalla_menu(pantalla:pygame.Surface, estado_juego:dict, imagenes_fijas:dict, rects:dict, eventos:list):
    """
    Funcion donde analiza los eventos en la pantalla menu y muetra esa pantalla
    """
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            analizar_coliciones_menu(estado_juego,rects,evento)
    ver_pantalla_menu(pantalla, imagenes_fijas, rects)

def obtener_rects_menu(imagenes:dict)->dict:
    """
    funcion que obtiene todos los rect o zonas de la pantalla menu
    devuelve un diccionario
    """
    rect_opcion_jugar = imagenes["imagen_jugar"].get_rect()
    rect_opcion_score = imagenes["imagen_score"].get_rect() 
    rect_opcion_salir = imagenes["imagen_salir"].get_rect()
    rect_opcion_jugar.topleft = (320,320)
    rect_opcion_score.topleft = (320,420)
    rect_opcion_salir.topleft = (320,520)
    return {"rect_jugar": rect_opcion_jugar, "rect_score": rect_opcion_score, "rect_salir":rect_opcion_salir}

def analizar_coliciones_menu(estado_juego:dict, rects:dict, evento:list):
    """
    analiza la coordenada del click con los rects, actualizando si hubo colicion, el estado de la pantalla
    """
    posicion_click = evento.pos
    if rects["rect_jugar"].collidepoint(posicion_click):
        estado_juego["pantalla_actual"] = "jugando"
        estado_juego["actualizar_datos"] = True
    elif rects["rect_score"].collidepoint(posicion_click):
        estado_juego["pantalla_actual"] = "viendo_score"
    elif rects["rect_salir"].collidepoint(posicion_click):
        estado_juego["correr_juego"] = False

# PANTALLA JUGAR
 
def obtener_datos_jugando(datos_escribiendo:dict, imagenes_fijas:dict)->dict:
    """
    Funcion que obtiene los datos que se usaran en el analisis de la pantalla.
    obtiene tambien las imagenes que son dinamicas, que cambian cada cierto evento.
    Devuelve un diccionario
    """
    tiempo_segundos = pygame.USEREVENT
    copia_preguntas = deepcopy(preguntas)
    nombre_usuario = datos_escribiendo["nombre_usuario"]
    pregunta_opciones = manejar_pregunta(copia_preguntas)
    tablero = [0,0,1,0,2,0,1,1,0,0,0,2,0,1,0,2,1,1,1,0,2,0,3,0,1,0,0,2,0,0,0]
    indice_usuario = 15
    cronometro = 0
    imagenes_texto_preguntas_opciones = obtener_imagenes_pregunta_opciones(pregunta_opciones)
    imagen_texto_cronometro = renderizar_valor(str(cronometro))
    
    configuracion_tablero = obtener_configuracion_tablero(imagenes_fijas,tablero,indice_usuario)
    return {"tablero" : tablero,
            "nombre_usuario":nombre_usuario,
            "indice_usuario":indice_usuario,
            "cronometro": 0,
            "tiempo_maximo": 15,
            "respuesta_usuario" : "",
            "clave_respuesta": "respuesta_correcta",
            "lista_preguntas":copia_preguntas,
            "pregunta_opciones":pregunta_opciones,
            "iniciar_cronometro": True,
            "eligio_opcion": False,
            "fin_juego": False,
            "evento_tiempo": tiempo_segundos,
            "imagen_pregunta_opciones":imagenes_texto_preguntas_opciones,
            "imagen_texto_cronometro": imagen_texto_cronometro,
            "configuracion_tablero": configuracion_tablero,}

def pantalla_jugando(pantalla:pygame.Surface,estado_juego:dict,datos:dict,imagenes_fijas:dict ,rects:dict,eventos:list):
    """
    Funcion analiza los eventos, actualiza los datos, y muestra en pantalla las imagenes
    """
    for evento in eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN:
            analizar_collidepoint_jugar(evento,rects,datos ,estado_juego)
        if evento.type == pygame.USEREVENT:
            datos["cronometro"] += 1
            if datos["cronometro"] != datos["tiempo_maximo"]:
                datos["imagen_texto_cronometro"] = renderizar_valor(datos["cronometro"])

    pantalla.blit(imagenes_fijas["volver_menu"],rects["opcion_volver_menu"])
    if datos["fin_juego"] == False:
        
        if datos["iniciar_cronometro"]:
            datos["cronometro"] = 0
            pygame.time.set_timer(datos["evento_tiempo"],1000)
            datos["imagen_texto_cronometro"] = renderizar_valor(datos["cronometro"])
            datos["iniciar_cronometro"] = False

        if datos["eligio_opcion"] or datos["cronometro"] == datos["tiempo_maximo"]:

            acerto = verificar_respuesta(datos["pregunta_opciones"], datos["respuesta_usuario"], datos["clave_respuesta"])
            datos["indice_usuario"] = jugar_turno(datos["indice_usuario"], datos["tablero"] , acerto)
            datos["fin_juego"] = verificar_fin_juego(datos["indice_usuario"], datos["tablero"] ,datos["lista_preguntas"])
            datos["respuesta_usuario"] = ""
            datos["iniciar_cronometro"] = True
            datos["elegir_pregunta"] = True
            datos["eligio_opcion"] = False
            datos["configuracion_tablero"] =  obtener_configuracion_tablero(imagenes_fijas, datos["tablero"], datos["indice_usuario"])
            if not datos["fin_juego"]:
                datos["pregunta_opciones"] = manejar_pregunta(datos["lista_preguntas"])
                datos["imagen_pregunta_opciones"] = obtener_imagenes_pregunta_opciones(datos["pregunta_opciones"])
            else:
                pygame.time.set_timer(datos["evento_tiempo"],0)
                datos["imagenes_fin_juego"] = obtener_imagenes_fin_juego(datos)
        ver_pantalla_jugando(pantalla, datos, imagenes_fijas, rects) 
    else:
        ver_pantalla_fin_juego(pantalla,datos,imagenes_fijas)

def analizar_collidepoint_jugar(evento:pygame.event.Event, rects:dict, datos:dict, estado_juego:dict):
    """
    analiza si hubo colicion con algun rect con la posicion del click, actualizando asi los datos y el estado del juego
    """
    posicion_click = evento.pos
    if rects["opcion_a"].collidepoint(posicion_click):
        datos["respuesta_usuario"] = "a"
    elif rects["opcion_b"].collidepoint(posicion_click):
        datos["respuesta_usuario"] = "b"
    elif rects["opcion_c"].collidepoint(posicion_click):
        datos["respuesta_usuario"] = "c"
    elif rects["opcion_volver_menu"].collidepoint(posicion_click):
        estado_juego["pantalla_actual"] = "viendo_menu"
        estado_juego["actualizar_datos"] = True
        guardar_score(datos["nombre_usuario"], datos["indice_usuario"])
    if datos["respuesta_usuario"] != "":
        datos["eligio_opcion"] = True

def obtener_rects_jugando(imagenes:dict)->dict:
    """
    funcion que obtiene todos los rect de la pantalla jugar devolviendolo en forma de diccionario
    """
    rect_opcion_a = imagenes["fondo_opcion"].get_rect()
    rect_opcion_b = imagenes["fondo_opcion"].get_rect()
    rect_opcion_c = imagenes["fondo_opcion"].get_rect()
    rect_opcion_volver_menu = imagenes["volver_menu"].get_rect()
    rect_opcion_volver_menu.topleft = (10,10)
    rect_opcion_a.topleft = (0,620)
    rect_opcion_b.topleft = (300,620)
    rect_opcion_c.topleft = (600,620)
    
    return {"opcion_a" :rect_opcion_a, "opcion_b" :rect_opcion_b, "opcion_c" :rect_opcion_c, "opcion_volver_menu" :rect_opcion_volver_menu}

def obtener_configuracion_tablero(imagenes:dict, tablero:list, indice_usuario:int)->dict:
    """
    funcion que obtiene de cada elemento de la lista del tablero, su respectiva imagen del fondo
    con su respectiva imagen de texto, ambos en una respectiva ubicacion. 
    Devuelve un diccionario donde las claves son cada casillero, y sus valores son un diccionario
    donde se guarda las imagenes de ese casillero y su ubicacion en la pantalla
    """
    ubicacion_imagenes = obtener_ubicacion_tablero_imagenes(tablero)
    imagenes_fondo = obtener_imagenes_fondo_tablero(imagenes,tablero,indice_usuario,)
    imagenes_texto = obtener_imagenes_texto_tablero(tablero,indice_usuario)
    configuracion_tablero = {}
    for i in range(len(tablero)):
        configuracion_tablero["casillero "+str(i)] = {
        "imagen_fondo":imagenes_fondo[i], "ubicacion_fondo":ubicacion_imagenes[i],
        "imagen_texto":imagenes_texto[i], "ubicacion_texto":ubicacion_imagenes[i]}
    return configuracion_tablero

# PANTALLA SCORE

def pantalla_score(pantalla:pygame.Surface, estado_juego:dict, datos:dict, imagenes_fijas:dict,rect:dict, eventos:list):
    """
    analiza los eventos que ocurrieron en la pantalla score y muestra la misma
    """
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            analizar_collidepoint_score(estado_juego,rect,evento)
    ver_pantalla_score(pantalla,datos,imagenes_fijas,rect)

def obtener_datos_score(ruta:str)->dict:
    """
    obtiene los datos que se usan en la pantalla score
    devolviendolos en forma de diccionario
    """
    matriz_imagenes = manejar_score(ruta)
    ubicaciones_matriz_imagenes = obtener_posiciones_matriz_score(matriz_imagenes)
    return {"matriz_imagenes":matriz_imagenes,
            "matriz_ubicaciones":ubicaciones_matriz_imagenes}

def manejar_score(ruta:str)->list:
    """
    Funcion que obtiene las imagenes de texto de un archivo, pasado como parametro su ruta
    """
    texto_score = leer_score(ruta)
    ordenar_score_ascendentemente(texto_score)
    imagenes_texto = renderizar_score(texto_score)
    return imagenes_texto

def analizar_collidepoint_score( estado_juego:dict, rect_opcion:pygame.Surface, evento:list):
    """
    Funcion que analiza si la posicion del click coliciono con el rect, actualizando el estado del juego
    """
    posicion_click = evento.pos
    if rect_opcion.collidepoint(posicion_click):
        estado_juego["pantalla_actual"] = "viendo_menu"

def obtener_rects_score(imagenes:dict)->pygame.Surface:
    """
    Funcion que obtiene la dimencion del rect y lo ubica en la pantalla
    """
    rect_opcion_volver_menu = imagenes["volver_menu"].get_rect()
    rect_opcion_volver_menu.topleft = (10,10) 
    return rect_opcion_volver_menu

