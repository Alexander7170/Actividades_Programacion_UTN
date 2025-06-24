def imprimir_tablero(tablero:list):
    """
    Funcion que imprime en la primera linea: todos el indice del tablero
    en la segunda linea imprime los valores de cada indice

    Parametros:
    
    tablero: una lista donde imprimiremos todos sus indice y valores
    """
    indices_casilleros = ""
    valores_casilleros = ""
    for i in range(len(tablero)):
        indices_casilleros += str(i) + " " * len(str(tablero[i])) + "|"
        valores_casilleros += str(tablero[i]) + " " * len(str(i)) + "|"
    print("Valores:    ", valores_casilleros)
    print("Casilleros: ", indices_casilleros)

def actualizar_tablero_segun_indice(tablero:list, indice_usuario:int):
    for i in range(len(tablero)):
        if (i < indice_usuario) and (tablero[i] > 0):
            tablero[i] = tablero[i] * -1
        elif (i > indice_usuario) and (tablero[i] < 0):
            tablero[i] = tablero[i] * -1

def verificar_perdedor(indice_usuario:int)->bool:
    """
    Funcion que verifica si indice pasado como parametro es igual a 0, osea que perdio ya

    Parametros:

    indice_usuario: un entero que indica el indice del usuario:

    Retorno:
        Devuelve un booleano verdadero si el el usuario esta en el indice 0, sino, devuelve falso
    """
    perdio = False
    if indice_usuario == 0:
        perdio = True
    return perdio

def verificar_ganador(tablero:list, indice_usuario:int)->bool:
    """
    Funcion que verifica si indice pasado como parametro es igual al ultimo indice del tablero

    Parametros:

    tablero: la lista donde verificaremos si el ultimo indice de esta lista es igual al indice del usuario

    indice_usuario: Un entero que indica el indice del usuario

    Retorno:
        Devuelve un booleano verdadero si el indice del usuario es igual al ultimo indice del tablero, sino devuelve falso
    """
    gano = False
    if indice_usuario == len(tablero) - 1:
        gano = True
    return gano
    
def pedir_string(mensaje:str)->str:
    return input(mensaje)

def validar_string(string:str,opcion1:str, opcion2:str)->str:
    """
    Funcion que obliga al usuario a que el string sea igual a una de la dos opciones

    Parametros:

    string: la cadena de caracter, que validaremos con una de las dos opciones

    opcion1: Una cadena de caracteres, que es la primera opcion que puede tomar el string

    opcion2: Una cadena de caracteres, que es la segunda opcion que puede tomar el string

    RETORNO:
        devuelve un string igual a una de las dos opciones
    """
    string.lower()
    while string != opcion1 and string != opcion2:
        string = input("ponga dentro de las opciones " + opcion1 + "/" + opcion2 + "  :  ").lower()
    return string

def ubicar_usuario(lista:list, indice:int, usuario:str):
    """
    Funcion que reemplaza el valor en ese indice por el usuario

    Parametros:

    lista: la lista donde usaremos un indice para reemplazar su valor de ese indice por usuario

    indice: un netero que significara el indice donde estara el usuario

    usuario: un string que sera el valor que estara en ese indice de la lista
    """
    lista[indice] = usuario

def buscar_usuario(lista:list, usuario:str)->int:
    """
    Funcion que busca al usuario en la lista

    Parametros:

    lista: una lista donde buscaremos en ella el usuario

    usuario: el valor tipo string que se buscara en la lista

    Retorno:
        Devuelve un entero que indica la posicion donde se encuentra el usuario:

    """
    for i in range(len(lista)):
        if lista[i] == usuario:
            return i
        
def verificar_lista_vacia(lista:list)->bool:
    """
    Funcion que comprueba si la lista tiene  o no elementos

    Parametros:

    lista: una lista la cual es la que comprobaremos si esta vacia

    Retorno:
        Devuelve un booleano verdadero si esta vacia, sino devuele falso

    """
    vacia = False
    if len(lista) == 0:
        vacia = True
    return vacia

