import pygame
from datos_pygame import *
from imagenes import *
pygame.init()

#   PANTALLA INICIO

def obtener_configuracion_peticion():
    """
    Funcion que obtiene los textos y el fondo fijo (que no cambian)de la pantalla escribiendo
    Devuelve una configuracion, del sector peticion del nombre
    """
    texto_peticion = fuente_grande.render("dime tu nombre", True,COLOR_NEGRO)
    return {
        "sector_peticion":{IMAGEN_FONDO: imagen_marco_peticion, UBICACION_FONDO:(200,100),
                           IMAGEN_TEXTO:texto_peticion, UBICACION_TEXTO: (250,40)}}

def obtener_configuracion_texto_nombre(nombre:str):
    """
    Funcion que renderiza un nombre y devuelve una configuracion, con su respectiva imagen y su ubicacion
    """
    imagen_nombre_usuario = fuente_grande.render(nombre,True,COLOR_NEGRO)
    return {"sector_nombre_usuario":{IMAGEN_TEXTO: imagen_nombre_usuario, UBICACION_TEXTO: (240,130)}}

#   PANTALLA MENU

def get_imagenes_menu_textos():
    """
    funcion que obtiene las imagenes de texto de la pantalla menu
    Devuelve un diccionario
    """
    imagen_texto_jugar = fuente_grande.render("J u g a r", True , COLOR_NEGRO,)
    imagen_texto_score = fuente_grande.render("S c o r e", True, COLOR_NEGRO)
    imagen_texto_salir = fuente_grande.render("S a l i r", True, COLOR_NEGRO)
    return {"score": imagen_texto_score, "jugar": imagen_texto_jugar, "salir": imagen_texto_salir}

def get_rects_menu():
    """
    funcion que obtiene todos los rect o zonas de la pantalla menu
    devuelve un diccionario
    """
    rect_opcion_jugar = imagen_rectangulo_verde.get_rect()
    rect_opcion_score = imagen_rectangulo_amarillo.get_rect() 
    rect_opcion_salir = imagen_rectangulo_rojo.get_rect()
    rect_opcion_jugar.topleft = (320,320) 
    rect_opcion_score.topleft = (320,420)
    rect_opcion_salir.topleft = (320,520)
    return {"jugar": rect_opcion_jugar, "score": rect_opcion_score, "salir":rect_opcion_salir}

def obtener_configuracion_menu(rect_opcion:dict):
    """
    funcion que obtiene la configuracion de imagenes y sus ubicaciones en la pantalla del menu
    devolviendo un diccionario con su respectiva sector en la pantalla
    """
    imagen_texto = get_imagenes_menu_textos()
    return{
    "sector_portada":{IMAGEN_FONDO:portada, UBICACION_FONDO: (50,0)},
    "sector_jugar":{IMAGEN_FONDO: imagen_rectangulo_verde, UBICACION_FONDO: rect_opcion["jugar"],
                    IMAGEN_TEXTO: imagen_texto["jugar"], UBICACION_TEXTO:(rect_opcion["jugar"].x + 10 , rect_opcion["jugar"].y)},
    "sector_score":{IMAGEN_FONDO: imagen_rectangulo_amarillo , UBICACION_FONDO:rect_opcion["score"],
                    IMAGEN_TEXTO:imagen_texto["score"], UBICACION_TEXTO:(rect_opcion["score"].x +10, rect_opcion["score"].y)},
    "sector_salir":{IMAGEN_FONDO: imagen_rectangulo_rojo, UBICACION_FONDO: rect_opcion["salir"],
                    IMAGEN_TEXTO:imagen_texto["salir"], UBICACION_TEXTO:(rect_opcion["salir"].x + 10, rect_opcion["salir"].y)}}

# PANTALLA JUGAR

def get_imagenes_preguntas_texto(pregunta:dict)->dict:
    """
    Funcion que obtiene las imagenes de texto de los valores del diccionario pregunta
    devolviendo un diccionario
    """
    imagen_texto_pregunta = fuente_pequeña.render(pregunta["pregunta"],True,COLOR_NEGRO)
    imagen_texto_opcion_a = fuente_pequeña.render(pregunta["respuesta_a"],True,COLOR_BLANCO)
    imagen_texto_opcion_b = fuente_pequeña.render(pregunta["respuesta_b"],True,COLOR_BLANCO)
    imagen_texto_opcion_c = fuente_pequeña.render(pregunta["respuesta_c"],True,COLOR_BLANCO)
    return {"pregunta": imagen_texto_pregunta, "opcion_a":imagen_texto_opcion_a, "opcion_b":imagen_texto_opcion_b, "opcion_c":imagen_texto_opcion_c}

