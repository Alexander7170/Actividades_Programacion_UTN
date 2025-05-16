contador1 = 0
contador2 = 0
mayor_edad = 0
flag = True
tecnologia_mayor = ""
nombre_mayor = ""
empleados_encuestados = 10
for i in range(empleados_encuestados):
    nombre = input("di tu nombre: ").lower
    edad = int(input("di tu edad: "))
    while edad < 18:
        edad = int(input("di tu edad de nuevo, tienes que ser mayor de edad: "))
    genero = input("di tu genero (m/f/otro): ").lower
    tecnologia = input("vota por una tecnologia (ia, rv, iot): ").lower

    if edad >= 25 and edad <= 50 and genero == "m"  and (tecnologia == "iot" or tecnologia == "ia"):
        contador1 += 1
    if edad >= 33 and edad <= 40 and genero != "f" and tecnologia != "ia":
        contador2 += 1
    if genero == "m":
        if flag == True:
            mayor_edad = edad
            nombre_mayor = nombre
            tecnologia_mayor = tecnologia
            flag = False
        else:
            if mayor_edad < edad:
                mayor_edad = edad
                nombre_mayor = nombre
                tecnologia_mayor = tecnologia
promedio = contador2 / empleados_encuestados * 100

print(f"Cantidad de empleados masculinos que hayan votado a IA o IOt y tengan entre 25 y 50 años: {contador1}")
print(f"porcentaje de empleados no femeninos que no hayan votado a IA y que tengan entre 33 y 40 años: %{promedio}")
print(f"su nombre es {nombre_mayor} y voto a {tecnologia_mayor}")