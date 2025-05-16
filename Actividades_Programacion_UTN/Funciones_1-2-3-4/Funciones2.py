#   EJERCICIO 1


# def calcular_area_rectangunlo(ancho:int, altura:int)->int:
#     area = ancho * altura
#     return area
# var_ancho = int(input("dime el ancho del rectangulo: "))
# var_largo = int(input("dime el largo del rectangulo: "))
# print(f"el area es de {calcular_area_rectangunlo(var_ancho,var_largo)}m²")


#   EJERCICIO 2


# import math

# def calcular_area_circulo(radio:float)->float:
#     area = radio**2 * math.pi
#     return area

# var_radio = float(input("Dime el radio del circulo: "))
# print(f"El area del circulo es {calcular_area_circulo(var_radio)}m²")


#   EJERCICIO 3


# def verificar_par():
#     mensaje = "es un numero par"
#     if numero % 2 != 0:
#         mensaje = "es un numero impar"
#     return mensaje
# numero = int(input("dime un numero: "))
# print(verificar_par())


#   EJERCICIO 4


# def verificar_par()->bool:
#     flag = True
#     if numero % 2 != 0:
#         flag = False
#     return flag
# numero = int(input("dime un numero: "))


#   EJERCICIO 5


# def encontrar_numero_mayor(numero1:int, numero2:int, numero3)->int:
#     numero_mayor = numero1
#     if numero_mayor < numero2:
#         numero_mayor = numero2
#     if numero_mayor < numero3:
#         numero_mayor = numero3
#     return numero_mayor


#   EJERCICIO 6


# def calcular_potencia(base:int, exponente:int)->int:
#     resultado = base ** exponente
#     return resultado


#   EJERCICIO 7


# def verificar_n_primo(numero:int)->bool:
#     flag = True
#     for i in range(2,numero): #Empieza desde 2 hasta el parametro numero sin incluirse asi mismo
#         if numero % i == 0:   #verifica si el resto de cada valor que va tomando i dividido por la variable numero da 0, un divisor
#             flag = False
#             break
#     return flag
# print(verificar_n_primo(7))#ejemplo pongo el 7


#   EJERCICIO 8


# def mostrar_n_primos(numero_1:int, numero_2:int)->int:
#     contador = 0
#     for i in range(numero_1, numero_2+1): #defino parametros el cual i recorrera
#         contador_divisor = 0
#         for j in range(1,i+1): # verificara si tiene un divisor mas aparte del 1 y del si mismo
#             if i % j == 0:
#                 contador_divisor += 1
#                 if contador_divisor == 2 and j == i: # imprimira solo si tiene dos divisores y j recorra i
#                     print(i)
#                     contador += 1
#     return contador
# num1 = int(input("Dime un numero: "))
# num2 = int(input("Dime un numero "))
# print(f"hay en total: {mostrar_n_primos(num1,num2)} numeros primos")


#   EJERCICIO 9


# def imprimir_tabla_de_multiplicar(numero, inicio:int, fin:int):
#     for i in range(inicio, fin+1):
#         resultado = i * numero
#         print(f"{i} x {numero} = {resultado}")

# var_num = int(input("Dime un numero: "))
# imprimir_tabla_de_multiplicar(var_num, 1, 10)


#   EJERCICIO 10


# def ingresar_entero()->int:
#     numero = int(input("dime un numero entero: "))
#     return numero


#   EJERCICIO 11

# def ingresar_flotante()->float:
#     numero = float(input("Dime un numero flotante: "))
#     return numero


#   EJERCICIO 12


# def ingresar_cadena()->str:
#     palabra = input("Ingresa una cadena de texto: ")
#     return palabra


#   EJERCICIO 13
# No entendi que habia que hacer