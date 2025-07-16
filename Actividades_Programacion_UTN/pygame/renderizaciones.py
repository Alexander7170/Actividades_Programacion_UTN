import pygame
pygame.init()
fuente_grande = pygame.font.SysFont("Comic Sans MS",40)
fuente_mediana = pygame.font.SysFont("Comic Sans MS",30)
fuente_pequeña = pygame.font.SysFont("Arial", 20)
COLOR_NEGRO = (0,0,0)

def renderizar_score(matriz_texto:list)->list:
    """
    Funcion que renderiza todos los valores de una matriz con una fuente y un color

    Parametros:
        matriz_texto: una lista anidada, todos sus elementos deben ser str
        fuente: un fuente, que determina el tipo de texto y el tamaño de la imagen del texto
        color: una tupla, el color del texto al pasarlo a imagen
    Retorno:
        Devuelve una lista anidada, en el mismo orden en que estuvo en el parametro, sale la lista anidada
    """
    lista_scores = []
    for i in range(len(matriz_texto)):
        lista_score = []
        for j in range(len(matriz_texto[i])):
            imagen = fuente_grande.render(matriz_texto[i][j],True,COLOR_NEGRO)
            lista_score.append(imagen)
        lista_scores.append(lista_score)
    return lista_scores

def obtener_imagenes_pantalla_menu()->dict:
    """
    carga las imagenes y las devuelve en forma de diccionario 
    """
    imagen_portada = pygame.image.load("Imagenes/portada titulo.png")
    imagen_jugar = pygame.image.load("Imagenes/jugar.png")
    imagen_score = pygame.image.load("Imagenes/score.png")
    imagen_salir = pygame.image.load("Imagenes/salir.png")
    return {"imagen_portada":imagen_portada,"imagen_jugar":imagen_jugar,"imagen_score":imagen_score, "imagen_salir": imagen_salir}

def renderizar_valores(pregunta:dict)->dict:
    """
    renderiza las cada valor del parametro pregunta, exepto una clave
    """
    imagen_texto_pregunta = fuente_pequeña.render(pregunta["pregunta"],True,COLOR_NEGRO)
    imagen_texto_opcion_a = fuente_pequeña.render(pregunta["respuesta_a"],True,COLOR_NEGRO)
    imagen_texto_opcion_b = fuente_pequeña.render(pregunta["respuesta_b"],True,COLOR_NEGRO)
    imagen_texto_opcion_c = fuente_pequeña.render(pregunta["respuesta_c"],True,COLOR_NEGRO)
    return {"pregunta": imagen_texto_pregunta, "opcion_a":imagen_texto_opcion_a, "opcion_b":imagen_texto_opcion_b, "opcion_c":imagen_texto_opcion_c}

def obtener_imagenes_fijas_score()->dict:
    """
    Carga las imagenes y renderiza los textos que no cambian a lo largo del juego.
    Devuelve un diccionario con esos valores cargados y renderizados
    """
    imagen_volver_menu = pygame.image.load("Imagenes/exit.png")
    imagen_texto_nombre = fuente_grande.render("Nombre",True, COLOR_NEGRO)
    imagen_texto_puntuacion = fuente_grande.render("Puntuacion", True, COLOR_NEGRO)
    return {"volver_menu": imagen_volver_menu, "texto_nombre": imagen_texto_nombre, "texto_puntuacion":imagen_texto_puntuacion}

def obtener_imagenes_fin_juego(datos:dict)->dict:
    """
    renderiza el nombre del usuario y su indice, ambos se deben encontrar en el parametro datos
    devuelve las rendereizaciones
    """
    imagen_texto_nombre = fuente_grande.render("Nombre: " + datos["nombre_usuario"],True,COLOR_NEGRO)
    imagen_texto_puntuacion = fuente_grande.render("Puntuacion: " + str(datos["indice_usuario"]),True,COLOR_NEGRO)
    return{"texto_nombre": imagen_texto_nombre, "texto_puntuacion": imagen_texto_puntuacion}

