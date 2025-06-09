"""
A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá 
determinar la posición del jugadoren la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot
"""
altura = int(input("Dime tu altura en centimetros y te dire en que posicion estaras: "))
if altura < 160:
    print("Tu posicion en la cancha sera Base")
elif altura < 180:
    print("Tu posicion en la cnahca sera la de Escolta")
elif altura < 200:
    print("Tu posicion en la cancha sera la de Alero")
else:
    print("Tu posicion en la cnacha sera la de Ala-Pivot o Pívot")

"""
Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota es ...

"""
from random import*
numero_random = randint (0, 10)
if numero_random < 4:
    print(f"Desaprobado, tu nota fue {numero_random}")
elif numero_random < 6:
    print(f"Aprobado, tu nota fue {numero_random}")
else:
    print(f"Promocion directa, tu nota fue {numero_random}")

"""
Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
Si es invierno: solo se viaja a Bariloche.
Si es verano: se viaja a Mar del plata y Cataratas.
Si es otoño: se viaja a todos los lugares.
Si es primavera: se viaja a todos los lugares menos Bariloche.
"""
estacion = input("dime la estacion del año en la que quiere viajar: ")
match estacion:
    case "invierno":
        print("solo se viaja a bariloche")
    case "verano":
        print("solo se viaja a mar del plata y cataratas")
    case "otoño":
        print("se viaja a todos los lugares")
    case _ :
        print("Se viaja a todos los lugares menor bariloche")