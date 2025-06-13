#   EJERCICIO 1


def sumar_naturales(numero:int)->int:
    if numero == 0:
        return numero
    else:
        return numero + sumar_naturales(numero - 1)

print(sumar_naturales(3))


#   EJERCICIO 2


def calcular_potencia(numero:int, exponente:int)->int:
    if exponente == 1:
        return numero
    else:
        return numero * calcular_potencia(numero, exponente - 1)
    
print(calcular_potencia(5,3))


#  EJERCICIO  3



def suma_digitos(numero:int)->int:
    if numero < 10:
        return numero
    else:
        return (numero % 10) + suma_digitos(numero//10) 
print(suma_digitos(123)) 


#   EJERCICIO 4

f_0 = 0
f_1 = 1
def calcular_fibonacci(numero:int)->int:
    if numero == 0:
        return numero
    elif numero == 1:
        return numero
    else:
        return  (calcular_fibonacci(numero - 1)) +(calcular_fibonacci(numero - 2))
    
num = int(input("dime un numero: "))
print(calcular_fibonacci(num))
