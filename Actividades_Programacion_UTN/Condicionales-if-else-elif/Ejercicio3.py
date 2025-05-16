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