def get_rects_jugar():
    """
    funcion que obtiene todos los rect de la pantalla jugar devolviendolo en forma de diccionario
    """
    rect_opcion_a = imagen_rectangulo_negro.get_rect()
    rect_opcion_b = imagen_rectangulo_negro.get_rect()
    rect_opcion_c = imagen_rectangulo_negro.get_rect()
    rect_opcion_a.topleft = (20,600)
    rect_opcion_b.topleft = (320,600)
    rect_opcion_c.topleft = (620,600)
    rect_opcion_volver_menu = imagen_fondo_volver_menu.get_rect()

    return {"a" :rect_opcion_a, "b" :rect_opcion_b, "c" :rect_opcion_c, "volver_menu" :rect_opcion_volver_menu}

def obtener_configuracion_juego_fijo(rect_opcion:dict):
    """
    funcion que obtiene de cada sector de la pantalla jugando, las imagenes del fondo y texto y sus
    respectivas ubicaciones
    devuelve una configuracion con claves de diferentes sectores de la pantalla
    """
    imagen_texto_exit = fuente_pequeña.render("exit",True,COLOR_NEGRO)
    return {
        "sector_pregunta":{IMAGEN_FONDO:imagen_marco_pregunta,UBICACION_FONDO:(10,500),
                           },

        "sector_opcion_a":{IMAGEN_FONDO: imagen_rectangulo_negro,UBICACION_FONDO:(rect_opcion["a"]),
                           },

        "sector_opcion_b":{IMAGEN_FONDO: imagen_rectangulo_negro,UBICACION_FONDO:(rect_opcion["b"]),
                           },

        "sector_opcion_c":{IMAGEN_FONDO: imagen_rectangulo_negro,UBICACION_FONDO:(rect_opcion["c"]),
                           },

        "sector_cronometro":{IMAGEN_FONDO: imagen_casillero_negro, UBICACION_FONDO: (0,400)},

        "sector_volver_menu": {IMAGEN_FONDO: imagen_fondo_volver_menu, UBICACION_FONDO: (0,0),
                               IMAGEN_TEXTO: imagen_texto_exit, UBICACION_TEXTO: rect_opcion["volver_menu"]}}

def obtener_configuracion_preguntas_texto(textos:dict,rect_opcion:dict):
    """
    funcion que obtiene las imagenes de texto de cada sector en la parte de la pregunta y sus opciones
    y ubicandolas en la pantalla jugando
    devuelve un diccionario donde cada sector como su clave, tiene valores que informan la imagen que funde y su ubicacion
    """
    imagenes_texto = get_imagenes_preguntas_texto(textos)
    return{
    "sector_pregunta":{IMAGEN_TEXTO:imagenes_texto["pregunta"], UBICACION_TEXTO:(80,500)},

    "sector_opcion_a":{IMAGEN_TEXTO: imagenes_texto["opcion_a"],UBICACION_TEXTO:(rect_opcion["a"])},

    "sector_opcion_b":{IMAGEN_TEXTO: imagenes_texto["opcion_b"],UBICACION_TEXTO:(rect_opcion["b"])},

    "sector_opcion_c" :{IMAGEN_TEXTO: imagenes_texto["opcion_c"],UBICACION_TEXTO:(rect_opcion["c"])}}

def obtener_configuracion_texto_cronometro(texto:str):
    """
    funcion que obtiene las imagenes del texto del cronometro, que va cambiando siempre
    devuelve un diccionario donde su los valores de cada clave indican la imagen y la ubicacion donde se fundira
    """
    imagen_texto_cronometro = fuente_grande.render(texto,True,COLOR_BLANCO)
    return{
        "sector_cronometro":{IMAGEN_TEXTO: imagen_texto_cronometro, UBICACION_TEXTO: (40,400)}}

def get_imagenes_texto_tablero(tablero:list,indice_usuario:int)->list:
    """
    Funcion que obtiene todas las imagenes de texto de cada valor del tablero, 
    exepto el valor donde su indice en el tablero sea igual a la del usuario

    Devuelve una lista de imagenes de texto renderizadas
    """
    imagenes_texto = []
    for i in range(len(tablero)):
        if i == indice_usuario:
            texto = ""
        else:
            texto = str(tablero[i])
        imagen_texto = fuente_grande.render(texto,True,COLOR_NEGRO)
        imagenes_texto.append(imagen_texto)
    return imagenes_texto

def get_imagenes_fondo_tablero(tablero:list,indice_usuario:int)->list:
    """
    Funcion que obtiene las imagenes del fondo del tablero, cambiando su color 
    dependiendo de la posicion del usuario

    Retorna una lista de imagenes del fondo

    """
    imagenes_fondo = []
    for i in range(len(tablero)):
        if i == indice_usuario:
            imagen_fondo = casillero_azul
        elif tablero[i] == 0:
            imagen_fondo = casillero_amarillo
        elif i < indice_usuario:
            imagen_fondo = casillero_rojo
        elif i > indice_usuario:
            imagen_fondo = casillero_verde
        imagenes_fondo.append(imagen_fondo)

    return imagenes_fondo

