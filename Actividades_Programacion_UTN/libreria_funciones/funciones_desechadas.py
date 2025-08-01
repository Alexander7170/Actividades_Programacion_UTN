#   FUNCIONES DESECHADAS

# """ FUNCION QUE VALIDA UN INDICE DENTRO DE LA LISTA (MAYOR A 0, MENOR A LA CANTIDAD DE ELEMENTOS DE LA LISTA -1 )
#     DEVUELVE ESE INDICE VALIDADO """

def validar_indice_dentro_lista(tablero:list, indice:int)->int:
    while indice < 0:
        indice += 1
    while indice > len(tablero) - 1:
        indice -= 1
    return indice

# """ FUNCION QUE COMPROBABA SI EL MOVIMIENDO TOTAL EXTRA QUE TIENE EL USUARIO ES MAYOR
#     A LA CANTIDAD TOTAL DE CASILLEROS O ES MENOR A 0"""
def verificar_movimiento_extra(tablero:list, mover_extra:int, indice_usuario:int)->bool:
   posible = True
   if (indice_usuario + 1 + mover_extra) > len(tablero) - 1 or (indice_usuario - 1 + mover_extra) < 0:
       posible = False
   return posible
# """
# FUNCIONES QUE VALIDABAN LOS AVANCES O RETROCESOS EXTRAS, POR SI LA ESCALERA O SERPIENTE
#     SUBIAN O BAJABAN EN EL CASILLERO MENOR A 0 O MAYOR AL NUMERO TOTAL DE CASILLEROS """
def validar_avance_extra(tablero:list, avanzar:int, indice_usuario:int)->int:
   while avanzar + 1 + indice_usuario > len(tablero) - 1:
       avanzar -= 1
   return avanzar

def verificar_booleanos_iguales(bool_1:bool, bool_2: bool, bool_3: bool) ->bool:
    """
    Funcion que compara 3 valores booleanos, si son iguales o no

    Parametro:
    bool_1: un booleano que se comparara con los otros

    bool_2: Otro booleano que sera comparado con los otros

    bool_3: ultimo booleano que tambien sera comparado con los otros

    Retorno:
        deuvelve un booleano verdadero si los 3 booleanos pasados como parametros son iguales, sino devuelve falso
    """
    iguales_booleanos = False
    if bool_1 == bool_2 == bool_3:
        iguales_booleanos = True
    return iguales_booleanos
def validar_retroceso_extra(retroceder:int, indice_usuario:int)->int:
    while retroceder - 1 + indice_usuario < 0:
        retroceder += 1
    return retroceder

def retroceder_casilleros(lista:list, indice_usuario:int, n_retroceso:int, cant_move_extra:int):

    lista[indice_usuario - n_retroceso + cant_move_extra] = lista[indice_usuario]

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

def ubicar_usuario(lista:list, indice:int, usuario:str):
    """
    Funcion que reemplaza el valor en ese indice por el usuario

    Parametros:

    lista: la lista donde usaremos un indice para reemplazar su valor de ese indice por usuario

    indice: un netero que significara el indice donde estara el usuario

    usuario: un string que sera el valor que estara en ese indice de la lista
    """
    lista[indice] = usuario

def actualizar_tablero_segun_indice(tablero:list, indice_usuario:int):
    """
    Funcion que convierte los numeros positivos en negativos solo a los valores que sean anterior al indice usuario
    Y convierte los numeros negativos en positivos solo a los valores que sean posteriores al indice usuario

    Parametros:
    
    tablero: una lista de numeros y el nombre del usuario
    
    indice_usuario: un entero e
    """
    for i in range(len(tablero)):
        if i < indice_usuario and tablero[i] > 0:
            tablero[i] = tablero[i] * -1
        elif i > indice_usuario and tablero[i] < 0:
            tablero[i] = tablero[i] * -1
            
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
    