
def importar_lista_true()->bool:
    from biblioteca import listas_personas
    return True

#   IMPRIMIR-------------------------------------------------------------------------------------------------------------
def imprimir_numero(entero:int):
    print(entero)

def imprimir_mensaje(mensaje:str):
    print(mensaje)

def imprimir_float(decimal:float):
    print(decimal)

def imprimir_lista(lista:list):
    print(lista)

def imprimir_datos_brazil(posicion_brazil:list, nombre:list, mail:list, telefono:list,):
   for i in range (len(posicion_brazil)):
       print(f"Nombre: {nombre[posicion_brazil[i]]}, mail: {mail[posicion_brazil[i]]}, telefono: {telefono[posicion_brazil[i]]}")

def imprimir_datos_completos_personas_lista(lista:list, nombre:list, telefono:list, mail:list, address:list, postalZip:list, region:list, pais:list, edades:list ):
    for i in range(len(lista)):
        print(f"Nombre:{nombre[lista[i]]}, telefono: {telefono[lista[i]]}, mail: {mail[lista[i]]}, address: {address[lista[i]]}, postalZip: {postalZip[lista[i]]}, region: {region[lista[i]]}, pais: {pais[lista[i]]}, edad: {edades[lista[i]]}")

#   RETORNAR LISTA-----------------------------------------------------------------------------------------------------------


def guardar_posiciones_en_lista_con_elementos_iguales(ubicacion:int, lista:list)->list:
    posiciones = []                                                                   
    for i in range(len(lista)):
        if lista[ubicacion] == lista[i]:
            posiciones.append(i)
    return posiciones

def buscar_string_en_lista(valor:str, lista:list)->list: 
    posiciones_string = []
    for i in range(len(lista)):
        if valor == lista[i]:
            posiciones_string.append(i)
    #print("las posiciones del string son: ", posiciones_string)
    return posiciones_string

def guardar_con_posiciones_elementos_entre_lista(lista_posiciones:list, lista:list)->list: #FALTA ARREGLAR
    lista_elementos = []
    for i in range(len(lista_posiciones)):
        lista_elementos.append(lista[lista_posiciones[i]])
    #print(lista_elementos)
    return lista_elementos

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

def interseccion_posiciones_en_listas(lista1:list, lista2:list)->list: #solo funciona con listas que contengan posiciones
    posiciones_intersecciones = []
    if len(lista1) <= len(lista2):
        lista_menor = lista1
        lista_mayor = lista2
    else:
        lista_menor = lista2
        lista_mayor = lista1
    for i in range(len(lista_menor)):
        for j in range(len(lista_mayor)):
            if lista_menor[i] == lista_mayor[j]:
                posiciones_intersecciones.append(lista_menor[i])
    if len(posiciones_intersecciones) == 0:
        posiciones_intersecciones = "No se encontro ninguna interseccion"
    #print("las intercessiones de las posiciones son: ", posiciones_intersecciones)
    return posiciones_intersecciones

def unir_posiciones(lista1:list, lista_agregar_posiciones:list)->list:
    lista_posiciones_agregadas = []
    if len(lista1) <= len(lista_agregar_posiciones):
        lista_menor = lista1
        lista_mayor = lista_agregar_posiciones
    else:
        lista_menor = lista_agregar_posiciones
        lista_mayor = lista1
    for i in range(len(lista_menor)):
        for j in range(len(lista_mayor)):
            if lista_menor[i] != lista_mayor[j] and j == len(lista_menor):
                lista_mayor.append(lista_menor[i])
    #print("la union de las posiciones son: ", lista_mayor)
    return lista_mayor

def buscar_elementos_mayores_a_entero(numero:int, lista:list)->list:
    posicion_numeros_mayores = []
    for i in range(len(lista)):
        if lista[i] > numero:
            posicion_numeros_mayores.append(i)
    #print("las posiciones mayores a 8000 son:", posicion_numeros_mayores)
    return posicion_numeros_mayores

#   RETORNAR STRING-------------------------------------------------------------------------------------------------------
def pedir_string(mensaje:str)->str:
    cadena_caracteres = input(mensaje)
    return mensaje

#   RETORNAR INTEGER------------------------------------------------------------------------------------------------------

def pedir_entero(mensaje:str)->int:
    entero = int(input(mensaje))
    return entero

def pedir_entero_con_parametros(mensaje:str, desde:int, hasta:int)->int:
    numero = int(input(mensaje))
    while numero < desde or numero > hasta:
        numero = int(input("error, " + mensaje))
    return numero

def buscar_la_posicion_menor_entero(lista:list)->int:
    flag = True
    for i in range(len(lista)):
        if flag:
            menor_numero = lista[i]
            posicion = i
            flag = False
        else:
            if menor_numero > lista[i]:
                menor_numero = lista[i]
                posicion = i
    return posicion

def buscar_la_posicion_del_mayor_entero(lista:list)->int: # CUARTO
    flag = True
    for i in range(len(lista)):
        if flag:
            mayor_numero = lista[i]
            posicion = i
            flag = False
        else:
            if mayor_numero < lista[i]:
                mayor_numero = lista[i]
                posicion = i
    return posicion

def buscar_el_elemento_del_mayor_entero(lista:list)->int:
    flag = True
    for i in range(len(lista)):
        if flag:
            mayor_numero = lista[i]
            flag = False
        else:
            if mayor_numero < lista[i]:
                mayor_numero = lista[i]
    return mayor_numero

def buscar_el_elemento_del_menor_entero(lista:list)->int:
    flag = True
    for i in range(len(lista)):
        if flag:
            mayor_numero = lista[i]
            flag = False
        else:
            if mayor_numero < lista[i]:
                mayor_numero = lista[i]
    return mayor_numero

#   RETORNAR FLOAT-------------------------------------------------------------------------------------------------------
def retornar_pedido_decimal(mensaje:str)->float:
    decimal = float(input(mensaje))
    return decimal
def retornar_pedido_decimal_con_parametros(mensaje:str, desde:float, hasta:float)->float:
    numero = float(input(mensaje))
    while numero < desde or numero > hasta:
        numero = float(input("error, " + mensaje))
    return numero

def retornar_promedio_de_lista(lista:list)->float:
    acumulador = 0
    contador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
        contador += 1
    promedio = (acumulador /contador)
    return promedio