def get_ubicacion_tablero_imagenes(tablero:list)->list:
    """
    Funcion que obtiene las ubicacion de las imagenes del tablero
    donde cada imagen tendra su respectiva ubicacion

    Devuelve una lista anidada, donde cada sublista representa la coordenada donde se ubicara la imagen 
    """
    ubicaciones_ordenada = []
    sentido_derecho = True
    sentido_izquierdo = False
    eje_x = 120
    eje_y = 400
    for i in range(len(tablero)):
        if i % 6 == 0:
            if i != 0:
                eje_y -= 78
                if sentido_derecho:
                    sentido_izquierdo = True
                    sentido_derecho = False
                elif sentido_izquierdo:
                    sentido_derecho = True
                    sentido_izquierdo = False
        elif sentido_derecho:
            eje_x += 115
        elif sentido_izquierdo:
            eje_x -= 115
        ubicaciones_ordenada.append((eje_x,eje_y))

    return ubicaciones_ordenada
    
def obtener_configuracion_tablero(tablero:list,indice_usuario:int)->dict:
    """
    funcion que devuelve la configuracino de cada sector del tablero, de cada casillero
    devolviendo una respectiva imagen del fondo con su respectiva imagen de texto en una respectiva ubicacion
    """
    ubicacion_imagenes = get_ubicacion_tablero_imagenes(tablero)
    imagenes_fondo= get_imagenes_fondo_tablero(tablero,indice_usuario)
    imagenes_texto = get_imagenes_texto_tablero(tablero,indice_usuario)
    configuracion_tablero = {}
    for i in range(len(tablero)):
        configuracion_tablero["casillero "+str(i)] = {
        IMAGEN_FONDO:imagenes_fondo[i], UBICACION_FONDO:ubicacion_imagenes[i],
        IMAGEN_TEXTO:imagenes_texto[i], UBICACION_TEXTO:ubicacion_imagenes[i]}
    return configuracion_tablero


# PANTALLA SCORE

def get_imagenes_texto_score():
    """
    Funcion que obtiene las imagenes de textos de la pantalla score

    """
    imagen_texto_exit = fuente_pequeña.render("exit",True, COLOR_NEGRO)
    imagen_texto_nombre = fuente_grande.render("Nombre",True, COLOR_NEGRO)
    imagen_texto_puntuacion = fuente_grande.render("Puntuacion", True, COLOR_NEGRO)
    return {"exit": imagen_texto_exit, "nombre": imagen_texto_nombre, "puntuacion":imagen_texto_puntuacion}

def get_rects_score():
    rect_exit = imagen_fondo_volver_menu.get_rect()
    rect_exit.topleft = (0,0) 
    return {"volver_menu": rect_exit}

def obtener_configuracion_score(rect:dict):
    imagenes_texto = get_imagenes_texto_score()
    return {"sector_salir":{IMAGEN_FONDO: imagen_fondo_volver_menu, UBICACION_FONDO:rect["volver_menu"],
                            IMAGEN_TEXTO: imagenes_texto["exit"], UBICACION_TEXTO: rect["volver_menu"]},
            "sector_nombre":{IMAGEN_FONDO:imagenes_texto["nombre"], UBICACION_FONDO: (30,30)},
            "sector_puntaje":{IMAGEN_FONDO: imagenes_texto["puntuacion"], UBICACION_FONDO: (500, 30)}}


#   PANTALLA FIN JUEGO

def get_imagenes_fin_juego(nombre:str,puntuacion:str)->dict:
    imagen_texto_exit = fuente_pequeña.render("exit",True,COLOR_NEGRO)
    imagen_texto_mensaje = fuente_grande.render("Fin del juego",True,COLOR_NEGRO)
    imagen_texto_nombre = fuente_grande.render("Nombre: " + nombre,True,COLOR_NEGRO)
    imagen_texto_puntuacion = fuente_grande.render("Puntuacion: " + puntuacion,True,COLOR_NEGRO)
    
    return{"nombre": imagen_texto_nombre, "puntuacion": imagen_texto_puntuacion, "mensaje":imagen_texto_mensaje, "exit":imagen_texto_exit}

def obtener_configuracion_fin_juego(nombre:str, puntuacion:str):
    rect = get_rects_score()
    imagenes_texto = get_imagenes_fin_juego(nombre, puntuacion)
    return{"sector_mensaje":{IMAGEN_FONDO: imagen_fondo_fin_juego, UBICACION_FONDO: (150,100),
                             IMAGEN_TEXTO: imagenes_texto["mensaje"], UBICACION_TEXTO:(280,100)},
           "sector_nombre_usuario":{IMAGEN_TEXTO: imagenes_texto["nombre"], UBICACION_TEXTO:(150,200)},
           "sector_puntuacion":{IMAGEN_TEXTO: imagenes_texto["puntuacion"], UBICACION_TEXTO:(150,300)},
           "sector_salir":{IMAGEN_FONDO: imagen_fondo_volver_menu, UBICACION_FONDO: rect["volver_menu"],
                           IMAGEN_TEXTO:imagenes_texto["exit"], UBICACION_TEXTO: rect["volver_menu"]}}
