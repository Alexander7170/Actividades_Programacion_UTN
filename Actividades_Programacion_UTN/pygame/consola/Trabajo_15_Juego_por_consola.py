from Modulo_juego import *
from datos import *

nombre_usuario = pedir_dato("Cual es tu nombre? ")
indice_usuario = PUNTO_DE_PARTIDA
seguir_jugando = analizar_dato(pedir_dato,validar_string,verificar_palabra)

while seguir_jugando:
    pregunta_y_opciones = manejar_pregunta(preguntas)
    imprimir_valores(pregunta_y_opciones)
    respuesta_usuario = pedir_dato("Que opcion eliges?(a/b/c): ")
    acerto = verificar_respuesta( pregunta_y_opciones, respuesta_usuario, CLAVE_OPCION_CORRECTA)
    indice_usuario, fin_juego = jugar_turno(indice_usuario, TABLERO, acerto, preguntas)
    print(MENSAJE_INFORMAR_CASILLERO, indice_usuario)
    if fin_juego:
        seguir_jugando = False
    else:
        seguir_jugando = analizar_dato(pedir_dato,validar_string,verificar_palabra)

    if seguir_jugando == False:
        guardar_score(nombre_usuario,indice_usuario)

print(MENSAJE_FIN_PROGRAMA)
