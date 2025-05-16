#   EJERCICIO 1
"""
Desarrollar una función que pida 10 nombres de manera secuencial, los
guarde en una lista y la retorne. El programa principal debe invocar a la función y
mostrar por pantalla el retorno
"""
def pedir_elementos (mensaje:str,maximo:int)->list:
    lista_nueva = [0] * maximo
    for i in range(len(lista_nueva)):
        elemento = (input(mensaje))
        lista_nueva[i] = elemento
    return lista_nueva

def mostrar_lista(lista:list):
    print(lista)

variable_lista_1 = [0] * 10
mostrar_lista((pedir_elementos("Diga 10 nombres: ",5)))

#   EJERCICIO 2
"""
Desarrollar una función que inicialice una lista de 10 números en 0, pida
posición y número a guardar al usuario, lo guarde en una lista en la posición
solicitada aleatoriamente y la retorne. El programa principal debe invocar a la
función y mostrar por pantalla el retorno
"""

def cambiar_posicion_numero()->list:
    lista = [0]*10
    numero = int(input("Dime el numero: "))
    posicion = int(input("Diga la posicion del numero: "))
    lista[posicion] = numero
    return lista

mostrar_lista((cambiar_posicion_numero()))


#EJERCICIO 3

def verificar_lista(desde,hasta)->list:
    lista = [0]*10
    for i in range(len(lista)):
        numero = int(input(f"Dime un numero que este dentro del {desde} y {hasta}: "))
        while numero > hasta or numero < desde:
            numero = int(input("No pusiste un numero dentro de los parametros, di de nuevo: "))
        lista[i] = numero
    return lista
mostrar_lista((verificar_lista(2,20)))


#   EJERCICIO 4


def buscar_numero_lista(numero:int, lista:list)->bool:
    flag = False
    for i in range(len(lista)):
        if lista[i] == numero:
            flag = True
            break
    return flag

mostrar_lista((buscar_numero_lista(3,[8,6,5,2,3]))) #ejemplo


#   EJERCICIO 5
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23
          ,25,34,23,46,23,45,67,37,68,25,55,45,27,43]

def retornar_posicion_menor_edad(lista_edades:list)->int:
    #esta funcion sirve para recorrer todos los elementos del array edades.
    #luego retorno la menor edad en la variable posicion:
    flag = True
    for i in range(len(lista_edades)):
        if flag == True:
            menor_edad = lista_edades[i]
            posicion = i
            flag = False
        else:
            if lista_edades[i] < menor_edad:
                menor_edad = lista_edades[i]
                posicion = i
    return posicion

def retornar_lista_posiciones_misma_minima_edad(posicion_menor_edad:int, edades:list)->list:
    #Aca pondriamos los elementos que son iguales a la edad minima a la lista posiciones_misma_edad.
    posiciones_misma_edad= []
    flag = False
    for j in range(len(edades)):
        if edades[posicion_menor_edad] == edades[j]:
            #agrago los elementos a la lista
            posiciones_misma_edad.append(j)
    return posiciones_misma_edad

def imprimir_nombres(edades_lista_actualizada:list, nombres_lista:list, edades_lista):
    # Esta funcion recorrera la edades_lista_actualizada, que seria la lista solo con las ubicaciones
    for i in range (len(edades_lista_actualizada)):
        # imprimo en la lista  edades_lista_actualizada  en el primer elemento de  edades_lista_actualizada que,
        # antes mencionado, seria la primera ubicacion del menor edad
        # hice lo mismo con edades
        print(nombres_lista[edades_lista_actualizada[i]], "con", edades_lista[edades_lista_actualizada[i]], "años")

imprimir_nombres(retornar_lista_posiciones_misma_minima_edad(retornar_posicion_menor_edad(Edades),Edades),Nombres, Edades)

#   Ejercicio 6

from biblioteca import listas_personas 
nombres_lista_personas_6 = listas_personas.nombres
mostrar_lista(nombres_lista_personas_6)

