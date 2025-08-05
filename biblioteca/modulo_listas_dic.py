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
    Funcion que filtra una el nombre de la clave de cada diccionario en la lista de diccionarios
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
