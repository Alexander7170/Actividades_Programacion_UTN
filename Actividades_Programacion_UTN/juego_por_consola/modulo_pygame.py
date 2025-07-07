import pygame
from constantes_pygame import *
def imprimir_menu_escribir(pantalla:pygame.Surface, configuracion:list, color:tuple):
    pygame.draw.line(pantalla,color,(200,250),(600,250),5)
    pygame.draw.rect(pantalla,color,(190,40,460,100),5)
    for i in range(len(configuracion)):
        pantalla.blit(configuracion[i][IMAGEN],configuracion[i][UBICACION])

def imprimir_menu(pantalla:pygame.Surface, configuracion:list):
    for sector in configuracion:
        pantalla.blit(sector["imagen_fondo"],sector["ubicacion_fondo"])
        if "imagen_texto" in sector:
            pantalla.blit(sector["imagen_texto"],sector["ubicacion_fondo"])

def imprimir_pregunta_py_game(pantalla:pygame.Surface, texto:str, fuente:pygame.font.Font, ubicacion_fondo:list, maximo_caracteres_por_linea:int, color:tuple):
    for i in range(0, len(texto), maximo_caracteres_por_linea):
        linea = texto[i : i+ maximo_caracteres_por_linea]
        imagen_linea = fuente.render(linea, True, color)
        pantalla.blit(imagen_linea, ubicacion_fondo)
        ubicacion_fondo[1] +=  30

def imprimir_tablero_pygame(pantalla:pygame.Surface, tablero:list, imagenes:dict, punto_origen:dict, dist_entre_casilleros:dict, cant_columna:int, indice_usuario:int, estilo_texto:dict) :
    sentido_derecho = True
    sentido_izquierdo = False
    eje_x = punto_origen["eje_x"]
    eje_y = punto_origen["eje_y"]
    for i in range(len(tablero)):
        if i % cant_columna == 0:
            if i != 0:
                eje_y -= dist_entre_casilleros["distancia_y"]
                if sentido_derecho:
                    sentido_izquierdo = True
                    sentido_derecho = False
                elif sentido_izquierdo:
                    sentido_derecho = True
                    sentido_izquierdo = False
        elif sentido_derecho:
            eje_x += dist_entre_casilleros["distancia_x"]
        elif sentido_izquierdo:
            eje_x -= dist_entre_casilleros["distancia_x"]
        imagen_numero = estilo_texto["fuente"].render(str(tablero[i]),True,estilo_texto["color"])
        if i == indice_usuario:
            pantalla.blit(imagenes["casillero_azul"],(eje_x,eje_y))
        elif tablero[i] == 0:
            pantalla.blit(imagenes["casillero_amarillo"],(eje_x,eje_y))
            pantalla.blit(imagen_numero,(eje_x,eje_y))
        elif i < indice_usuario:
            pantalla.blit(imagenes["casillero_rojo"],(eje_x,eje_y))
            pantalla.blit(imagen_numero,(eje_x,eje_y))
        elif i > indice_usuario:
            pantalla.blit(imagenes["casillero_verde"],(eje_x,eje_y))
            pantalla.blit(imagen_numero,(eje_x,eje_y))
        
def imprimir_configuracion(pantalla:pygame.Surface,configuracion:dict):
    for i in range(len(configuracion)):
        pantalla.blit(configuracion[i][IMAGEN],configuracion[i][UBICACION])
def imprimir_opciones_y_pregunta(pantalla:pygame.Surface, configuracion:list):
    for sector in configuracion:
        pantalla.blit(configuracion[sector]["imagen_fondo"],configuracion[sector]["ubicacion_fondo"])
        pantalla.blit(configuracion[sector]["imagen_texto"],configuracion[sector]["ubicacion_fondo"])
        
def renderizar_valores_dic(valor_dic:dict, clave_excepcion:str, fuente:pygame.font.Font, color:tuple)->list:
    lista_imagenes = []
    for clave in valor_dic:
        if clave != clave_excepcion:
            imagen_texto = fuente.render(valor_dic[clave],True,color)
            lista_imagenes.append(imagen_texto)
    return lista_imagenes

