#EJERCICIO 1

# def mostrar_numero(numero):
#     print("el numero es: ", numero)
# mostrar_numero()

#EJERCICIO 2

# def registrar_numero()->int:
#     numero = int(input("diga un numero: "))
#     return numero
# registrar_numero()

#EJERCICIO 3

# def determinar_par()->bool: 
#                #determina si es par o no, devolviendo un valor booleable
#     determinar = True
#     if numero % 2 != 0:
#         determinar = False
#     return determinar

# numero = int(input("Di un numero: "))
# if determinar_par():
#     print("es par")
# else:
#     print("es impar")

#EJERCICIO 4

#3.1
# def determinar_parametros(desde:int, numero:int, hasta:int) ->bool:
#     #funcion que valida si el numero ingresado esta dentro de los parametros
#     validacion = True
#     if numero < desde or numero > hasta:
#         validacion = False
#     return validacion
# def mostrar_numero(numero):
#     print(numero)
# numero = int(input("di un numero: "))
# if determinar_parametros(0,numero,100): #pongo como prueba "Desde" = 0 "Hasta" = 100
#     mostrar_numero(numero)

# #3.2
# def determinar_parametros_2(desde:int, numero_2:int, hasta:int)->int:
#     #Funcion que retornara el numero que diga el usuario segun los parametros indicados anteriormente
#     numero_2 = int(input("dime un numero: "))
#     if numero_2 > desde and numero_2 < hasta:
#         return numero_2
# determinar_parametros_2(0,numero,100) #pongo como ejemplo "Hasta" = 0  "Desde" = 100

#EJERCICIO 5

# def restar_1(num_1:int, num_2:int)->int:
#     resultado_1= num_1 - num_2
#     return resultado_1
# numero_1 = int(input("Dime un numero: "))
# numero_2 = int(input("Dime otro numero: "))
# print(f"{numero_1} - {numero_2} = {restar_1(numero_1, numero_2)}")

# def restar_2()->int:
#     resultado_2 = numero_11 - numero_22
#     return resultado_2
# numero_11 = int(input("Dime un numero: "))
# numero_22 = int(input("Dime otro numero: "))
# print(f"{numero_11} - {numero_22} = {restar_2()}")

# def restar3(num_111:int, num_222:int):
#     resultado_3 = num_111 - num_222
#     print(f"{numero_111} - {numero_222} = {resultado_3}")
# numero_111 = int(input("Dime un numero: "))
# numero_222 = int(input("Dime otro numero: "))
# restar3(numero_111, numero_222)

# def restar4():
#     resultado_4 = numero_1111 - numero_2222
#     print(f"{numero_1111} - {numero_2222} = {resultado_4}")
# numero_1111 = int(input("Dime un numero: "))
# numero_2222 = int(input("Dime otro numero: "))
# restar4()

#EJERCICIO 6

variable1 = int(input("Dime un numero entre el 10 y el 100: "))
def validar_numero(desde:int, numero:int, hasta:int)->bool:
    flag = False
    if numero >= desde and numero <= hasta:
        flag = True
    return flag
def realizar_descuento(num:int)->int:
    descuento = num -( num /100 * 5)
    return descuento
validar_numero(10,variable1,100)
while validar_numero(10,variable1,100) == False:
    variable1 = int(input("Error, dime un numero entre el 10 y el 100: "))
    validar_numero(10,variable1,100)

# print(f"el 5% de {variable1} es {realizar_descuento(variable1)}")

#EJERCICIO 7

# def restar_numeros(num1, num2,)->int:
#     resultado = num1 - num2
#     return resultado
# def sumar_numeros(num1, num2)->int:
#     resultado = num1 + num2
#     return resultado

# numero1 = int(input("Dime un numero entre el 10 y el 100: "))
# while numero1 < 10 or numero1 > 100:
#     numero1 = int(input("Error, dime un numero entre el 10 y el 100: "))

# numero2 = int(input("Dime el segundo numero entre el 10 y el 100: "))
# while numero2 < 10 or numero2 > 100:
#     numero2 = int(input("Error, dime un numero entre el 10 y el 100: "))

# operacion = input("Diga una operacion de sumar o restar (s/r): ")
# while operacion != "s" and operacion != "r":
#     operacion = input("Error, diga una operacion de restar o sumar (s/r): ")

# if operacion == "s":
#     print(sumar_numeros(numero1, numero2))
# else:
#     print(restar_numeros(numero1, numero2))
