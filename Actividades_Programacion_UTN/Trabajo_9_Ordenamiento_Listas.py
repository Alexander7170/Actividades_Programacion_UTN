#   Ejercicio 1
from biblioteca import modulos
"""
Dadas las siguientes listas:
Nombres =["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Anto
nio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que realice el ordenamiento de las listas por nombre de
manera ascendente
"""
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def ordenar_ascendentemente_listas(lista:list,lista_2:list)->list:
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                aux = lista_2[i]
                lista_2[i] = lista_2[j]
                lista_2[j] = aux


def mostrar_dos_listas(lista1:list,mensaje:str,lista2:list):
    for i in range(len(lista1)):
        print("{:<25}{:<14}{:<20}".format(lista1[i], mensaje, lista2[i]))

ordenar_ascendentemente_listas(Nombres,Edades)
mostrar_dos_listas(Nombres,"Con edad de ",Edades)


#   Ejercicio 2 
"""
Dadas las siguientes listas:
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias
Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
"Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
Desarrollar una función que realice el ordenamiento de las listas por nombre de
manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera
descendente.
"""

Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias","Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos","Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def ordenar_ascendentemente_si_igual__entonces_descendentemente(lista:list,lista_numeros:list):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                aux = lista_numeros[i]
                lista_numeros[i] = lista_numeros[j]
                lista_numeros[j] = aux
            elif lista[i] == lista[j]:
                if lista_numeros[i] < lista_numeros[j]:
                    aux = lista_numeros[i]
                    lista_numeros[i] = lista_numeros[j]
                    lista_numeros[j] = aux

ordenar_ascendentemente_si_igual__entonces_descendentemente(Nombres,Puntos)
mostrar_dos_listas(Nombres,"con puntos de: ", Puntos)

#   Ejercicio 3
"""
Dadas las siguientes listas:
Estudiantes =
["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Anto
nio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos =
[“Sosa”,”Gutierrez”,”Alsina”,”Martinez”,”Sosa”,”Ramirez”,”Perez”,”Lopez”,”Arregui”
,”Mitre”,”Andrade”,”Loza”,”Antares”,”Roca”,”Perez”]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
Desarrollar una función que realice el ordenamiento de las listas por apellido de
manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
ascendente, si el nombre también es el mismo, debe ordenar por nota de manera
descendente.
"""
Estudiantes =["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
def ordenar_lista_ascendentemente_ascedentemente_descendentemente(lista_1:list, lista_2:list, lista_3:list):
    for i in range(len(lista_1)-1):
        for j in range(i+1,len(lista_1)):
            if lista_1[i] > lista_1[j]:
                aux = lista_1[i]
                lista_1[i] = lista_1[j]
                lista_1[j] = aux
                aux = lista_2[i]
                lista_2[i] = lista_2[j]
                lista_2[j] = aux
                aux = lista_3[i]
                lista_3[i] = lista_3[j]
                lista_3[j] = aux
            elif lista_1[i] == lista_1[j]:
                if lista_2[i] > lista_2[j]:
                    aux = lista_2[i]
                    lista_2[i] = lista_2[j]
                    lista_2[j] = aux
                elif lista_2[i] == lista_2[j]:
                    if lista_3[i] < lista_3[j]:
                        aux = lista_3[i]
                        lista_3[i] = lista_3[j]
                        lista_3[j] = aux
def imprimir_tres_listas(lista1:list, mensaje:str, lista2:list, mensaje2:str, lista3:list):
    for i in range(len(lista1)):
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(lista1[i], mensaje, lista2[i], mensaje2, lista3[i]))

ordenar_lista_ascendentemente_ascedentemente_descendentemente(Apellidos,Estudiantes,Nota)

imprimir_tres_listas(Estudiantes," con apellido de: ", Apellidos, " con nota de:", Nota)

#Ejercicio 4
