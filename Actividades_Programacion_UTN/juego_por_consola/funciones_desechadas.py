#   FUNCIONES DESECHADAS

# """ FUNCION QUE VALIDA UN INDICE DENTRO DE LA LISTA (MAYOR A 0, MENOR A LA CANTIDAD DE ELEMENTOS DE LA LISTA -1 )
#     DEVUELVE ESE INDICE VALIDADO """

# def validar_indice_dentro_lista(tablero:list, indice:int)->int:
#     while indice < 0:
#         indice += 1
#     while indice > len(tablero) - 1:
#         indice -= 1
#     return indice

# """ FUNCION QUE COMPROBABA SI EL MOVIMIENDO TOTAL EXTRA QUE TIENE EL USUARIO ES MAYOR
#     A LA CANTIDAD TOTAL DE CASILLEROS O ES MENOR A 0"""
# def verificar_movimiento_extra(tablero:list, mover_extra:int, indice_usuario:int)->bool:
#    posible = True
#    if (indice_usuario + 1 + mover_extra) > len(tablero) - 1 or (indice_usuario - 1 + mover_extra) < 0:
#        posible = False
#    return posible
# """
# FUNCIONES QUE VALIDABAN LOS AVANCES O RETROCESOS EXTRAS, POR SI LA ESCALERA O SERPIENTE
#     SUBIAN O BAJABAN EN EL CASILLERO MENOR A 0 O MAYOR AL NUMERO TOTAL DE CASILLEROS """
# def validar_avance_extra(tablero:list, avanzar:int, indice_usuario:int)->int:
#    while avanzar + 1 + indice_usuario > len(tablero) - 1:
#        avanzar -= 1
#    return avanzar


# def validar_retroceso_extra(retroceder:int, indice_usuario:int)->int:
#     while retroceder - 1 + indice_usuario < 0:
#         retroceder += 1
#     return retroceder

# def retroceder_casilleros(lista:list, indice_usuario:int, n_retroceso:int, cant_move_extra:int):

#     lista[indice_usuario - n_retroceso + cant_move_extra] = lista[indice_usuario]