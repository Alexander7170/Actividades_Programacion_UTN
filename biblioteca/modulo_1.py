

def pedir_numero_con_parmaetros(mensaje:str,minimo:int, maximo:int)->int:
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        numero = int(input("error ",mensaje))
    return numero
def verificar_tesoro(mapa: list, x: int, y: int) -> int:
    distancia = 0
    if mapa[x][y] == 0:
        ecuacion_1 = (x - 1)
        ecuacion_2 = (x - 3)
        if ecuacion_1 < 0:
            ecuacion_1 *= -1
        if ecuacion_2 < 0:
            ecuacion_2 *= -1
        distancia = ecuacion_1 + ecuacion_2
    return distancia

def lista_misma_columna(matriz:list)->list:
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i < len(matriz)-2:
                if matriz[i+2][j] == matriz[i][j] == matriz[i+1][j]:
                    lista.append(matriz[i][j])
    return lista

#   Cadena de Caracteres

def transform_list_dict(keys:list, values:list)->dict:
    """
    Funcion que arma items, obteniendo sus claves con los valores usando sus indices
    """
    items = {}
    for i in range(len(keys)):
        items[keys[i]] = values[i]
    return items

def cant_letras(letras:list, texto:str)->dict:
    """
    funcion que cuenta la cantidad de letra que hay de la lista de letra, en la cadena de texto.
    Devuelve un diccionario, donde sus claves son las letras a buscar y sus valores son las coincidencias que se encontro
    """
    lista_contadores = [0]*len(letras)
    items = transform_list_dict(letras, lista_contadores)
    for i in range(len(texto)):
        for key in items:
            if key == texto[i]:
                items[key] += 1
    return items

def buscar_letra(letra:str, texto:str)->int:
    """
    Funcion que busca la primera incidencia de una letra en la cadena de texto y devuelve su posicion

    Parametros:

    cadena: Un string, la cadena de texto donde buscarames una letra en ella

    caracter: Un string, la letra que buscaremos en la cadena de texto

    Retorno:
        Un entero que indica la posicion de la primera incidencia de la letra en la cadena de texto
    """
    indice = -1
    for i in range(len(texto)):
        if letra == texto[i]:
            indice = i
            break
    return indice

def supr_letras_repetidas(texto:str)->str:
    """
    Funcion que suprimira los caracteres repetidos de una cadena de texto:

    Parametros:
        cadena_de_texto: Un string que es la suprimiremos las letras que tenga repetidas
    Retorno:
        un string, La cadena de texto original sin la letras repetidas
    """
    if len(texto) == 0:
        nueva_cadena = ""
    else:
        nueva_cadena = texto[0]
        letras_repetidas = [texto[0]]
        for letra in texto:
            for i in range(len(letras_repetidas)):
                if letra == letras_repetidas[i]:
                    break
                elif i == len(letras_repetidas)-1:
                    nueva_cadena += letra
                    letras_repetidas.append(letra)
                    break
    return nueva_cadena