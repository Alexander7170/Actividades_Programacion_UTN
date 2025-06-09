#   Ejercicio 1
"""
Desarrollar una función que reciba una letra y una cadena.
Debe retornar las veces que la letra está incluida en el texto
"""
def contar_veces_letra_en_lista(letra_veces:str, cadena_de_texto:str)->int:
    """
    Funcion que cuenta la cantidad de veces que aparece la letra en la cadena de texto

    Parametros:

    letra_veces: El string, la letra la cual contaremos cuantas veces aparece en la cadena

    cadena_de_texto: un string, en esta cadena sera donde contaremos la cantidad de veces que aparece una letra

    Retorno:
        Un entero que es el numero de veces que aperecio el la letra en la cadena
    """
    contador = 0
    for letra in cadena_de_texto:
        if letra == letra_veces:
            contador +=1
    return contador

#   Ejercicio 2:
"""
Desarrollar una función que reciba una cadena y dos índices.
Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
Si las posiciones no son válidas se debe informar.
"""
def retornar_cadena_entre_dos_indices(cadena_de_texto:str, primer_indice:int, ultimo_indice:int)->str:
    """
    Funcion que retorna una cadena de texto entre dos parametros

    Parametros: 
    
    cadena_de_texto: Un string en la cual retornaremos las letras que esten entre el primero indice y el ultimo indice

    primer_indice: Un entero que actuara como el primer parametro para la cadena de texto

    ultimo_indice: Un entero que actuara como el segundo parametro para la cadena de texto, hasta que letra retornara

    Retorno:
        Un string, la cadena de texto que esta entre los dos incides del la cadena de texto pasada como parametro.
        Si los indices no son posibles en la cadena, retorna un mensaje diciendo "indices invalidos"
    
    """
    texto_entre_indices = ""
    if primer_indice < 0 or ultimo_indice > len(cadena_de_texto):
        texto_entre_indices = "indices invalidos"
    else:
        for i in range(primer_indice,ultimo_indice):
            texto_entre_indices += cadena_de_texto[i]
    return texto_entre_indices

#   Ejercicio 3:
"""
Desarrollar una función “char_at” que recibe una cadena y un número.
Se debe retornar el caracter en la posición indicada por el número si ésta es válida. 
"""
def char_at(cadena_de_texto:str, numero:int)->str:
    """
    Funcion que retorna una letra en la cadena usando un indice como su posicion en la cadena.

    Parametros:
    
    cadena_de_texto: un string que es la cadena de texto donde retornaremos una letra de ella

    numero: Un entero que representara el indice de una letra en la cadena de texto

    Retorno:
        un string, la letra que esta en ese indice en la cadena de texto, si el indice no esta 
        dentro del range de la cadena de texto, no retorna nada 
    """
    if numero > 0 and numero < len(cadena_de_texto):
        return cadena_de_texto[numero]
    
#   Ejercicio 1:
"""
Crear una función que reciba como parámetro una cadena y determine la
cantidad de vocales que hay de cada una (individualmente). La función
retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
la cantidad.
"""
def contar_vocales_en_cadena(cadena_de_texto:str)->list:
    """
    Funcion que cuenta individialmente cada vocal de la cadena_de_texto

    Parametros:
    
    cadena_de_texto: Un string, la cadena la cual contaremos su vocales individualmente

    Retorno:
        devuelve una lista anidada, que donde su la primera columna de cada fila es la vocal 
        y su segunda columna es la cantidad de veces que aparecio en la cadena de texto
    """
    lista = [["a",0],["e",0],["i",0],["o",0],["u",0]]
    contador_vocal = 0
    for letra in cadena_de_texto:
        if letra == "a":
            contador_vocal += 1
            lista[0][1] += contador_vocal
            contador_vocal_ = 0
        elif letra == "e":
            contador_vocal_ += 1
            lista[1][1] += contador_vocal
            contador_vocal = 0
        elif letra == "i":
            contador_vocal += 1
            lista[2][1] += contador_vocal
            contador_vocal = 0
        elif letra == "o":
            contador_vocal += 1
            lista[3][1] += contador_vocal
            contador_vocal = 0
        elif letra == "u":
            contador_vocal += 1
            lista[4][1] += contador_vocal
            contador_vocal = 0
    return lista

