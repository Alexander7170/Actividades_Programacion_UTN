"""
Crear un programa en Python que:
Construya una matriz de 4 filas x 4 columnas con números fijos (predefinida).
Utilice una función que recorra las columnas de la matriz y
verifique si existe un número repetido 3 veces de manera vertical (una debajo de otra).
Si lo encuentra, la función debe retornar ese número.
Si no existe, debe retornar None.
# MATRIZ FIJA
matriz = [
    [5, 0, 3, 4],
    [5, 2, 7, 8],
    [2, 2, 3, 1],
    [1, 6, 7, 4]
]
"""
matriz = [[5, 0, 3, 0],
          [5, 2, 7, 4],
          [2, 2, 3, 4],
          [1, 6, 7, 4]]

def recorrer(matrix:list)->int:
    for i in range(3):
        for j in range(3):
            numero = matrix[i][j]
            if numero == matrix[1][i] and numero == matrix[2][i]:
                print(numero)
recorrer(matriz)