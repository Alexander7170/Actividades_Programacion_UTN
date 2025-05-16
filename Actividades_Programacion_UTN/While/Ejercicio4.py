acumulador = 0
contador = 0
pares = 0
while contador < 10:
    contador +=1
    pares = contador
    if contador % 2 == 0:
        acumulador = contador + acumulador
print(acumulador)
