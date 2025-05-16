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