def modificar_configuracion(configuracion:dict, imagenes:list):
    indice = 0
    for clave in configuracion:
        configuracion[clave]["imagen_texto"] = imagenes[indice]
        indice += 1

def verificar_colicion_con_click(rect:pygame.Rect,coordenada:tuple)->bool:
    coliciono = False
    if rect.collidepoint(coordenada):
        coliciono = True
    return coliciono

def analizar_tecla(evento:pygame.event.Event, texto:str, maximo_caracteres:int, estado_usuario:dict , inicializacion:dict)->str:
    tecla = evento.key
    if tecla == pygame.K_RETURN:
        estado_usuario[ESCRIBIENDO_NOMBRE] = False
        estado_usuario[VIENDO_MENU] = True
        inicializacion[VIENDO_MENU] = True
    elif tecla == pygame.K_BACKSPACE:
        texto = texto[0:-1]
    elif len(texto) <= maximo_caracteres:
        texto += evento.unicode
    return texto

def cambiar_estado_pantalla_click(rects: dict, coordenada:tuple, estado_usuario:dict, inicializacion:dict):
    if rects[OPCION_JUGAR].collidepoint(coordenada):
        estado_usuario[JUGANDO] = True
        inicializacion[JUGANDO] = True
        estado_usuario[VIENDO_MENU] = False
    elif rects[OPCION_SCORE].collidepoint(coordenada):
        estado_usuario[VIENDO_SCORE] = True
        inicializacion[VIENDO_SCORE] = True
        estado_usuario[VIENDO_MENU] = False
    elif rects[OPCION_SALIR].collidepoint(coordenada):
        estado_usuario[CORRER_JUEGO] = False
        estado_usuario[VIENDO_MENU] = False

def cambiar_string_click(zona:dict, posicion_click:tuple , respuesta_usuario:str)->str:
    if zona[OPCION_A].collidepoint(posicion_click):
        respuesta_usuario = "a"
    elif zona[OPCION_B].collidepoint(posicion_click):
        respuesta_usuario = "b"
    elif zona[OPCION_C].collidepoint(posicion_click):
        respuesta_usuario = "c"
    return respuesta_usuario

def leer_score(score:str)->list:
    texto = []
    try:
        with open(score,"r") as archivo:
            for linea in archivo:
                linea = linea.strip() #ELIMINA LOS ESPACION EN BLANCOS Y LOS SALTOS DE LINEA \n
                linea = linea.split(",") # SEPARA EL TEXTO EN DIFERNETES PARTES, CON UN SEPARADOR DE ,
                texto.append(linea)
    except: FileNotFoundError

    return texto

def ordenar_score_ascendentemente(matriz_usuarios:list):
    for i in range(len(matriz_usuarios)-1):
        for j in range(i+1,len(matriz_usuarios)):
            if int(matriz_usuarios[i][1]) > int(matriz_usuarios[j][1]):
                aux = matriz_usuarios[i]
                matriz_usuarios[i] = matriz_usuarios[j]
                matriz_usuarios[j] = aux

def renderizar_score(lista_texto:list, fuente:pygame.font.Font, color:tuple)->list:
    lista_imagenes_puntuaciones = []
    for i in range(len(lista_texto)):
        lista_imagenes_puntuacion = []
        for j in range(len(lista_texto[i])):
            imagen = fuente.render(lista_texto[i][j],True,color)
            lista_imagenes_puntuacion.append(imagen)
        lista_imagenes_puntuaciones.append(lista_imagenes_puntuacion)
    return lista_imagenes_puntuaciones

def imprimir_score(pantalla:str,matriz_imagenes:list ,punto_inicio:tuple, distancia_entre_imagenes:tuple, color:tuple):
    pygame.draw.line(pantalla,COLOR_NEGRO,(0,100),(900,100),4)
    pygame.draw.line(pantalla,COLOR_NEGRO,(400,0),(400,700),4)
    eje_x = punto_inicio[0]
    eje_y = punto_inicio[1]
    for i in range(len(matriz_imagenes)):
        for j in range(len(matriz_imagenes[i])):
            pantalla.blit(matriz_imagenes[i][j],[eje_x,eje_y])
            eje_x += distancia_entre_imagenes[0]
        eje_x = punto_inicio[0]
        eje_y += distancia_entre_imagenes[1]

