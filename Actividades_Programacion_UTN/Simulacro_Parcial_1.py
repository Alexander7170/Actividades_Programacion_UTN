mapa = [[0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0] ]

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

seguir_jugando = True
while seguir_jugando:
    coordenada_x = pedir_numero_con_parmaetros("Dime la coordenada x entre el 0 y el 4: ",0,4)
    coordenada_y = pedir_numero_con_parmaetros("Dime la coordenada y entre el 0 y el 4: ",0,4)

    numero_retornado = verificar_tesoro(mapa,coordenada_x,coordenada_y)
    if numero_retornado == 0:
        print("Felicidades escontraste el tesoro")
        seguir_jugando = False
    else:
        print("fallaste, el tesosro esta a ", numero_retornado)
        pregunta = input("Quiere seguir jugando?: ")
        if pregunta == "no":
            seguir_jugando  = False
        elif pregunta != "si":
            while pregunta != "si":
                pregunta = "di si o no "

