#   Ejercicio 1 
from copy import deepcopy
"""
Se tiene una lista de diccionarios, donde cada diccionario representa un
producto con nombre, precio y categoría. Escribe una función procesar_productos
que reciba esta lista y una función de operación. Luego, crear distintas funciones
para:
Filtrar productos de una categoría dada.
Calcular el precio promedio de todos los productos.

"""
productos = [
 {"nombre": "Laptop", "precio": 1200, "categoria": "tecnología"},
 {"nombre": "Silla", "precio": 150, "categoria": "hogar"},
 {"nombre": "Smartphone", "precio": 800, "categoria": "tecnología"},
 {"nombre": "Mesa", "precio": 300, "categoria": "hogar"},
 {"nombre": "Auriculares", "precio": 200, "categoria": "tecnología"}]

def filtrar_lista(lista_de_diccionarios:list)->list:
    key = "categoria"
    valor = "tecnología"
    lista_nueva = []
    for diccionario in lista_de_diccionarios:
        if diccionario[key] == valor:
            lista_nueva.append(diccionario)
    return lista_nueva

def procesar_productos(lista_de_diccionarios:list,  operacion:callable )->any:
    retorno = operacion(lista_de_diccionarios)
    return retorno

def calcular_promedio(lista_de_diccionarios:list)->int:
    key = "precio"
    acumulador = 0
    for diccionario in lista_de_diccionarios:
        acumulador += diccionario[key]
    return acumulador / len(lista_de_diccionarios)

lista_filtrada = procesar_productos(productos,filtrar_lista)
promedio_precios = procesar_productos(productos,calcular_promedio)

#   Ejercicio 2

"""
Se tiene una lista de diccionarios donde cada diccionario representa un
estudiante con su nombre, curso y calificación. Escribe una función
procesar_estudiantes que reciba esa lista y una función como parámetro. Luego,
implementa:
Una función que devuelva solo los estudiantes aprobados (nota mayor o igual a
60).
Otra que calcule el promedio de calificaciones de todos los estudiantes.
"""
estudiantes = [
{"nombre": "Sofía", "curso": "Matemáticas", "calificacion": 7.5},
{"nombre": "Tomás", "curso": "Historia", "calificacion": 5.5},
{"nombre": "Valentina", "curso": "Ciencias", "calificacion": 9.0},
{"nombre": "Lucas", "curso": "Literatura", "calificacion": 4.0},
{"nombre": "Martina", "curso": "Física", "calificacion": 6.8} ]

def procesar_estudiantes (lista_dic: list, funcion:callable)->any:
    if funcion == calcular_promedio:
        calcular_promedio(lista_dic,)