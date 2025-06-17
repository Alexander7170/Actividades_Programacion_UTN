"""
Contadores - Acumuladores - Máximos y mínimos

1)   Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
2)  Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
3)  Mostrar la suma de los números desde el 1 hasta el 10.
4)  Mostrar la suma de los números pares desde el 1 hasta el 10.
5)  Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. 
    Mostrar la suma y el promedio por pantalla.

6)  Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
    Calcular la suma de los números ingresados y el promedio de los mismos.

7)  Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
    Calcular la suma de los números positivos y el producto de los negativos.

8)  Ingresar 10 números enteros. Determinar el máximo y el mínimo.

9)  Solicitar al usuario que ingrese como mínimo 5 números. 
    Calcular la suma de los números ingresados y el promedio de los mismos.

10) Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10.
     Calcular la suma de los números ingresados y el promedio de los mismos.

"""
# #   1)
# contador1 = 0
# contador2 = 0
# while contador1 < 10:
#     contador1 += 1
#     contador2 = 0
#     while contador2 < 10:
#         contador2 += 1
#         print(contador2)
# #   2)
# contador1 = 10
# contador2 = 10
# while contador1 > 0:
#     contador2 = 10
#     contador1 -= 1
#     while contador2 > 0:
#         print(contador2)
#         contador2 -= 1
# contador1 -= 1

# #   3)

# acumulador = 0
# contador = 0
# while contador < 10:
#     contador += 1
#     acumulador = acumulador + contador
# print(acumulador)

# #   4)

# acumulador = 0
# contador = 0
# pares = 0
# while contador < 10:
#     contador +=1
#     pares = contador
#     if contador % 2 == 0:
#         acumulador = contador + acumulador
# print(acumulador)

# #   5)

# acumulador = 0
# contador = 0
# while contador < 5:
#     numero = int(input("Di un numero,,: "))
#     acumulador = acumulador + numero
#     contador += 1
# promedio = acumulador / 5
# print(acumulador)
# print(promedio)

# #   6)

# flag = True
# acumulador = 0
# contador = 0
# while flag == True:
#     numero = int(input("Dime un numero: "))
#     acumulador = acumulador + numero
#     contador += 1
#     continuar = input("quieres continuar?(si/no): ")
#     if continuar == "no":
#         flag = False
# promedio = acumulador / contador
# print(acumulador)
# print(promedio)

#   7)
# continuar = "si"
# suma_positivos = 0
# producto_negativos = 1
# while continuar == "si":
#     numero = int(input("Di un numero"))
#     if numero >= 0:
#         suma_positivos += numero
#     else:
#         producto_negativos *= numero
    
#     continuar = input("Quieres continuar: ?")
#     while continuar != "si" and continuar != "no":
#         continuar = input("Error, si si o no: ")

#   8)

# contador = 0
# flag_1 = True
# while contador < 5:
#     numero = int(input("Di un numero: "))
#     if flag_1:
#         numero_mayor = numero
#         numero_menor = numero
#         flag_1 = False
#     else:
#         if numero_mayor < numero:
#             numero_mayor = numero
#         if numero_menor > numero:
#             numero_menor = numero
#     contador += 1
# print(numero_mayor, numero_menor)