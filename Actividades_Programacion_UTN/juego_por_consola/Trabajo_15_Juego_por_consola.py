from Modulo_juego import *
from datos_consola import *

nombre_usuario = pedir_dato(MENSAJE_PEDIR_NOMBRE)
indice_usuario = PUNTO_DE_PARTIDA
respuesta = pedir_dato("Quiere jugar ?(si/no): ")
respuesta = validar_string(respuesta,"si","no")
seguir_jugando = verificar_palabra(respuesta, "si")

while seguir_jugando:
    pregunta_y_opciones = buscar_pregunta(preguntas)
    imprimir_valores(pregunta_y_opciones, CLAVE_RESPUESTA_CORRECTA)
    eliminar_una_pregunta(preguntas, pregunta_y_opciones)

    respuesta_usuario = pedir_dato("Que opcion eliges?(a/b/c): ")
    acerto = verificar_respuesta( pregunta_y_opciones, respuesta_usuario, CLAVE_RESPUESTA_CORRECTA)

    indice_usuario = mover_usuario(indice_usuario , acerto, MOVERSE_RESPUESTA_CORRECTA, MOVERSE_RESPUESTA_INCORRECTA)
    movimiento_adicional = buscar_movimiento_adicional(TABLERO,indice_usuario)
    indice_usuario = mover_adicional_usuario(indice_usuario,acerto,movimiento_adicional)

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
