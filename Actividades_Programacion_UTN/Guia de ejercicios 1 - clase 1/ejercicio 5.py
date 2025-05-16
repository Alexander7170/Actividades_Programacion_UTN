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
