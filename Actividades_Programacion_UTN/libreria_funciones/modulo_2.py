def pedir_numero_con_parmaetros(mensaje:str,minimo:int, maximo:int)->int:
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        numero = int(input("error ",mensaje))
    return numero
def verificar_tesoro(mapa: list, x: int, y: int) -> int:
    distancia = 0
    if mapa[x][y] == 0:
        ecuacion_1 = (x - 1)
        ecuacion_2 = (x - 3)
        if ecuacion_1 < 0:
            ecuacion_1 *= -1
        if ecuacion_2 < 0:
            ecuacion_2 *= -1
        distancia = ecuacion_1 + ecuacion_2
    return distancia

def lista_misma_columna(matriz:list)->list:
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i < len(matriz)-2:
                if matriz[i+2][j] == matriz[i][j] == matriz[i+1][j]:
                    lista.append(matriz[i][j])
    return lista