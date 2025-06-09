def pedir_posicion_tridimencional(fila:int, columna:int, h:int)->list:
    lista_ubicacion_tridimencional = [fila - 1, columna - 1,h - 1]
    return lista_ubicacion_tridimencional

def subtituir_string_en_lista_tridimencional(lista:list, valor_original:str, valor_nuevo:str):
    """
    Esta funcion subtituye un valor de tipo string de una lista tridimencional,
    por un valor de tambien de tipo string que se pasa por el ultimo parametro

    Parametros:

    lista: Son listas anidadas que es donde vamos a subtituir el parametro valor_original por el valor_nuevo

    valor_original: Es un string que se encuentra en la lista y la que vamos a cambiar por otro valor

    valor_nuevo: Es un string que es la que subtituira al valor pasado como parametro valor_original

    """
    subtituyo = False
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            for h in range(len(lista[i][j])):
                if lista[i][j][h] == valor_original:
                    lista[i][j][h] = valor_nuevo
                    subtituyo = True
                    break
            if subtituyo:
                break
        if subtituyo:
            break

def subtituir_entero_en_lista_tridimencional(lista:list, valor_original:int, valor_nuevo:int):
    """
    Esta funcion subtituye un valor de tipo entero de una lista tridimencional,
    por un valor de tambien de tipo entero que se pasa por el ultimo parametro

    Parametros:

    lista: Son listas anidadas que es donde vamos a subtituir el parametro valor_original por el valor_nuevo

    valor_original: Es un entero que se encuentra en la lista y la que vamos a cambiar por otro valor

    valor_nuevo: Es un entero que es la que subtituira al valor pasado como parametro valor_original

    """
    subtituyo = False
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            for h in range(len(lista[i][j])):
                if lista[i][j][h] == valor_original:
                    lista[i][j][h] = valor_nuevo
                    subtituyo = True
                    break
            if subtituyo:
                break
        if subtituyo:
            break

def verificar_existencia_string_en_lista_tridimencional(lista_tridimencional:list, valor:str,)->bool:
    """
    Esta funcion verifica si la cadena de texto ya existe o no en la lista

    Parametros:

    lista_tridimencional: Son listas anidadas la cual se recorrera verificando si existe el producto en esa lista

    valor: Es el string que buscaremos en la lista
    
    Retorno:

    Si el valor existe retorna verdadero, sino retorna falso

    """
    existe_string = False
    seguir_iterando = True
    for i in range(len(lista_tridimencional)):
        for j in range(len(lista_tridimencional[i])):
            for h in range(len(lista_tridimencional[i][j])):
                if valor == lista_tridimencional[i][j][h]:
                    existe_string = True
                    seguir_iterando = False
                    break
            if seguir_iterando == False:
                break
        if seguir_iterando == False:
            break
    return existe_string

def verificar_indice_con_string_en_lista_tridimencional(lista_tridimencional:list, fila:int, columna:int, altura:int)->bool:
    """
    Esta funcion verifica si existe o no una cadena de texto en 3 indices de la en una lista tridimencional.

    Parametros:

    lista_tridimencional: listas anidadas que es donde se busca el valor en una sola coordenada

    fila: un entero que actuara como un indice, la fila en donde verificara si existe un valor

    columan: Un entero que actuara como un indice, para la columna en donde verificara si existe un valor

    altura: un entereo que actuara como un indice, para la tercera dimencion en donde verificara si existe un valor

    Retorna falso si el no hay un cadena de texto en ese indice, si lo hay, retorna verdadero
    """
    existe_valor_en_un_indice = True
    if lista_tridimencional[fila][columna][altura] == "":
        existe_valor_en_un_indice = False
    return existe_valor_en_un_indice

def asignar_string_en_lista_tridimencional(lista_tridimencional:list, valor:str, fila:int, columna:int, altura:int):
    """
    Esta funcion Agregara un string en la lista con los indices pasados como parametros

    Parametros: 

    lista_tridimencional: Son listas anidadas que es donde vamos a agregar el string y la cantidad en la misma sublista

    valor: En un string que se usara para agregarlo en la lista tridimencional.
    
    fila: Es un entero que determina la fila en la que estara el string en la lista tridimencional

    columna: Es un entero que determina la columna en la que estara el string en la lista tridimencional

    altura: Es un entero que determina en que indice de la sublista de la sublista ira en la lista  tridimencional

    
    """
    lista_tridimencional[fila][columna][altura] = valor

