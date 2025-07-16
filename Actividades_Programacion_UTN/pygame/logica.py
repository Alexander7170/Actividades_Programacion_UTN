def verificar_respuesta(pregunta:dict, respuesta:str, clave_respuesta:str)->bool:
    """
    Funcion que verifica si el parametro respuesta es igual al valor dentro de una clave

    Parametros:
        Pregunta: un diccionario donde se encuentra esa clave
        respuesta: el valor string que compararemos con el valor dentro de la clave
        clave_respuesta: un string que indicara la clave en donde vericaremos
    Retorno:
        Devuelve un booleano verdadero si el valor respuesta es igual al valor dentro de la clave, sino devuelve falso
    """
    acerto = False
    respuesta = respuesta
    if pregunta[clave_respuesta] == respuesta:
        acerto = True
    return acerto

def manejar_pregunta(lista:list)->dict:
    """
    Funcion que busca aleatoriamente un diccionario dentro de la listay la elimina de la lista:
    parametros:
        lista: Lista de diccionarios donde buscaremos un diccionario aleatoriamente
    Retorno:
        devuelve un diccionario cualquiera dentro de la lista
    """
    import random
    pregunta = random.choice(lista)
    lista.remove(pregunta)
    return pregunta

def guardar_score(nombre:str, puntuacion:int):
    """
    Funcion que anexa el nombre y la puntuacion del usuario en un archivo

    Parametros:

    nombre: un string que seria el nombre del usuario y el que primero anexaremos

    puntuacion: un entero que seria el indice del usuario y el segundo que anexaremos
    """
    archivo = open("score.csv", "a")
    archivo.write(nombre + "," + str(puntuacion) + "\n")
    archivo.close()

def mover_usuario(acerto:bool, indice_usuario:int)->int:
    """
    funcion que mueve al usuario dependien de un criterio, si es verdadero el usuario avanza
    si el falso el usuario retrocede

    Parametros:
        indice_usuario: un entero que determina en donde esta parado el usuario
        acerto: un booleano que determina si el usuario tiene que avanzar o retroceder
    Retorno:
        devuelve un entero que indicaria la posicion donde quedo el usuario
    """
    if acerto:
        indice_usuario += 1
    else:
        indice_usuario -= 1
    return indice_usuario

def mover_extra_usuario(acerto:bool, indice_usuario:int, tablero:list)->int:
    """
    Funcion que mueve al usuario dependiendo del valor donde este en el tablero y si acerto o no

    Parametros:
        acerto: un booleano que determina si avanza o retrocede
        indice_usuario: un entero que indica la posicion del usuario
        tablero: una lista que representa el tablero 
    """
    if acerto:
        indice_usuario += tablero[indice_usuario]
    else:
        indice_usuario -= tablero[indice_usuario]
    return indice_usuario

def validar_indice_usuario(indice_usuario:int,tablero:list)->int:
    """
    funcion que valida al indice usuario en el tablero
    Parametros:
        indice_usuario: un entero, indica la posicion del usuario
        tablero: una lista, indica el tablero
    Retorno:
        devuelve el indice del usuario dentro del tablero
    """
    if indice_usuario > len(tablero)-1:
        indice_usuario = 30
    elif indice_usuario < 0:
        indice_usuario = 0
    return indice_usuario

def verificar_fin_juego(indice_usuario:int, tablero:list, preguntas:list)->bool:
    """
    Funcion que verifica si el juego ya a concluido o aun sigue en pie
    
    Parametros:
        indice_usuario: un entero que determina la posicion actual del usuario
        tablero: una lista de enteros, representa el tablero
        preguntas: una lista de diccionaros, representan las preguntas que aun quedas

    Retorno:
        Devuelve un booleano verdadero si el usuario quedo en el ultimo casillero o en el primero
        o si la lista de preguntas esta vacia, sino devuelve falso
    """
    fin_juego = False
    if indice_usuario == 0 or len(preguntas) == 0 or indice_usuario == len(tablero)-1:
        fin_juego = True
    return fin_juego

def jugar_turno(indice_usuario:int, tablero:list, criterio:bool)->int:
    """
    Funcion que controla el indice del usuario, moviendolo y validandolo dentro del tablero
    Parametros:
        indice_usuario: un entero que determina la posicion del usuario
        tablero: una lista que determina el tablero
        criterio: un booleano que determina si el usuario avanza o retrocede
    Retorno:
        devuelve el indice del usuario
    """

    indice_usuario = mover_usuario(criterio,indice_usuario)
    indice_usuario = validar_indice_usuario(indice_usuario,tablero)
    indice_usuario = mover_extra_usuario(criterio,indice_usuario,tablero)
    return indice_usuario

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
    except:FileNotFoundError
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

def obtener_posiciones_matriz_score(matriz_imagenes:list)->list:
    posiciones_imagenes = []
    eje_x = 30
    eje_y = 100
    for i in range(len(matriz_imagenes)):
        posicion_imagen = []
        for j in range(len(matriz_imagenes[i])):
            posicion_imagen.append((eje_x,eje_y))
            eje_x += 400
        posiciones_imagenes.append(tuple(posicion_imagen))
        eje_y += 50
        eje_x = 30
    return tuple(posiciones_imagenes)

def obtener_ubicacion_tablero_imagenes(tablero:list)->list:
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

def obtener_imagenes_fondo_tablero(imagenes:dict,tablero:list,indice_usuario:int)->list:
    """
    Funcion que obtiene las imagenes del fondo del tablero, cambiando su color 
    dependiendo de la posicion del usuario

    Retorna una lista de imagenes del fondo

    """
    imagenes_fondo = []
    for i in range(len(tablero)):
        if i == indice_usuario:
            imagen_fondo = imagenes["casillero_azul"]
        elif tablero[i] == 0:
            imagen_fondo = imagenes["casillero_amarillo"]

        elif i < indice_usuario:
            imagen_fondo = imagenes["casillero_rojo"]
        elif i > indice_usuario:
            imagen_fondo = imagenes["casillero_verde"]
        imagenes_fondo.append(imagen_fondo)
    return imagenes_fondo
