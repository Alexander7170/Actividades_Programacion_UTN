
#   RETORNAR LISTA-----------------------------------------------------------------------------------------------------------

def buscar_mismos_elementos(ubicacion:int, lista:list)->list:
    """
    
    """
    posiciones = []                                                     
    for i in range(len(lista)):
        if lista[ubicacion] == lista[i]:
            posiciones.append(i)
    return posiciones

def buscar_indices_por_valor(valor:int|float|str, lista:list)->list:
    """
    busca los indices que tengan el mismo valor en la lista, devuelve los indices donde
    se encuentren ese valor
    """
    posiciones_string = []
    for i in range(len(lista)):
        if valor == lista[i]:
            posiciones_string.append(i)
    return posiciones_string


def buscar_en_determinados_posiciones_mayor_entero(posiciones:list, lista:list)->int: 
    flag = True
    for i in range(len(posiciones)):
        if flag:
            mayor_numero = lista[posiciones[i]]
            posicion_mayor = posiciones[i]
            flag = False
        else:
            if mayor_numero < lista[posiciones[i]]:
                mayor_numero = lista[posiciones[i]]
                posicion_mayor = posiciones[i]
    return posicion_mayor

def buscar_en_determinadas_posiciones_mismo_numero(posicion:int,posiciones:list,lista:list)->list: #
    posiciones_mismos_numeros = []
    for i in range(len(posiciones)):
        if lista[posicion] == lista[posiciones[i]]:
            posiciones_mismos_numeros.append(posiciones[i])
    return posiciones_mismos_numeros

def filtrar_mismos_elementos(lista_a_filtrar:list)->list:
    """
    Funcion que filtra los mismos elementos de la lista, Devuelve una nueva lista ya filtrada
    """
    cant_elementos = len(lista_a_filtrar)
    if cant_elementos == 0:
        lista_filtrada = []
    else:
        lista_filtrada = [lista_a_filtrar[0]]
        for elemento_nuevo in lista_a_filtrar:
            for elemento_repetido in lista_filtrada:
                if elemento_nuevo == elemento_repetido:
                    nuevo = False
                    break
                else:
                    nuevo = True
            if nuevo:
                lista_filtrada.append(elemento_nuevo)
    return lista_filtrada

def interseccion_elementos(lista_1:list, lista_2:list, elementos_duplicados:bool)->list:
    """
    Funcion que busca y retorna los elementos identicos entre las dos listas, sin contar con los duplicados
    """
    copia_lista_1 = lista_1.copy()
    copia_lista_2 = lista_2.copy()
    if not elementos_duplicados:
        copia_lista_1 = filtrar_mismos_elementos(copia_lista_1 )
        copia_lista_2 = filtrar_mismos_elementos(copia_lista_2)
    e_intersecciones = []
    if len(copia_lista_1) <= len(copia_lista_2):
        lista_menor = copia_lista_1 
        lista_mayor = copia_lista_2
    else:
        lista_menor = copia_lista_2
        lista_mayor = copia_lista_1 
    for i in range(len(lista_menor)):
        for j in range(len(lista_mayor)):
            if lista_menor[i] == lista_mayor[j]:
                e_intersecciones.append(lista_menor[i])
    return e_intersecciones


def union_elementos(lista_1:list, lista_2:list, e_duplicados:bool)->list:
    """
    Funcion que suma los elementos de dos listas, queda a decision del usuario si
    se suma tmb lo suplicados o no, devuelde una lista con todos los elementos de ambas
    listas pasadas como parametro
    """
    copia_lista_1 = lista_1.copy()
    copia_lista_2 = lista_2.copy()
    if len(copia_lista_1) <= len(copia_lista_2 ):
        lista_menor = copia_lista_1
        lista_mayor = copia_lista_2 
    else:
        lista_menor = copia_lista_2 
        lista_mayor = copia_lista_1
    for elemento in lista_menor:
        lista_mayor.append(elemento)
    if not e_duplicados:
        lista_mayor = filtrar_mismos_elementos(lista_mayor)
    return lista_mayor

def analizar_valores(analizar_elementos:callable, lista:list, valor:int|float, tipo_retorno:str)->list:
    indices_premisas = analizar_elementos(lista,valor)
    if tipo_retorno == "elemento":
        elementos_premisas = []
        for i in range(len(indices_premisas)):
            elementos_premisas.append(lista[indices_premisas[i]])
        premisa_devuelta = elementos_premisas

    elif tipo_retorno == "flag":
        flags_premisas = []
        contador = 0
        for i in range(len(lista)):
            if i == indices_premisas[contador]:
                flags_premisas.append(True)
                contador += 1
            else:
                flags_premisas.append(False)
        premisa_devuelta = flags_premisas
    elif tipo_retorno == "indice":
        premisa_devuelta = indices_premisas
    else:
        print("Error, se nesesita que el tipo de retorno sea elemento/flag/indice")
        premisa_devuelta = []
    return premisa_devuelta

def buscar_indices_mayores(lista:list, numero:int|float)->list:
    indices = []
    for i in range(len(lista)):
        if lista[i] > numero:
            indices.append(i)
    return indices

def buscar_indices_menores(lista:list, numero:int|float)->list:
    indices = []
    for i in range(len(lista)):
        if lista[i] < numero:
            indices.append(i)
    return indices

def buscar_indices_iguales(lista:list, numero:int|float)->list:
    indices = []
    for i in range(len(lista)):
        if lista[i] == numero:
            indices.append(i)
    return indices

def analizar_lista(lista_numeros:list, opcion:str)->int:
    if opcion == "promedio":
        resultado = buscar_promedio(lista_numeros)
    elif opcion == "mayor_n":
        resultado = buscar_mayor_numero(lista_numeros)
    elif opcion == "menor_n":
        resultado = buscar_menor_numero(lista_numeros)
    else:
        resultado = None
        print("Opcion invalida")
    return resultado

def buscar_mayor_numero(lista:list)->int:
    cant_e = len(lista)
    if cant_e != 0:
        mayor_numero = lista[0]
        posicion = 0
        for i in range(1, cant_e):
            if mayor_numero < lista[i]:
                mayor_numero = lista[i]
                posicion = i
        return posicion

def buscar_menor_numero(lista:list)->int:
    cant_e = len(lista)
    if cant_e != 0:
        menor_numero = lista[0]
        posicion = 0
        for i in range(1,cant_e):
            if menor_numero > lista[i]:
                menor_numero = lista[i]
                posicion = i
        return posicion

def buscar_promedio(lista:list)->int:
    acumulador = 0
    contador = 0
    for numero in lista:
        acumulador += numero
        contador += 1
    promedio = acumulador/ contador
    return promedio



