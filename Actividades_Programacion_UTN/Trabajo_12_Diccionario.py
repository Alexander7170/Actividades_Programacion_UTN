from biblioteca.estudiantes import *
from biblioteca.modulo_v3 import *
from biblioteca.modulo import pedir_entero_con_parametros 
from biblioteca.modulo_listas_bidimencionales import buscar_promedios_en_listas_anidadas
from biblioteca.modulo_listas import buscar_promedio, buscar_la_posicion_del_mayor_entero, buscar_el_elemento_del_menor_entero
imprimir_menu_de_opciones_estudiantes()
flag = True
while flag: 
    match pedir_entero_con_parametros("Dime una opcion del 1 al 7: ",1,7): 
        case 1:
            ordenar_lista_dic_ascen_ascen(estudiantes)
            imprimir_lista_dic_v1(estudiantes)
        case 2:
            listas_notas = buscar_con_clave(estudiantes,"notas")
            promedio_notas = buscar_promedios_en_listas_anidadas(listas_notas)
        case 3:
            estudiantes_ingenieros_informaticos = filtrar_dic_str(estudiantes,"programa","Ingenieria en Informatica")
            imprimir_lista_dic_v1(estudiantes_ingenieros_informaticos)
        case 4:
            lista_edades = buscar_con_clave(estudiantes,"edad")
            promedio_edad = buscar_promedio(lista_edades)
        case 5:
            listas_notas = buscar_con_clave(estudiantes, "notas")
            promedio_notas = buscar_promedios_en_listas_anidadas(listas_notas)
            indice_del_mayor_promedio = buscar_la_posicion_del_mayor_entero(promedio_notas)
            imprimir_datos_nombre_apellido(estudiantes,indice_del_mayor_promedio)
        case 6:
            estudiantes_en_clubes = filtar_clave(estudiantes,"grupos")
            estudiantes_del_club_informatica = filtrar_dic_str(estudiantes_en_clubes,"grupos","Club de Informatica")
            listas_notas = buscar_con_clave(estudiantes_en_clubes,"notas")
            promedios_notas = buscar_promedios_en_listas_anidadas(listas_notas)
            imprimir_datos_estudiantes_con_promedio(estudiantes_del_club_informatica,promedios_notas)
        case 7:
            lista_edades = buscar_con_clave(estudiantes,"edad")
            el_menor_edad = buscar_el_elemento_del_menor_entero(lista_edades)
            estudiantes_misma_menor_edad = filtrar_dic_entero(estudiantes,"edad",el_menor_edad)
            imprimir_datos_menor_edad(estudiantes_misma_menor_edad)