def renderizar_valor(texto:str)->pygame.Surface:
    """
    renderiza un texto en una fuente grande de color negro y lo devuelve una imagen de texto
    """
    texto = str(texto)
    imagen_texto = fuente_grande.render(texto,True,COLOR_NEGRO)
    return imagen_texto

def renderizar_valor_pequeño(texto:str)->pygame.Surface:
    """
    renderiza un texto en una fuente pequeña de color negro y lo devuelve una imagen de texto
    """
    texto = str(texto)
    imagen_texto = fuente_pequeña.render(texto,True,COLOR_NEGRO)
    return imagen_texto

def obtener_imagenes_fijas_jugando()->dict:
    """
    carga las imagenes de esa pantalla y renderiza los textos que no cambian a lo largo del juego.
    devuelve un diccionario con valores iguales a las imagenes cargadas y las renderizadas
    """

    imagen_volver_menu = pygame.image.load("Imagenes/exit.png")
    imagen_fondo_cronometro = pygame.image.load("Imagenes/casillero negro.png")
    imagen_fondo_pregunta = pygame.image.load("Imagenes/marco rectangulo.png")
    imagen_fondo_opcion = pygame.transform.scale(imagen_fondo_pregunta,(250,60))
    imagen_fondo_pregunta = pygame.transform.scale(imagen_fondo_pregunta,(750,90))
    imagen_casillero_azul = pygame.image.load("Imagenes/casillero azul.png")
    imagen_casillero_rojo = pygame.image.load("Imagenes/casillero rojo.png")
    imagen_casillero_amarillo = pygame.image.load("Imagenes/casillero amarillo.png")
    imagen_casillero_verde = pygame.image.load("Imagenes/casillero verde.png")
    imagen_texto_fin_juego = renderizar_valor("Fin Del Juego")
    return{"volver_menu": imagen_volver_menu,
           "fondo_cronometro":imagen_fondo_cronometro,
           "fondo_pregunta": imagen_fondo_pregunta,
           "fondo_opcion": imagen_fondo_opcion,
           "casillero_rojo": imagen_casillero_rojo,
           "casillero_azul": imagen_casillero_azul,
           "casillero_verde": imagen_casillero_verde,
           "casillero_amarillo": imagen_casillero_amarillo,
           "texto_fin_juego":imagen_texto_fin_juego}

def obtener_imagenes_pregunta_opciones(pregunta_opciones:dict)->dict:
    """
    Funcion que renderiza los valores del diccionario, exepto el valor de una clave
    """
    imagen_texto_pregunta = renderizar_valor_pequeño(pregunta_opciones["pregunta"])
    imagen_texto_opcion_a = renderizar_valor_pequeño(pregunta_opciones["respuesta_a"])
    imagen_texto_opcion_b = renderizar_valor_pequeño(pregunta_opciones["respuesta_b"])
    imagen_texto_opcion_c = renderizar_valor_pequeño(pregunta_opciones["respuesta_c"])
    return{"texto_pregunta":imagen_texto_pregunta,
           "texto_opcion_a": imagen_texto_opcion_a,
           "texto_opcion_b": imagen_texto_opcion_b,
           "texto_opcion_c": imagen_texto_opcion_c}

def obtener_imagenes_texto_tablero(tablero:list,indice_usuario:int)->list:
    """
    Funcion que obtiene todas las imagenes de texto de cada valor del tablero, 
    exepto el valor donde su indice en el tablero sea igual a la del usuario

    Devuelve una lista de imagenes de texto renderizadas
    """
    imagenes_texto = []
    for i in range(len(tablero)):
        if i == indice_usuario:
            texto = ""
        else:
            texto = str(tablero[i])
        imagen_texto = renderizar_valor(texto)
        imagenes_texto.append(imagen_texto)
    return imagenes_texto