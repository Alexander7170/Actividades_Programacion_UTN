
def imprimir_menu_de_opciones_estudiantes():
    """
    Funcion que imprimir un menu de opciones de 7 lineas 
    """
    print("""
1-Listar los alumnos por orden ascendente de apellido, si se repite, ordenar por nombre. Mostrar legajo, nombre, apellido y edad 
2-Obtener el promedio de notas para cada estudiante
3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de “Ingenieria en Informatica“
4-Obtener un promedio de edad de los estudiantes. Mostrar nombre y apellido
5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y apellido
6-Listar nombre y apellido de los alumnos que forman el grupo “Club de Informática” con sus respectivos promedios
7-Listar legajo, nombre, apellido y programas que cursan los alumnos más jóvenes.""")

def imprimir_lista_dic_v1(lista_de_diccionarios:dict):
    """
    funcion que imprime en forma de formato los valores con los keys "nombre", "apellido", "legajo" y "edad" de una
    lista de diccionarios. Cada fila del formato represente cada estudiante son los, sus columnas el nombre del key
    cada interseccion representa el valor del key de dicha en dicha lista de diccionario
    se muestra los valores

    Parametros:
    
    lista_de_diccionarios: Una lista donde estan los keys "nombre", "apellido", "legajo" y "edad" 
    """
    print("{:<12}{:<12}{:<12}{:<12}".format("Nombre", "Apellido", "legajo", "edad"))
    for i in range(len(lista_de_diccionarios)):
        print("{:<12}{:<12}{:<12}{:<12}".format(lista_de_diccionarios[i]["nombre"], lista_de_diccionarios[i]["apellido"],lista_de_diccionarios[i]["legajo"],lista_de_diccionarios[i]["edad"]))

def imprimir_datos_nombre_apellido(lista_de_diccionarios:dict, indice:int):
    """
    Funcion que imprime en forma de formato los valores dentro del key "nombre" y "apellido" pero de solo un diccionario
    de la lista de diccionarios, que lo determina la posicion

    Parametros:

    lista_de_diccionarios: Una lista donde todos sus elementos son diccionarios y donde solo imprimiremos un diccionarios usando un indice

    indice: un entero que determina la posicion donde esta el diccionario en la lista de diccionarios

    """
    print("{:<12}{:<12}".format("Nombre", "Apellido"))
    print("{:<12}{:<12}".format(lista_de_diccionarios[indice]["nombre"], lista_de_diccionarios[indice]["apellido"]))

def imprimir_datos_estudiantes_con_promedio(lista_de_diccionarios:dict, promedios:list):
    """
    Funcion que imprime en formato 
    """
    print("{:<12}{:<12}{:<12}".format("Nombre", "Apellido", "Promedio notas"))
    for i in range(len(lista_de_diccionarios)):
        print("{:<12}{:<12}{:<12}".format(lista_de_diccionarios[i]["nombre"], lista_de_diccionarios[i]["apellido"], promedios[i]))

def imprimir_datos_menor_edad(lista_de_diccionarios:dict):
    print("{:<12}{:<12}{:<12}{:<12}{:<15}".format("Legajo","Nombre", "Apellido", "Programas", "Nivel"))
    for i in range(len(lista_de_diccionarios)):
        print("{:<12}{:<12}{:<12}{:<12}{:<15}".format(lista_de_diccionarios[i]["legajo"], lista_de_diccionarios[i]["nombre"],
                                                 lista_de_diccionarios[i]["apellido"], lista_de_diccionarios[i]["programa"]["nombre"], lista_de_diccionarios[i]["programa"]["nivel"]))

