from Modulo_juego import *
from datos import *

nombre_usuario = pedir_dato("Cual es tu nombre? ")
indice_usuario = PUNTO_DE_PARTIDA
seguir_jugando = analizar_dato()

while seguir_jugando == "si":
    pregunta_y_opciones = manejar_pregunta(preguntas)
    imprimir_valores(pregunta_y_opciones)
    respuesta_usuario = pedir_dato_para_pregunta("Que opcion eliges?(a/b/c): ")
    acerto = verificar_respuesta( pregunta_y_opciones, respuesta_usuario, CLAVE_OPCION_CORRECTA)
    indice_usuario = jugar_turno(indice_usuario, TABLERO, acerto)
    fin_juego = verificar_fin_juego(indice_usuario, TABLERO, preguntas)
    print("Quedaste en el casillero:", indice_usuario)
    if fin_juego:
        seguir_jugando = "no"
    else:
        seguir_jugando = analizar_dato()

    if seguir_jugando == "no":
        guardar_score(nombre_usuario,indice_usuario)

print("Fin del programa")
