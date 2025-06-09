#Ejercicio 1

# contador = 0
# for i in range(10):
#     contador += 1
#     print(contador)

# #Ejercicio 2
# for i in range(10,0,-1):
#     print(i)

#Ejercicio 3

# contador = 0
# rango = int(input("Di un numero: "))
# for i in range(rango):
#     contador += 1
#     print (contador)

#Ejercicio 4

# contador = 0
# numero = int(input("Di un numero: "))
# for i in range(10):
#     contador += 1
#     resultado = numero * contador
#     print(f"{numero} x {contador} = {resultado}")

#Ejercicio 5

# acumulador = 0
# promedio = 0
# for i in range(10):
#     numero = int(input("di un numero: "))
#     acumulador += numero
#     promedio += 1
#     if numero == 0:
#         break
# print(f"la suma de todos los numeros es {acumulador} con un promedio de {acumulador/promedio}")

#Ejercicio 6

#contador = 0
# divisor = 0
# for i in range(10
#                ):
#     contador += 1
#     divisor = contador % 3
#     if divisor == 0:
#         print(contador)

#Ejercicio 7

# contador = 0
# pares = 0
# for i in range(50):
#     contador += 1
#     pares = contador % 2
#     if pares == 0:
#         print(contador)

#Ejercicio 8

#numero = int(input("ingrese un numero: "))
# piramide = ""
# for i in range (numero):
#     piramide += str(i+1)
#     print(piramide)

#Ejercicio 9

#numero = int(input("di un numero: "))
# for i in range(numero):
#     i += 1
#     if numero % i == 0:
#         print(i)

#Ejercicio 10

# contador = 0
# numero = int(input("Di un numero: "))
# for i in range(numero):
#     i += 1
#     if numero % i == 0:
#         contador += 1
#         if contador == 2 and i == numero:
#             print("es numero primo")

#Ejercicio 11

# numero = int(input("Di un numero: "))
# for i in range(numero):
#     contador = 0
#     i += 1
#     for j in range(i):
#         if i % j == 0:
#             contador += 1
#             if contador == 2 and j == i:
#                 print(j) 
#                 contador = 0

def imprimir(num:int):
    for i in range(1,num):
        print(i)
imprimir(5)