def asignar_entero_en_lista_tridimencional(lista_tridimencional:list, valor:int, fila:int, columna:int, altura:int):
    """
    Esta funcion Agregara el numero entero en la lista tridimencional con los indices pasados como parametros

    Parametros: 

    lista_tridimencional: Son listas anidadas que es donde vamos a agregar el entero 

    valor: En un entero que se usara para agregarlo en la lista tridimencional.
    
    fila: Es un entero que determina la fila en la que estara el entero en la lista tridimencional

    columna: Es un entero que determina la columna en la que estara el numero en la lista tridimencional

    altura: Es un entero que determina en que indice de la sublista ira el numero entero en la lista tridimencional

    
    """
    lista_tridimencional[fila][columna][altura] = valor

def buscar_segun_posicion_un_string_en_lista_tridimencional(lista_tridimencional:list, fila:int, columna:int, altura:int)->str:
    """
    Funcion que buscara segun una coordenada y retornara un el elemento de tipo cadena de texto 
    
    Parametros: 

    lista_tridimencional: Listas anidadas que es donde vamos a buscar una coordenada en ella

    fila: Un entero que determina la fila donde buscaremos el string

    columna: Un entero que determina la columna en donde buscaremos el string

    altura: Un entero que determina la altura en donde buscaremos el string

    Retornara la cadena de texto que se encuentra en tal fila, tal columna y tal altura
    """
    return lista_tridimencional[fila][columna][altura]

def buscar_segun_posicion_un_entero_en_lista_tridimencional(lista_tridimencional:list, fila:int, columna:int, altura:int)->int:
    """
    Funcion que buscara segun una coordenada y retornara un el elemento de tipo numerico entero 
    
    Parametros: 

    lista_tridimencional: Listas anidadas que es donde vamos a buscar una coordenada en ella

    fila: Un entero que determina la fila donde buscaremos el numero

    columna: Un entero que determina la columna en donde buscaremos el numero

    altura: Un entero que determina la altura en donde buscaremos el numero

    Retornara numero entero que se encuentra en tal fila, tal columna y tal altura
    """
    return lista_tridimencional[fila][columna][altura]

def buscar_posiciones_de_string_en_lista_tridimencional(lista_tridimencional:list, nombre_producto:str,)->list:
    """
    Funcion que me buscara la coordenada del string en la listra tridimencional para retornarlo

    Parametros:

    lista_tridimencional: listas anidadas que es donde buscaremos las coordenadas del string

    nombre_producto: Es un string que existe en la lista y con una coordenada que queremos retornar

    Retorna una lista con la coordenada del string, en donde su primer elemento o indice
    es la fila del string, su segundo elemento en la columna y su tercer elemento es la altura

    """
    lista_ubicacion_tridimencional = []
    encontro = False
    for i in range(len(lista_tridimencional)):
        for j in range(len(lista_tridimencional[i])):
            for h in range(len(lista_tridimencional[i][j])):
                if nombre_producto == lista_tridimencional[i][j][h]:
                    lista_ubicacion_tridimencional.append(i)
                    lista_ubicacion_tridimencional.append(j)
                    lista_ubicacion_tridimencional.append(h)
                    encontro = True
                    break
            if encontro:
                break
        if encontro:
            break

    return lista_ubicacion_tridimencional
    
