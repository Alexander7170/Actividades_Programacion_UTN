def retornar_pedido_decimal(mensaje:str)->float:
    decimal = float(input(mensaje))
    return decimal

def retornar_pedido_decimal_con_parametros(mensaje:str, desde:float, hasta:float)->float:
    numero = float(input(mensaje))
    while numero < desde or numero > hasta:
        numero = float(input("error, " + mensaje))
    return numero

def pedir_entero(mensaje:str)->int:
    entero = int(input(mensaje))
    return entero

def pedir_entero_con_parametros(mensaje:str, desde:int, hasta:int)->int:
    numero = int(input(mensaje))
    while numero < desde or numero > hasta:
        numero = int(input("error, " + mensaje))
    return numero

def pedir_string(mensaje:str)->str:
    cadena_caracteres = input(mensaje)
    return cadena_caracteres

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
