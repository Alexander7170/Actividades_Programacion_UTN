from Modulo_juego import *
from copy import deepcopy
from Datos_juego_por_consola import *
# CREAR FUNCION QUE VALIDE LA TABLA

nombre_usuario = pedir_string("Holaa, como te llamas?: ")
indice_usuario = PUNTO_DE_PARTIDA
copia_tablero = deepcopy(tablero)
jugar = pedir_string(" Quiere jugar ?(si/no): ")
jugar = validar_string(jugar,"si","no")
usuario_ubicado = False
while jugar == "si":
    if usuario_ubicado == False:
        ubicar_usuario(copia_tablero,PUNTO_DE_PARTIDA, nombre_usuario)
        usuario_ubicado = True
    actualizar_tablero_segun_indice(copia_tablero,indice_usuario)
    imprimir_tablero(copia_tablero)

    dic_pregunta_opciones = buscar_dic_random(preguntas)
    eliminar_un_dict(preguntas, dic_pregunta_opciones)
    imprimir_valores_con_excepcioon( dic_pregunta_opciones,"respuesta_correcta")

    respuesta_usuario = pedir_string("Respuesta:  ")
    respuesta_correcta = verificar_respuesta( dic_pregunta_opciones, respuesta_usuario, "respuesta_correcta")

    if respuesta_correcta:

        print("Correcto")
        indice_casillero_a_moverse = indice_usuario + MOVERSE_RESPUESTA_CORRECTA
        casillero_vacio = verificar_casillero_vacio(copia_tablero, indice_casillero_a_moverse)
        if casillero_vacio:
            intercambiar_i_usuario(copia_tablero, indice_usuario, indice_casillero_a_moverse)
        else:
            avanzar_demas = cant_movimiento_adicionales(copia_tablero, indice_casillero_a_moverse)
            indice_casillero_a_moverse += avanzar_demas
            intercambiar_i_usuario(copia_tablero, indice_usuario, indice_casillero_a_moverse)

    else:
        print("Incorrecto")
        indice_casillero_a_moverse = indice_usuario + MOVERSE_RESPUESTA_INCORRECTA
        casillero_vacio = verificar_casillero_vacio(copia_tablero, indice_casillero_a_moverse)
        if casillero_vacio:
            intercambiar_i_usuario(copia_tablero,indice_usuario, indice_casillero_a_moverse)
        else:
            retroceder_demas = cant_movimiento_adicionales(copia_tablero, indice_casillero_a_moverse)
            indice_casillero_a_moverse += retroceder_demas 
            intercambiar_i_usuario(copia_tablero, indice_usuario, indice_casillero_a_moverse)

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
        if jugar == "no":
            guardar_score(indice_usuario,nombre_usuario)

print("quedaste en el casillero: ", indice_usuario)
print("Fin del programa")
