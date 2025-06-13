from biblioteca.modulo import pedir_entero_con_parametros
from biblioteca.modulo import pedir_string
from biblioteca.modulo_listas_tridimencionales import *


    
gondola = [[["(1,1)" , "" , 0] , ["(1,2)" , "botellas",3] , ["(1,3)" , "",0]       , ["(1,4)" , "frascos" , 8] , ["(1,5)" , "" , 0]],
           [["(2,1)" , "" , 0] , ["(2,2)" , "",0]         , ["(2,3)" , "fideos",4] , ["(2,4)" , "", 0]        , ["(2,5)" , "" , 0]],
           [["(3,1)" , "" , 0] , ["(3,2)" , "",0]         , ["(3,3)" , "",0]       , ["(3,4)" , "leche" , 6]   , ["(3,5)" , "" , 0]]]
gestionar_menu_de_opciones = True
alta_producto = False
imprimir_menu_de_opciones_v1()
while gestionar_menu_de_opciones:
    match pedir_entero_con_parametros("Dime a cual quieres acceder: ",0,7):
        case 1:
            alta_producto = True
            producto_nuevo = pedir_string("Dime que producto quieres añadir?: ")
            existe_producto = verificar_existencia_string_en_lista_tridimencional(gondola,producto_nuevo)
            imprimir_dependiendo_bool(existe_producto,"Producto ya existe","Producto no existe, vamos a agregarlo")
            if existe_producto == False:
                fila = pedir_entero_con_parametros("Dime en que fila de la 1 a la 3 queres que este ? ",1,3) - 1
                columna = pedir_entero_con_parametros("Dime en que columna de la 1 a la 5 queres que este ? ",1,5) - 1
                posicion_ocupada = verificar_indice_con_string_en_lista_tridimencional(gondola,fila,columna,1)
                if posicion_ocupada == False:
                    unidades_del_producto = pedir_entero_mayor_al_minimo("Dime cuantas unidades agrego?: ", 1 )
                    asignar_string_en_lista_tridimencional(gondola, producto_nuevo, fila , columna ,1 )
                    asignar_entero_en_lista_tridimencional(gondola, unidades_del_producto, fila , columna ,2 )
                imprimir_dependiendo_bool(posicion_ocupada,"Ya existe un producto en esa posicion", "Producto agregado")     
        case 2: 
            if alta_producto:
                producto_eliminar = pedir_string("Dime que producto quieres eliminar?: ")
                existe_producto = verificar_existencia_string_en_lista_tridimencional(gondola,producto_eliminar)
                if existe_producto:
                    indices_producto = buscar_en_lista_tridimencional_string_posiciones(gondola,producto_eliminar)
                    subtituir_string_en_lista_tridimencional(gondola,producto_eliminar,"")
                    asignar_entero_en_lista_tridimencional(gondola, 0 ,indices_producto[0],indices_producto[1], 2)
                imprimir_dependiendo_bool(existe_producto,"Producto eliminado","Ese producto no existe")
        case 3:
            if alta_producto:
                producto_modificar = pedir_string("Que producto quieres modificar ?: ")
                existe_producto = verificar_existencia_string_en_lista_tridimencional(gondola , producto_modificar)
                if existe_producto:
                    fila_nueva = pedir_entero_con_parametros("Dime en que fila (1/3)queres que lo cambie: ",1,3) - 1
                    columna_nueva = pedir_entero_con_parametros("Dime en que columna (1,5) queres que lo cambie: ",1,5)- 1
                    indices_producto_viejo = buscar_posiciones_de_string_en_lista_tridimencional(gondola , producto_modificar)
                    indices_producto_nuevo = [ fila_nueva , columna_nueva , 1]
                    intercambiar_valores_en_lista_tridimencional(gondola,indices_producto_viejo,indices_producto_nuevo)
                    cantidad_nueva = pedir_entero_mayor_al_minimo("Dime la cantidad a modificar del producto?: ", 1)
                    indices_cantidad_vieja = cambiar_indice_de_una_lista_de_indices(indices_producto_viejo,2,2)
                    indices_cantidad_nueva = cambiar_indice_de_una_lista_de_indices(indices_producto_nuevo,2,2)
                    intercambiar_valores_en_lista_tridimencional(gondola,indices_cantidad_vieja,indices_cantidad_nueva)
                imprimir_dependiendo_bool(existe_producto,"Producto cambiado", "No existe el producto a cambiar")

        case 4:
                mostrar_listas_tridimencionales_v1(gondola)
        case 5:
                lista_bidimencional = transformar_lista_tridimencional_en_bidimencional(gondola)
                ordenar_lista_bidimencional_v1(lista_bidimencional)
                lista_tridimencional = transformar_lista_bidimencional_en_tridimencional(lista_bidimencional,gondola)
                mostrar_listas_tridimencionales_v1(lista_tridimencional)
        case 6 :
                gestionar_menu_de_opciones = False
    imprimir_dependiendo_bool(alta_producto,"lista importada","lista no importada")