def intercambiar_valores_en_lista_tridimencional(lista_tridimencional:list, lista_posiciones_1: list, lista_posiciones_2: list):
    """
    Esta funcion va a intercambiar dos valores de la lista tridimencional usando sus coordenadas
    que pasan como parametros en forma de listas

    Paramatros:

    lista_tridimencional: son listas anidadas, que es donde vamos a poder cambiar valores dentro de la lista segun sus coordenadas

    lista_posiciones_1: Esta lista tiene como elementos una coordenada de la lista tridimencional,
    siendo primer indice la fila, segundo la columna y el ultimo la altura.

    lista_posiciones_2: Esta lista tiene como elementos otra coordenada que es con la que vamos a intercambiar
    los valores que esten representen las coordenadas. Su primer indice es su fila del valor, su segundo la columna
    y el ultimo la altura

    """
    aux = lista_tridimencional[lista_posiciones_1[0]][lista_posiciones_1[1]][lista_posiciones_1[2]]
    lista_tridimencional[lista_posiciones_1[0]][lista_posiciones_1[1]][lista_posiciones_1[2]] = lista_tridimencional[lista_posiciones_2[0]][lista_posiciones_2[1]][lista_posiciones_2[2]]
    lista_tridimencional[lista_posiciones_2[0]][lista_posiciones_2[1]][lista_posiciones_2[2]] = aux

def mostrar_listas_tridimencionales_v1(gondola:list):
    """
    Muestra una lista tridimencional de manera personalizada
    """
    for i in range(len(gondola)):
        for j in range(len(gondola[i])):
            if gondola[i][j][1] != "":
                print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("Posicion: ",gondola[i][j][0], "Producto: ", gondola[i][j][1], "Cantidad: ", gondola[i][j][2]))

def transformar_lista_tridimencional_en_bidimencional(lista_tridimencional:list)->list:
    """
    Esta funcion va a transformar una lista de tres dimenciones, una lista con filas, columans y altura, en una lista
    bidimencional, con solo columna y filas

    Parametros:

    lista_tridimencional: son listas anidadas que es la que vamos a convertir en solo una lista anidada,

    Retorna una lista bidimencional con los elementos de la lista tridimencional pero sin la ultima anidacion
    """
    lista_bidimencional = []
    for i in range(len(lista_tridimencional)):
        for j in range(len(lista_tridimencional[i])):
            lista_bidimencional.append(lista_tridimencional[i][j])

    return lista_bidimencional

def transformar_lista_bidimencional_en_tridimencional(lista_bidimencional:list, lista_tridimencional:list)->list:
    """
    Esta funcion transforma una lista bidimenional, de columnas y filas, en una tridimencional, de columnas, filas y altura

    Paramatros: 

    lista_bidimencional: es una lista anidada en donde agregaros sus elementos a una nueva lista tridimencional

    lista_tridimencional: son listas anidadas en donde la cantidad de columnas que tenga esta lista determinara la 
    cantidad de columnas y filas de la lista nueva tridimencional

    Retornara una lista tridimencional donde cada elemento de la lista bidimencional pasa a tener un indice de i,j,h 
    y su estructura, columnas y filas, lo determinara la lista bidimencional. 
    
    """
    contador = 0
    lista_nueva = []
    columna = len(lista_tridimencional[0])
    lista_altura = []

    for elemento in (lista_bidimencional):
        lista_altura.append(elemento)
        contador += 1
        if contador == columna:   
            lista_nueva.append(lista_altura)
            lista_altura = []
            contador = 0
    return lista_nueva

def ordenar_lista_bidimencional_v1(lista_bidimencional:list):
    for i in range(len(lista_bidimencional)-1):
        for j in range(i+1,len(lista_bidimencional)):
            if lista_bidimencional[i][1] > lista_bidimencional[j][1]:
                aux = lista_bidimencional[i]
                lista_bidimencional[i] = lista_bidimencional[j]
                lista_bidimencional[j] = aux
    return lista_bidimencional

def cambiar_posicion_producto_bidimencional (lista_bidimencional:list, lista_posiciones_1:list, lista_posiciones_2:list):
    
    """
    Esta funcion va a intercambiar dos valores de la lista bicondicional usando sus indices
    que pasan como parametros en forma de listas

    Paramatros:

    lista_bidimencional: Una lista anidada que es donde vamos a poder cambiar valores dentro de la lista segun los indices

    lista_posiciones_1: Esta lista tiene como elementos 2 indices de la lista bicondicional,
    siendo primer indice la fila y segundo la columna.

    lista_posiciones_2: Esta lista tiene como elementos otros 2 indices de la lista bicondicional,
    siendo su primer indice es su fila del valor y su segundo la columna

    """
    aux = lista_bidimencional[lista_posiciones_1[0]][lista_posiciones_1[1]]
    lista_bidimencional[lista_posiciones_1[0]][lista_posiciones_1[1]] = lista_bidimencional[lista_posiciones_2[0]][lista_posiciones_2[1]]
    lista_bidimencional[lista_posiciones_2[0]][lista_posiciones_2[1]] = aux

