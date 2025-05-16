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