#   Ejercicio 5: #tonto

estanteria = [[["tornillo 12", 65], ["tornillo 16", 86], ["tornillo 20", 65], ["tornillo 25", 45]],
            [["tornillo 30", 68], ["tornillo 35", 73], ["tornillo 40", 85], ["tornillo 45", 89]],
            [["tarugo 4", 58], ["tarugo 5", 48], ["tarugo 6", 64], ["tarugo 7", 96]],
            [["tarugo 8", 36], ["tarugo 10", 72], ["tarugo 12", 78], ["tarugo 14", 71]]]

imprimir_menu_de_opciones_v2()
salir_menu = False
while salir_menu == False:
    match pedir_entero_con_parametros("Dime que opcion del menu quiere entrar (1/4): ",1 , 4 ):
        case 1:
            producto_a_reponer = pedir_string("Dime el producto a reponer: ")
            existe_producto = verificar_existencia_string_en_lista_tridimencional(estanteria,producto_a_reponer)
            imprimir_dependiendo_bool(existe_producto,"Producto existe","El producto no existe")
            if existe_producto:  
                cantidad_nueva = pedir_entero_mayor_al_minimo("Dime cuantas unidades mas quieres agregar?: ",0)
                indices_producto = buscar_posiciones_de_string_en_lista_tridimencional(estanteria,producto_a_reponer)
                indices_cantidad = cambiar_indice_de_una_lista_de_indices(indices_producto,2,1)
                vieja_cantidad_del_producto = buscar_segun_posicion_un_entero_en_lista_tridimencional(estanteria,indices_cantidad[0],indices_cantidad[1],indices_cantidad[2])
                nueva_cantidad_del_producto = sumar_numeros(vieja_cantidad_del_producto,cantidad_nueva)
                asignar_entero_en_lista_tridimencional(estanteria,nueva_cantidad_del_producto,indices_cantidad[0],indices_cantidad[1],indices_cantidad[2])
            imprimir_dependiendo_bool(existe_producto,"cantidad_nueva agregado","El producto no existe")
        case 2:
            producto_a_vender = pedir_string("Dime el producto a vender: ")
            existe_producto = verificar_existencia_string_en_lista_tridimencional(estanteria,producto_a_vender)
            imprimir_dependiendo_bool(existe_producto,"el producto existe, puede venderse","El producto no existe para vender")
            if existe_producto:
                 cantidad_a_vender = pedir_entero_mayor_al_minimo("Dime cual es la cantidad que vas a vender: ",0)
                 indices_producto = buscar_posiciones_de_string_en_lista_tridimencional(estanteria,producto_a_vender)
                 indices_cantidad_del_producto = cambiar_indice_de_una_lista_de_indices(indices_producto,2,1)
                 vieja_cantidad_del_producto = buscar_segun_posicion_un_entero_en_lista_tridimencional(estanteria,indices_cantidad_del_producto[0],indices_cantidad_del_producto[1],indices_cantidad_del_producto[2])
                 nueva_cantidad_del_producto = restar_numeros(vieja_cantidad_del_producto,cantidad_a_vender)
                 alcanza_stock = verificar_entero_por_un_minimo(vieja_cantidad_del_producto,nueva_cantidad_del_producto)
                 imprimir_dependiendo_bool(alcanza_stock,"Cantidad del producto vendida", "la cantidad a vender no alcanza con el stock")
                 if alcanza_stock:
                    asignar_entero_en_lista_tridimencional(estanteria,nueva_cantidad_del_producto,indices_cantidad_del_producto[0],indices_cantidad_del_producto[1],indices_cantidad_del_producto[2])
        case 3:
            mostrar_listas_tridimencionales_v2(estanteria)
        case 4:
              salir_menu = True

          