import pygame
from datos_pygame import *

def imprimir_configuracion(pantalla:pygame.Surface, configuracion:dict):
    """
    Funcion que imprime en una superficie, las imagenes de configuracion con sus respectivas ubicaciones ya definidas
    
    parametros:

        pantalla: la superficie donde fundiremos las imagenes con sus ubicaciones y la linea y el rect

        configuracion: una lista donde sus elementos son diccionarios, los cuales cada diccionario
                    tiene sus respectivas imagenes, con sus respectivas coordenadas de fundicion en pantalla
    """
    for opcion in configuracion:
        if IMAGEN_FONDO in configuracion[opcion]:
            pantalla.blit(configuracion[opcion][IMAGEN_FONDO],configuracion[opcion][UBICACION_FONDO])
        if IMAGEN_TEXTO in configuracion[opcion]:
            pantalla.blit(configuracion[opcion][IMAGEN_TEXTO], configuracion[opcion][UBICACION_TEXTO])
def imprimir_tablero_pygame(pantalla:pygame.Surface, tablero:list, imagenes:dict, punto_origen:dict, dist_entre_casilleros:dict, cant_columna:int, indice_usuario:int, estilo_texto:dict):
    """
    Funcion que imprime un dato tipo lista de numeros, en una tablero con un limite de columana por fila y cambiado de sentido por cada fila
    dependiendo los numeros de la lista y la ubicacion del usuario, funde diferentes imagenes.
    
    Parametros:

        pantalla: una superficie donde se fundira las imagenes
        tablero: una lista de numeros, que indica las imagenes de texto de cada casillero, representando casilleros amarillos los valores 0
        imagenes: un diccionario donde estan todas las imagenes cargadas de los diferentes casilleros
        punto_origen: un diccionario donde estan las coordenadas del inicio de fundicion del tablero
        dist_entre_casilleros: un diccionario que indica la distancia maxima entre casilleros en el eje_x, eje_y
        cant_columna: un entero que indica la cantidad de columnas maxima que puede tener las filas
        indice_usuario: un entero que indica un indice, que los indices del tablero menores a este, se fundiran casilleros rojos, y los mayores casilleros verdes
        estilo_texto: un diccionario en donde se obtiene la fuente del texto de valores de los casilleros y el color
    """
    sentido_derecho = True
    sentido_izquierdo = False
    eje_x = punto_origen[EJE_X]
    eje_y = punto_origen[EJE_Y]
    for i in range(len(tablero)):
        if i % cant_columna == 0:
            if i != 0:
                eje_y -= dist_entre_casilleros[EJE_Y]
                if sentido_derecho:
                    sentido_izquierdo = True
                    sentido_derecho = False
                elif sentido_izquierdo:
                    sentido_derecho = True
                    sentido_izquierdo = False
        elif sentido_derecho:
            eje_x += dist_entre_casilleros[EJE_X]
        elif sentido_izquierdo:
            eje_x -= dist_entre_casilleros[EJE_X]

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
        
def renderizar_valores_dic(valor_dic:dict, clave_excepcion:str, fuente:pygame.font.Font, color:tuple)->list:
    """
    Una funcion que renderiza todos los valores del dic a exepcion de uno,

    Parametros: 

        valor_dic: el diccionario donde todos sus valores son strings
        clave_excepcion: un string que determina la clave a la cual no renderizara su valor
        funete: una fuente en la que determina el tipo de texto y el tamaño de letra de la imagen
        color: una tupla que determina el color de la letras de la imagen
    
    Retorno:
        devuelve una lista de imagenes, de las que fueron renderizadas
    """
    lista_imagenes = []
    for clave in valor_dic:
        if clave != clave_excepcion:
            imagen_texto = fuente.render(valor_dic[clave],True,color)
            lista_imagenes.append(imagen_texto)
    return lista_imagenes

def modificar_configuracion(configuracion:dict, imagenes:list):
    """
    funcion que agrega la clave "imagen_texto" por cada valor de la lista de imagenes al diccionario

    Parametros:
        configuracion: un diccionario donde agregaremos claves con valores
        imagenes: la lista de imagenes, que son los valores que se guardaran en la configuracion
    """
    indice = 0
    for sector in configuracion:
        configuracion[sector][IMAGEN_TEXTO] = imagenes[indice]
        indice += 1

def verificar_colicion_con_click(rect:pygame.Rect,coordenada:tuple)->bool:
    """
    funcion que verifica si una region colisiono en una coordenada

    Parametros:
        rect: la region, donde se verifica si se colisiono
        coordenada: una tupla que tiene eje x,y
    Retorno:
        Devuelve un booleano verdadero si se colisiono
    """
    colisiono = False
    if rect.collidepoint(coordenada):
        colisiono = True
    return colisiono

