from Modulo_juego import *
from copy import deepcopy
from Datos_juego_por_consola import *
# CREAR FUNCION QUE VALIDE LA TABLA

nombre_usuario = pedir_string("Holaa, como te llamas?: ")
indice_usuario = PUNTO_DE_PARTIDA
copia_tablero = deepcopy(tablero)
jugar = pedir_string(" Quiere jugar ?(si/no): ")
jugar = validar_string(jugar,"si","no")
tablero_transformado = False
usuario_ubicado = False
while jugar == "si":
        if tablero_transformado == False:
            transformar_tablero(copia_tablero, PUNTO_DE_PARTIDA)
            tablero_transformado = True
        if usuario_ubicado == False:
            ubicar_usuario(copia_tablero,PUNTO_DE_PARTIDA, nombre_usuario)
            usuario_ubicado = True

        imprimir_tablero(copia_tablero)
        dic_pregunta_opciones = buscar_dic_random(preguntas)
        eliminar_un_dict(preguntas, dic_pregunta_opciones)
        imprimir_pregunta_opciones( dic_pregunta_opciones,"respuesta_correcta")

        respuesta_usuario = pedir_string("Respuesta:  ")
        respuesta_correcta = verificar_respuesta( dic_pregunta_opciones, respuesta_usuario, "respuesta_correcta")

        if respuesta_correcta:

            print("Correcto")
            casillero_vacio = verificar_indice_vacio_en_un_movimiento(copia_tablero, indice_usuario, MOVERSE_RESPUESTA_CORRECTA)
            if casillero_vacio:
                intercambiar_valor_en_un_movimiento(copia_tablero, indice_usuario, MOVERSE_RESPUESTA_CORRECTA)
            else:
                avances_extras = numero_movimientos_extras(copia_tablero,indice_usuario + MOVERSE_RESPUESTA_CORRECTA)
                avances_totales = avances_extras + MOVERSE_RESPUESTA_CORRECTA
                intercambiar_valor_en_un_movimiento(copia_tablero, indice_usuario, avances_totales)

        else:
            print("Incorrecto")
            casillero_vacio = verificar_indice_vacio_en_un_movimiento(copia_tablero, indice_usuario, MOVERSE_RESPUESTA_INCORRECTA)
            if casillero_vacio:
                intercambiar_valor_en_un_movimiento(copia_tablero,indice_usuario,MOVERSE_RESPUESTA_INCORRECTA)
            else:
                movimiento_extra = numero_movimientos_extras(copia_tablero, indice_usuario + MOVERSE_RESPUESTA_INCORRECTA)
                retrocesos_totales = movimiento_extra + MOVERSE_RESPUESTA_INCORRECTA
                intercambiar_valor_en_un_movimiento(copia_tablero, indice_usuario, retrocesos_totales)

        indice_usuario = buscar_usuario(copia_tablero, nombre_usuario)

        if verificar_perdedor(indice_usuario):
            print("Perdiste")
            jugar = "no"
        elif verificar_ganador(copia_tablero,indice_usuario):
            print("Ganaste")
            jugar = "no"
        elif verificar_lista_vacia(preguntas):
            print("Preguntas agotadas")
            jugar = "no"
        else:  
            jugar = pedir_string("Desea jugar?(si/no): ")
            jugar = validar_string(jugar,"si","no")

guardar_score(indice_usuario,nombre_usuario)
print("quedaste en el casillero: ", indice_usuario)
print("Fin del programa")