def buscar_en_lista_tridimencional_string_posiciones(lista:list, eje_tridimencional_string_h:int)->list:
    lista_con_posiciones_string = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if len(lista[i][j][eje_tridimencional_string_h]) > 0:
                lista_con_posiciones_string.append([i,j,eje_tridimencional_string_h])
    return lista_con_posiciones_string

def buscar_en_lista_tridimencional_string_elementos(lista:list, eje_tridimencional_string_h:int)->list:
    lista_con_posiciones_string = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if len(lista[i][j][eje_tridimencional_string_h]) > 0:
                lista_con_posiciones_string.append(lista[i][j][eje_tridimencional_string_h])
    return lista_con_posiciones_string

def buscar_en_lista_tridimencional_enteros_elementos(lista:list, eje_tridimencional_string_h:int)->list:
    lista_con_posiciones_string = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j][eje_tridimencional_string_h] != 0:
                lista_con_posiciones_string.append(lista[i][j][eje_tridimencional_string_h])
    return lista_con_posiciones_string
    
def imprimir_elementos_tridimencional(lista:list, lista_posiciones:list):
    for i in range(len(lista_posiciones)):
        print(f" {lista[lista_posiciones[i][0]][lista_posiciones[i][1]][lista_posiciones[i][2]]}")
    
def imprimir_booleano(t_f: bool)->bool:
    return t_f

def imprimir_menu_de_opciones_v1():
    print("1-Alta de productos (producto nuevo)\n"\
        "2-Baja de productos (producto existente)\n"\
        "3-Modificar productos (cantidad, ubicación)\n"\
        "4-Listar productos \n"\
        "5-Lista de productos ordenado por nombre \n" \
        "6-Salir")
    
def imprimir_menu_de_opciones_v2():
    print("1-Reponer mercaderia \n"\
        "2-Vender mercadería \n"\
        "3-Listar inventario\n"\
        "4-Salir")

def mostrar_listas_tridimencionales_v2(estanteria:list):
    """
    Muestra una lista tridimencional de manera personalizada
    """
    for i in range(len(estanteria)):
        for j in range(len(estanteria[i])):
            if estanteria[i][j][1] != "":
                print("{:<15}{:<15}{:<15}{:<10}".format("Producto: ", estanteria[i][j][0], "Cantidad: ", estanteria[i][j][1]))
def imprimir_dependiendo_bool(booleano: bool, verdadero:str, falso:str):

    if booleano:
        print(verdadero)
    else:
        print(falso)

def cambiar_indice_de_una_lista_de_indices(lista_de_indices:list, indice_en_lista_a_cambiar:int, valor_indice_a_reemplazarlo:int)->list:
    lista_de_indices[indice_en_lista_a_cambiar] = valor_indice_a_reemplazarlo
    return lista_de_indices
def sumar_elementos_usando_indices_tridimencional(lista_tridimencional:list, lista_indices_1:list, lista_indices_2:list)->int:
    suma = lista_tridimencional[lista_indices_1[0]][lista_indices_1[1]][lista_indices_1[2]] + lista_tridimencional[lista_indices_2[0]][lista_indices_2[1]][lista_indices_2[2]]
    return suma
def sumar_numeros(numero_1:int, numero_2:int)->int:
    return numero_1 + numero_2
def restar_numeros(numero_1:int, numero_2_negativo:int)->int:
    return numero_1 - numero_2_negativo
def verificar_entero_por_un_minimo(minimo:int,numero:int)->bool:
    numero_mayor_al_minimo = True
    if numero < minimo:
        numero_mayor_al_minimo = False
    return numero_mayor_al_minimo
def pedir_entero_mayor_al_minimo(mensaje:str,minimo:int)->int:
    numero = int(input(mensaje))
    if numero < minimo:
        numero = int(input(minimo))
    return numero

    