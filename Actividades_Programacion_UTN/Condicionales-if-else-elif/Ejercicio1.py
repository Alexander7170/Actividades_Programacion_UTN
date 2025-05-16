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