# #   EJERCICIO 7
from biblioteca import modulos
def mostrar_menu_de_opciones():
    print("{:<2} {:<20}".format("Menu    ", "Opciones"))
    print("{:<2} {:<20}".format("1 ----->", "Importar lista"))
    print("{:<2} {:<20}".format("2 ----->", "Listar los datos de los usuarios de México"))
    print("{:<2} {:<20}".format("3 ----->", "Listar los nombre, mail y teléfono de los usuarios de Brasil"))
    print("{:<2} {:<20}".format("4 ----->", "Listar los datos del/los usuario/s más joven/es"))
    print("{:<2} {:<20}".format("5 ----->", "Obtener un promedio de edad de los usuarios"))
    print("{:<2} {:<20}".format("6 ----->", "De los usuarios de Brasil, listar los datos del usuario de mayor edad"))
    print("{:<2} {:<20}".format("7 ----->", "Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000"))
    print("{:<2} {:<20}".format("8 ----->", "Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años."))

Lista_importada = False
fin_del_programa = False
while fin_del_programa == False:
    mostrar_menu_de_opciones()
    match modulos.pedir_entero_con_parametros("dime el numero donde desea ingresar: ",1,8): 
        case 1:
            from biblioteca import listas_personas
            Lista_importada = modulos.importar_lista_true()
            modulos.imprimir_mensaje("Lista importada")
            
        case 2:
            if Lista_importada == True:
                modulos.imprimir_datos_completos_personas_lista(modulos.buscar_string_en_lista("Mexico",listas_personas.country), listas_personas.nombres, listas_personas.telefonos, listas_personas.mails, listas_personas.address, listas_personas.postalZip, listas_personas.region, listas_personas.edades, listas_personas.country)
                fin_del_programa = True
        case 3:
            if Lista_importada == True:
                modulos.imprimir_datos_brazil(modulos.buscar_string_en_lista("Brazil",listas_personas.country),listas_personas.nombres, listas_personas.mails, listas_personas.telefonos )
                fin_del_programa = True
        case 4:
            if Lista_importada == True:
                modulos.imprimir_datos_completos_personas_lista(modulos.guardar_posiciones_en_lista_con_elementos_iguales(modulos.buscar_la_posicion_menor_entero(listas_personas.edades), listas_personas.edades), listas_personas.nombres, listas_personas.telefonos, listas_personas.mails, listas_personas.address, listas_personas.postalZip, listas_personas.region, listas_personas.country, listas_personas.edades)
                fin_del_programa = True
        case 5:
            if Lista_importada == True:
                modulos.imprimir_numero(modulos.retornar_promedio_de_lista(listas_personas.edades))
                fin_del_programa = True
        case 6:
            if Lista_importada == True:
                modulos.imprimir_datos_completos_personas_lista(modulos.buscar_en_determinadas_posiciones_mismo_numero(modulos.buscar_en_determinados_posiciones_mayor_entero(modulos.buscar_string_en_lista("Brazil",listas_personas.country),listas_personas.edades),modulos.buscar_string_en_lista("Brazil",listas_personas.country),listas_personas.edades),listas_personas.nombres, listas_personas.telefonos, listas_personas.mails, listas_personas.address, listas_personas.postalZip, listas_personas.region, listas_personas.edades, listas_personas.country)
                fin_del_programa = True
        case 7:
            if Lista_importada == True:
                modulos.imprimir_datos_completos_personas_lista(modulos.interseccion_posiciones_en_listas(modulos.buscar_elementos_mayores_a_entero(8000,listas_personas.postalZip), (modulos.unir_posiciones(modulos.buscar_string_en_lista("Brazil",listas_personas.country),modulos.buscar_string_en_lista("Mexico",listas_personas.country)))), listas_personas.nombres, listas_personas.telefonos, listas_personas.mails, listas_personas.address, listas_personas.postalZip, listas_personas.region, listas_personas.edades, listas_personas.country)
                fin_del_programa = True
        case 8:
            if Lista_importada == True:
                modulos.imprimir_datos_brazil(modulos.interseccion_posiciones_en_listas(modulos.buscar_string_en_lista("Italy",listas_personas.country), modulos.buscar_elementos_mayores_a_entero(40,listas_personas.edades)),listas_personas.nombres, listas_personas.mails, listas_personas.telefonos )
                fin_del_programa = True
    if Lista_importada == False:
        modulos.imprimir_mensaje("Lista no importada")