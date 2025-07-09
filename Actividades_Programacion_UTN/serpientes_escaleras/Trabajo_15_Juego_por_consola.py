from Modulo_juego import *
from datos import *

nombre_usuario = pedir_dato(MENSAJE_PEDIR_NOMBRE)
indice_usuario = PUNTO_DE_PARTIDA
respuesta = pedir_dato("Quiere jugar ?(si/no): ")
respuesta = validar_string(respuesta,"si","no")
seguir_jugando = verificar_palabra(respuesta, "si")

while seguir_jugando:
    pregunta_y_opciones = manejar_pregunta(preguntas)
    imprimir_valores(pregunta_y_opciones, CLAVE_RESPUESTA_CORRECTA)
    respuesta_usuario = pedir_dato("Que opcion eliges?(a/b/c): ")
    acerto = verificar_respuesta( pregunta_y_opciones, respuesta_usuario, CLAVE_RESPUESTA_CORRECTA)
    indice_usuario = mover_usuario(indice_usuario, TABLERO, acerto, MOVERSE_RESPUESTA_CORRECTA, MOVERSE_RESPUESTA_INCORRECTA)
    print(MENSAJE_INFORMAR_CASILLERO, indice_usuario)
    fin_juego = verificar_fin_juego(indice_usuario,TABLERO,preguntas)
    if fin_juego:
        seguir_jugando = False
    if seguir_jugando:
        respuesta = pedir_dato("Quiere jugar ?(si/no): ")
        respuesta = validar_string(respuesta,"si","no")
        seguir_jugando = verificar_palabra(respuesta, "si")

    if seguir_jugando == False or fin_juego == True:
        guardar_score(nombre_usuario,indice_usuario)

print(MENSAJE_FIN_PROGRAMA)
