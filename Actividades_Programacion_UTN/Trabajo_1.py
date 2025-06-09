#Ejercicio 1
"""
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.Ejercicio 1:
"""
nombre1 = input("dime tu nombre: ")
sueldo1 = float(input("dime tu sueldo actual: "))
print(f"el sueldo de {nombre1} con un aumento de {sueldo1 * 0.10} pesos")

#ejercicio 2
"""
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).
"""
edad2 = int(input("dime tu edad: "))
if edad2 < 13:
    print("Eres niño")
elif edad2 < 18:
    print("Eres adolecente")
else:
    print("Eres adulto")

#Ejercicio 3
""""
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.
"""
contador_numero_pares = 0
contador_numero_inpares = 0
acumulador_numero_positivos = 0
menor_numero = 0
producto_Negativo = 1
par_mayor = 0
flag = True
flag_par_mayor = True
contador = 0
for i in range(5):
    numero = int(input("dime un numero: "))

    if numero == 0:
        print("error, diga culquier numero menos el 0")
    else:                 #cantidad de pares
        if numero % 2 == 0:
            contador_numero_pares += 1
            if flag_par_mayor == True:
                par_mayor = numero
                flag_par_mayor = False
            else:
                if par_mayor < numero:
                    par_mayor = numero
        else:
            contador_numero_inpares +=1
        #menor numero
        if flag == True:
            menor_numero = numero
            flag = False
        else:
            if numero < menor_numero:
                menor_numero = numero
        

        if numero > 0:
            acumulador_numero_positivos += numero
            contador = contador + 1
            if contador == 5:
                producto_Negativo = 0
        else:
            producto_Negativo = producto_Negativo * numero

    
print(""
"")
print(f"los numeros pares son {contador_numero_pares}")
print(f"los numeros impares son {contador_numero_inpares}")
print(f"El menor numero es {menor_numero}")
print(f"De los pares el mayor numero ingresado es {par_mayor}")
print(f"la suma de los numeros positivo es {acumulador_numero_positivos}")
print(f"la multiplicacion de los negativos es {producto_Negativo}")

#Ejercicio 4
"""
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.'
"""
edad = int(input("Dime tu edad: "))
estado_civil = input("Dime tu estado civil: ")
if edad < 18 and estado_civil != "soltero":
    print("es muy pequeño para no estar soltero")


#Ejercicio 5
"""
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:

-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%

-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%

-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.

Validar el ingreso de datos
"""
Flag = True
base_estadia = 15000
while Flag == True:
    estacion = input("Dime una estacion del año (verano/otoño/primavera/invierno): ")
    if estacion == "verano" or estacion == "otoño" or estacion == "primavera" or estacion == "invierno":
        break
    else:
        print("dato incorrecto")
while Flag == True:
    localidad = input("Dime la localidad (bariloche/cataratas/mar del plata/cordoba): ")
    if localidad == "bariloche" or localidad == "cataratas" or localidad == "mar del plata" or localidad == "cordoba":
        break
    else:
        print("opcion invalida")

if estacion == "invierno":
    if localidad == "bariloche":
        base_estadia = base_estadia + base_estadia * 0.20
    elif localidad == "cordoba" or localidad == "cataratas":
        base_estadia = base_estadia - base_estadia * 0.10
    else:
        base_estadia = base_estadia - base_estadia * 0.20
elif estacion == "verano":
    if localidad == "bariloche":
        base_estadia = base_estadia - base_estadia * 0.20
    elif localidad == "cordoba" or localidad == "cataratas":
        base_estadia = base_estadia + base_estadia * 0.10
    else:
        base_estadia = base_estadia + base_estadia * 0.20
else:
    if localidad == "bariloche":
        base_estadia = base_estadia + base_estadia * 0.10
    elif localidad == "cataratas":
        base_estadia = base_estadia + base_estadia * 0.10
    elif localidad == "mar del plata":
        base_estadia = base_estadia + base_estadia * 0.10
    else:
        base_estadia = base_estadia

print(f"el precio final que dependia de la localidad y la estacion es de ${base_estadia}")