def ordenar_lista_dic_ascen_ascen(lista_de_diccionarios:list):
    """
    Funcion que ordena la lista de diccionarios comparando el valor dentro del key "apellido" ascendentemente.
    Si la comparacion es igual, entonces compara el valor dentro del key "nombre" ascendentemente

    Parametros:

    lista_de_diccionarios: una lista donde estan los keys "nombre" y "apellido"
    """
    for i in range(len(lista_de_diccionarios)-1):
        for j in range(i+1,len(lista_de_diccionarios)):
            if lista_de_diccionarios[i]["apellido"] > lista_de_diccionarios[j]["apellido"]:
                aux = lista_de_diccionarios[i]
                lista_de_diccionarios[i] = lista_de_diccionarios[j]
                lista_de_diccionarios[j] = aux
            elif lista_de_diccionarios[i]["apellido"] == lista_de_diccionarios[j]["apellido"]:
                if lista_de_diccionarios[i]["nombre"] > lista_de_diccionarios[j]["nombre"]:
                    aux = lista_de_diccionarios[i]
                    lista_de_diccionarios[i] = lista_de_diccionarios[j]
                    lista_de_diccionarios[j] = aux

def buscar_con_clave(lista_de_diccionarios:list, key:str)->list:
    """
    Funcion que busca una clave en cada diccionario y guarda el valor o los valores

    Parametros:

    lista_de_diccionarios: una lista de diccionarios, donde se encuentras las claves y sus valores

    key: Un string, que representa la clave que usaremos para guardar su valor en la lista nueva

    Retorno:
        Devuelve una lista nueva con el valor o los valores de una clave de cada diccionario
    """
    lista_valores = []
    for lista in lista_de_diccionarios:
        valor = lista[key]
        lista_valores.append(valor)
    return lista_valores

def filtar_clave(lista_de_diccionarios:list ,clave:str)->list:
    """
    Funcion que filtra una el nombre de la clave de cad diccionario en la lista de diccionarios

    Parametros:

    lista_de_diccionarios: una lista donde sus elementos son todos diccionarios y donde filtraremos un key

    clave: un string que sera el filtro que le pondremos a la lista diccionario, el nombre del key

    Retorno:
        Devuelve una lista nueva con los elementos originales pero sin los elementos que no contengan esa clave en sus diccionarios

    """
    lista_nueva = [ ]
    for diccionario in lista_de_diccionarios:
        for key in diccionario:
            if key == clave:
                lista_nueva.append(diccionario)
    return lista_nueva

def filtrar_dic_str(lista_de_dicionarios:list, clave:str, string_filtrar:str)->list:
    """
    Funcion que en una lista de diccionarios, filtrara un determinado valor string
    con un mismo nombre de clave para lista de diccionario
    Parametros: 

    lista_de_diccionarios: una lista donde todos sus elementos son diccionarios, y donde dentro de una clave buscaremos la palabra

    Keys: Un string que seria la clave donde buscaremos dentro de cada lista de diccionario

    string: la palabra que buscaremos dentro de las claves en la lista de diccionarios

    Retorno:
        Devuelve una nueva lista de diccionarios igual a la pasada como parametro pero solo con los elementos donde se 
        haya encontrado el string como el valor
    """
    lista_filtrada = []
    for persona in lista_de_dicionarios:
        for dato in persona[clave]:
            for elemento in dato:
                if dato[elemento] == string_filtrar:
                    lista_filtrada.append(persona)
    return lista_filtrada

def filtrar_dic_entero(lista_de_dicionarios:list, clave:str, entero_filtrar:int)->list:
    """
    Funcion que filtrara los diccionarios que tengan en una determinada clave, el mismo numero entero

    Parametros: 

    lista_de_diccionarios: una lista donde todos sus elementos son diccionarios. Donde buscaremos el mismo numero de una clave fija

    Keys: Un string que seria la clave fija

    entero_filtrar: El numero entero que se usara como el criterio para filtrar diccionarios en una lista de diccionarios 

    Retorno:
        Devuelve una nueva lista de diccionarios igual a la original pero solo con los diccionarios donde se 
        haya encontrado el numero entero en la clave
    """
    lista_filtrada = []
    for persona in lista_de_dicionarios:
        if persona[clave] == entero_filtrar:
            lista_filtrada.append(persona)
    return lista_filtrada