#   Ejercicio 2
"""
Crear una función que reciba una cadena y un caracter. La función deberá
devolver el índice en el que se encuentre la primera incidencia de dicho
caracter, o -1 en caso de que no esté.
"""
def buscar_una_letra_en_cadena(cadena:str, caracter:str)->int:
    """
    Funcion que busca la primera incidencia de una letra en la cadena de texto y devuelve su posicion

    Parametros:

    cadena: Un string, la cadena de texto donde buscarames una letra en ella

    caracter: Un string, la letra que buscaremos en la cadena de texto

    Retorno:
        Un entero que indica la posicion de la primera incidencia de la letra en la cadena de texto
    """
    indice = -1
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            indice = i
            break
    return indice

#   Ejercicio 3:
"""
Crear una función que reciba como parámetro una cadena y determine si la
misma es o no un palíndromo. Deberá retornar un valor booleano indicando
lo sucedido.
"""
def verificar_cadena_palindromo(cadena_de_texto:str)->bool:
    """
    Funcion que verifica si la cadena de texto es palindromo

    Parametros:

    cadena_de_texto: un string que es la cadena que invertiremos sus letras y verificaremos si es palindromo

    Retorno:
        Un booleabla, True si es la cadena es palindromo o false si no lo es
    """
    es_palindromo = False
    cadena_de_texto_al_reves = ""
    for i in range(len(cadena_de_texto)):
        cadena_de_texto_al_reves += cadena_de_texto[len(cadena_de_texto)-1-i]
    if cadena_de_texto == cadena_de_texto_al_reves:
        es_palindromo = True
    return es_palindromo

#   Ejercicio 4:
"""
Crear una función que reciba como parámetro una cadena y suprima los
caracteres repetidos.
"""
def suprimir_caracteres_repetidos(cadena_de_texto:str)->str:
    """
    Funcion que suprimira los caracteres repetidos de una cadena de texto:

    Parametros:

    cadena_de_texto: Un string que es la suprimiremos las letras que tenga repetidas

    Retorno:
        un string, La cadena de texto original sin la letras repetidas
    """
    nueva_cadena = ""
    flag = True
    for letra in cadena_de_texto:
        if flag:
            nueva_cadena += letra
            flag = False
        else:
            for i in range(len(nueva_cadena)):
                if letra == nueva_cadena[i]:
                    break
                elif i == len(nueva_cadena)-1:
                    nueva_cadena += letra
    return nueva_cadena

#   Ejercicio 5:
"""
Crear una función que reciba una cadena por parámetro y suprima las
vocales de la misma.
"""
def suprimir_vocales_de_cadenas(cadena_de_texto:str)->str:
    """
    Funcion que suprimira las voales de una cadena de texto:

    Parametros:

    cadena_de_texto: Un string que es la suprimiremos sus vocales

    Retorno:
        un string, La cadena de texto original sin las vocales
    """
    nueva_cadena = ""
    vocales = ["a","e","i","o","u"]
    for letra in cadena_de_texto:
        for i in range(len(vocales)):
            if letra == vocales[i]:
                break
            elif i == len(vocales)-1:
                nueva_cadena += letra
    return nueva_cadena

#   Ejercicio 6:
"""
Crear una función para contar cuántas veces aparece una subcadena dentro
de una cadena.
"""
def contar_subcadenas_en_cadenas(cadena_de_texto:str, sub_cadena:str)->int:
    """
    """
    contador = 0
    print(len(cadena_de_texto))
    print(len(sub_cadena))
    for i in range(len(cadena_de_texto)-len(sub_cadena)+1):
        for j in range(len(sub_cadena)):
            if sub_cadena[j] == cadena_de_texto[i+j]:
                if j == len(sub_cadena)-1 :
                    contador += 1    
            else:
                break
    return contador

print(contar_subcadenas_en_cadenas("alexa","alexa"))

def contar_subcadenas_en_cadenas_v1(cadena_de_texto:str, sub_cadena:str)->int:
    contador = 0
    len_sub = len(sub_cadena) #3
    len_texto = len(cadena_de_texto)#5

    for i in range(len_texto - len_sub + 1):#3
        es_igual = True
        for j in range(len_sub): #3
            if cadena_de_texto[i + j] != sub_cadena[j]:
                es_igual = False
                break
        if es_igual:
            contador += 1

    return contador

 
            
