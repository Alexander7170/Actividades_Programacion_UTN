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
