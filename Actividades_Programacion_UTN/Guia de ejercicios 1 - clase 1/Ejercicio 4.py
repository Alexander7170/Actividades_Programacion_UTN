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
