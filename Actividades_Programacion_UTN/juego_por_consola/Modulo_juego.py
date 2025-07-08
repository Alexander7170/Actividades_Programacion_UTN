
def pedir_dato(mensaje:str)->str:
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

def verificar_palabra(palabra:str, palabra_a_comparar:str)->bool:
    """
    Funcion que verifica si la primera palabra es igual a la segunda palabra pasado como paremetro

    Parametros:

    palabra: un string que la que compararemos con la otra palabra

    palabra_a_comparar: un string que se usara como la comparacion de la otra palabra

    Retorno:
        Devuelve un booleano verdadero si ambas palabras son iguales, sino devuelve falso 
    """
    palabras_iguales = False
    if palabra == palabra_a_comparar:
        palabras_iguales = True
    return palabras_iguales

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

def imprimir_valores(diccionario:dict, clave_excepcion:str):
    """
    Funcion que imprime todos los valores del diccionario, excepto el valor que este dentro de una clave. 
    En paralelo, imprime por cada valor del diccionario, un valor de la lista de encabezados, osea el encabezado
    de cada valor

    Parametros:
    
    diccionario: un dicccionario donde imprimeros todos sus valores excepto el valor con la clave_respuesta

    clave_respuesta: un string que indica que indica que valor no se imprimira

    """
    for clave in diccionario:
        if clave != clave_excepcion: 
            print((clave) + " : " + diccionario[clave])

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

def buscar_pregunta(lista:list)->dict:
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

def eliminar_una_pregunta(lista:list, valor_a_eliminar:dict):
    """
    Funcion que elimina un diccionario dentro de la lista de diccionarios

    Parametros:

    lista: la lista de diccionarios donde se encuentra el diccionario que se  eliminara

    diccionario_eliminar: un diccionario el cual existe en la lista y es el que vamos a eliminar:

    """
    lista.remove(valor_a_eliminar)



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

def mover_usuario(indice_usuario:int, criterio:bool, avanzar:int, retroceder:int)->int:
    """
    funcion que mueve al usuario dependien de un criterio, si es verdadero el usuario avanza
    si el falso el usuario retrocede

    Parametros:

    indice_usuario: un entero que determina en donde esta parado el usuario

    criterio: un booleano que determina si el usuario tiene que avanzar o retroceder

    avanzar: un entero que indica cuantos casilleros avanzara

    retroceder: un entero que indica cuantos casilleros retrocedera 

    Retorno:
        devuelve un entero que indicaria la posicion donde quedo el usuario
    """
    if criterio:
        indice_usuario += avanzar
    else:
        indice_usuario -= retroceder
    return indice_usuario

def buscar_movimiento_adicional(tablero:list , indice:int)->int:
    """
    funcion que busca en el tablero, el valor que esta en un indice

    Parametros:

    tablero: una lista que determina el tablero

    indice: un entero que determina un indice

    Retorno:
        devuelve un valor que esta en ese indice del tablero
    """
    return tablero[indice]

def mover_adicional_usuario(indice_usuario:int,criterio:bool, adicional:int)->int:
    """
    funcion que mueve al usuario adicionalmente segun el criterio, si es verdadero avanza, si es falso retrocede

    Parametros:

    indice_usuario: entero determina el indice del usuario

    criterio: un booleano que influye si el usuairo avanza o retroce adicionalmente

    adicional: un entero que indica la cantidad de casilleros que se movera el usuario

    Retorno:
        devuelve un entero que indica la posicion actual del usuario despues del movimiento
    """
    if criterio:
        indice_usuario += adicional
    else:
        indice_usuario -= adicional
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

