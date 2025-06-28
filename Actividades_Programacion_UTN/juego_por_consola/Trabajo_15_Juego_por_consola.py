from Modulo_juego import *
from copy import deepcopy
from Datos_juego_por_consola import *

nombre_usuario = pedir_dato(MENSAJE_PEDIR_NOMBRE)
indice_usuario = PUNTO_DE_PARTIDA

respuesta = pedir_dato("Quiere jugar ?(si/no): ")
respuesta = validar_string(respuesta,"si","no")
seguir_jugando = verificar_palabra(respuesta, "si")

copia_preguntas = deepcopy(preguntas)
while seguir_jugando:

    pregunta_y_opciones = buscar_valor(copia_preguntas)
    imprimir_valores(pregunta_y_opciones,ENCABEZADO_PREGUNTA, CLAVE_RESPUESTA_CORRECTA)
    eliminar_un_valor(copia_preguntas, pregunta_y_opciones)
    
    respuesta_usuario = pedir_dato(MENSAJE_PEDIR_OPCION)
    acerto = verificar_respuesta( pregunta_y_opciones, respuesta_usuario, CLAVE_RESPUESTA_CORRECTA)

    indice_usuario = mover_usuario(indice_usuario , acerto, MOVERSE_RESPUESTA_CORRECTA, MOVERSE_RESPUESTA_INCORRECTA)

    casillero_vacio = verificar_casillero_vacio(TABLERO,indice_usuario)
    if casillero_vacio == False:

        movimiento_adicional = buscar_movimiento_adicional(TABLERO,indice_usuario)
        indice_usuario = mover_adicional_usuario(indice_usuario,acerto,movimiento_adicional)

    imprimir_segun_booleano(acerto,MENSAJE_CORRECTO , MENSAJE_INCORRECTO)

    perdio = verificar_perdedor(indice_usuario)
    gano = verificar_ganador(TABLERO,indice_usuario)
    preguntas_agotadas = verificar_lista_vacia(copia_preguntas)
    seguir_jugando = verificar_booleanos_iguales(perdio,gano,preguntas_agotadas)

    print(MENSAJE_INFORMAR_CASILLERO, (indice_usuario))

    if seguir_jugando:
        respuesta = pedir_dato("Quiere jugar ?(si/no): ")
        respuesta = validar_string(respuesta,"si","no")
        seguir_jugando = verificar_palabra(respuesta, "si")

    if seguir_jugando == False:
        anexar_score(nombre_usuario, indice_usuario)
        print(MENSAJE_INFORMAR_CASILLERO, (indice_usuario))

print(MENSJAE_FIN_PROGRAMA)
