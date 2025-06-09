#Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
contador1 = 0
contador2 = 0
while contador1 < 10:
    contador1 += 1
    contador2 = 0
    while contador2 < 10:
        contador2 += 1
        print(contador2)
#Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
contador1 = 10
contador2 = 10
while contador1 > 0:
    contador2 = 10
    contador1 -= 1
    while contador2 > 0:
        print(contador2)
        contador2 -= 1
contador1 -= 1

#Mostrar la suma de los números desde el 1 hasta el 10.
acumulador = 0
contador = 0
while contador < 10:
    contador += 1
    acumulador = acumulador + contador
print(acumulador)
#
acumulador = 0
contador = 0
pares = 0
while contador < 10:
    contador +=1
    pares = contador
    if contador % 2 == 0:
        acumulador = contador + acumulador
print(acumulador)

"""
Solicitar el ingreso de 5 números, calcular la suma de los números ingresados
y el promedio. Mostrar la suma y el promedio por pantalla
"""
acumulador = 0
contador = 0
while contador < 5:
    numero = int(input("Di un numero: "))
    acumulador = acumulador + numero
    contador += 1
promedio = acumulador / 5
print(acumulador)
print(promedio)

"""
Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
Calcular la suma de los números ingresados y el promedio de los mismos.
"""
flag = True
acumulador = 0
contador = 0
while flag == True:
    numero = int(input("Dime un numero: "))
    acumulador = acumulador + numero
    contador += 1
    continuar = input("quieres continuar?(si/no): ")
    if continuar == "no":
        flag = False
promedio = acumulador / contador
print(acumulador)
print(promedio)
