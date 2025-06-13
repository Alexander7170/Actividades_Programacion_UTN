def buscar_promedios_en_listas_anidadas(lista:list)->list:
    promedios = []
    acumulador = 0
    contador = 0
    for elemento in lista:
        for i in range(len(elemento)):
            acumulador += elemento[i]
            contador += 1
        promedio = acumulador/contador
        promedios.append(promedio)
    return promedios