def analizar_tecla(evento:pygame.event.Event, texto:str, maximo_caracteres:int, estado_usuario:dict , inicializacion:dict)->str:
    """
    Funcion que analiza el vento tipo tecla con algunos criterios definidos

    Parametros:
        evento: un evento de tipo tecla
        texto: un string que se modificara dependiendo del evento
        maximo_caracteres: un entero que determina el maximo caracteres que puede tener el texto
        estado_usuario: un diccionario donde se modificara o no sus valores dentro dependiendo del criterio de la tecla
        inicializacion: un diccionario donde se modificar o no sus valores dentro dependiendo del criterio de la tecla
    
    Retorno:
        Devuelve el string texto alterado dependiendo del evento tecla
    """
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
    """
    Funcion que modifica los valores de los dicts dependiendo con que region coliciono,o no, la coordenada

    Parametros:
        rects: un diccionario donde todos sus valores son regiones o rect
        coordenada: una tupla que indica un punto en eje
        estado_usuario: un dict donde sus valores se veran afectados dependindo de la colision
        inicializacion: otro dict donde sus valores se veran afectados dependiendo de la colision
    """
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

def cambiar_string_click(rects:dict, posicion_click:tuple , respuesta_usuario:str)->str:
    """
    Funcion que modifica el valor de un string dependiendo si un punto colisiono en una region

    Parametros:
        rects: un diccionario donde todos sus valores son regiones
        posicion_click: una tupla que determina un punto en el eje
        respuesta_usuario: un string que se alterara dependiendo de la colision
    Retorno:
        devuelve "a" si colisiono con el la region OPCION_A, si coliciono con la region OPCION_B devuelve "b"
        si en cambio colisiono con la region OPCION_C, devuelve "c"
    """
    if rects[OPCION_A].collidepoint(posicion_click):
        respuesta_usuario = "a"
    elif rects[OPCION_B].collidepoint(posicion_click):
        respuesta_usuario = "b"
    elif rects[OPCION_C].collidepoint(posicion_click):
        respuesta_usuario = "c"
    return respuesta_usuario

def leer_score(score:str)->list:
    """
    Funcion que lee un archivo tipo csv y devuelve el texto

    Parametros:
        score: un string que representa el nombre del archivo
    
    Retorno:
        Devuelve una lista anidada, donde cada sublista representa dada fila del texto, sin los saltos de linea,
        y las columnas las determina el separador "," 
    """
    texto = []
    try:
        with open(score,"r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                linea = linea.split(",")
                texto.append(linea)
    except: FileNotFoundError
    return texto

def ordenar_score_ascendentemente(matriz_usuarios:list):
    """
    funcion que ordena ascendentemente una matriz segun el comparamiento del segundo elemento de cada sublista
    
    Parametros:
        matriz_usuarios: una lista anidada

    """
    for i in range(len(matriz_usuarios)-1):
        for j in range(i+1,len(matriz_usuarios)):
            if int(matriz_usuarios[i][1]) > int(matriz_usuarios[j][1]):
                aux = matriz_usuarios[i]
                matriz_usuarios[i] = matriz_usuarios[j]
                matriz_usuarios[j] = aux

def renderizar_score(matriz_texto:list, fuente:pygame.font.Font, color:tuple)->list:
    """
    Funcion que renderiza todos los valores de una matriz con una fuente y un color

    Parametros:
        matriz_texto: una lista anidada, todos sus elementos deben ser str
        fuente: un fuente, que determina el tipo de texto y el tamaño de la imagen del texto
        color: una tupla, el color del texto al pasarlo a imagen
    Retorno:
        Devuelve una lista anidada, en el mismo orden en que estuvo en el parametro, sale la lista anidada
    """
    lista_imagenes_puntuaciones = []
    for i in range(len(matriz_texto)):
        lista_imagenes_puntuacion = []
        for j in range(len(matriz_texto[i])):
            imagen = fuente.render(matriz_texto[i][j],True,color)
            lista_imagenes_puntuacion.append(imagen)
        lista_imagenes_puntuaciones.append(lista_imagenes_puntuacion)
    return lista_imagenes_puntuaciones

def imprimir_score(pantalla:pygame.Surface,matriz_imagenes:list ,punto_inicio:tuple, distancia_entre_imagenes:tuple, color:tuple):
    """
    Funcion que imprime el score separandolo con dibujos de lineas en nombre y puntuacion

    Parametros: 
        pantalla: Una superficie que es donde se imprimiran todos las imagenes
        matriz_imagenes: una lista anidada donde todos sus elementos son imagenes:
        punto_inicio: una tupla que indica el punto de origen de la primera imagen, determinando la ubicacion de las demas
        distancia_entre_imagenes: una tupla donde sus valores indicas el distancia maxima entre imagenes
        color: una tuple que determina el color de la linea
    """
    pygame.draw.line(pantalla,color,(0,100),(900,100),4)
    pygame.draw.line(pantalla,color,(400,0),(400,700),4)
    eje_x = punto_inicio[0]
    eje_y = punto_inicio[1]
    for i in range(len(matriz_imagenes)):
        for j in range(len(matriz_imagenes[i])):
            pantalla.blit(matriz_imagenes[i][j],[eje_x,eje_y])
            eje_x += distancia_entre_imagenes[0]
        eje_x = punto_inicio[0]
        eje_y += distancia_entre_imagenes[1]