def imprimir_valores_con_excepcioon(diccionario:dict, clave_excepcion: str):
    """
    Funcion que imprime en un orden secuencial, los elementos de una lista local
    seguido de los valores de las claves del diccionario, excepto una clave

    Parametros:
    
    diccionario: un dicccionario donde imprimeros todos sus valores excepto el valor con la clave_respuesta

    clave_respuesta: un string que indica que indica que valor no se imprimira

    """
    lista_opciones = ["Pregunta","a","b","c","d","e"]
    contador = 0
    for clave in diccionario:
         if clave != clave_excepcion:
            print(lista_opciones[contador]," : ", diccionario[clave])
            contador += 1

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
    if pregunta[clave_respuesta] == respuesta:
        acerto = True
    return acerto

def buscar_dic_random(lista:list)->dict:
    """
    Funcion que busca aleatoriamente un diccionario dentro de la lista:

    parametros:

    lista: Lista de diccionarios donde buscaremos un diccionario aleatoriamente

    Retorno:
        devuelve un diccionario cualquiera dentro de la lista
    """
    import random
    pregunta = random.choice(lista)
    return pregunta

def eliminar_un_dict(lista:list, diccionario_eliminar:dict):
    """
    Funcion que elimina un diccionario dentro de la lista de diccionarios

    Parametros:

    lista: la lista de diccionarios donde se encuentra el diccionario que se  eliminara

    diccionario_eliminar: un diccionario el cual existe en la lista y es el que vamos a eliminar:

    """
    lista.remove(diccionario_eliminar)

def verificar_casillero_vacio(tablero:list, indice_casillero:int)->bool:
    """
    Funcion que comprueba si donde esta el indice del usuario, 
    en ciertos avances,si el casillero donde caeria esta vacio, osea un 0

    Parametros:

    tablero: una lista donde verificaremos si el valor de un indice es igual a 0

    indice_usuario: Un entero que indica donde se encuentra el usuario

    movimiento: Un entero que se le suma al indice del usuario

    Retorno:
        Devuelve un booleano verdadero si el  valor que esta en el
        indice es igual a 0, sino devuelve falso
        """
    casillero_vacio = False
    if tablero[indice_casillero] == 0:
        casillero_vacio = True
    return casillero_vacio

def cant_movimiento_adicionales(tablero_lista:list, indice_us:int)->int:
        """Una funcion recursiva que calcula cuantos casilleros mas tiene que avazar o retroces, en caso de que 
        el jugador cae en ese indice Osea si cayo en una serpiente o escalera, y en consecuencia, 
        cae en otra serpiente o escalera
        
        Parametros:
        
        tablero_lista: Una lista que contiene numeros enteros, y es donde sumo los movimientos concecuentes que tuvo el usuario al caer
        en ese indice 
        
        indice: un entero que representa donde estaria el usuario 
        
        Retorno:
            Devuelve un numero entero, indicando cunatos casilleros mas tiene que avanzar o retrocer"""

        if tablero_lista[indice_us] == 0 :
            return 0
        else:
            return tablero_lista[indice_us] + cant_movimiento_adicionales(tablero_lista , indice_us + tablero_lista[indice_us])

def intercambiar_i_usuario(tablero:list, indice_usuario:int, indice_nuevo_usuario:int):
    """
    Funcion que intercambia el valor dentro del indice_usuario: y el valor dentro del indice usuario mas
    el parametro movimiento:
    
    Parametros:

    tablero: la lista donde haremos el swapeo

    indice_usuario: Un entero que representa el indice del usuario

    movimiento: un entero que se sumara al indice usuario

    """
    aux = tablero[indice_usuario]
    tablero[indice_usuario] = tablero[indice_nuevo_usuario]
    tablero[indice_nuevo_usuario] = aux

def guardar_score(indice_usuario:int, nombre_usuario:str):
    import os
    os.remove("score.csv")
    if os.path.exists("score.csv"):
        archivo = open("score.csv","a")
        archivo.write(f"{nombre_usuario},{indice_usuario} \n ")
    else:
        archivo = open("score.csv","w")
        archivo.write("Nombre,Puntaje \n")
        archivo.write(f"{nombre_usuario},{indice_usuario} \n")
    archivo.close()
