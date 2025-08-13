import pygame
from renderizar import *
from data import *
pygame.init()

def analizar_correr_juego(state_game:dict , events:list):
    """
    analiza si el usuario quiere cerrar la ventana
    """
    for event in events:
        if event.type == pygame.QUIT:
            state_game["running"] = False


# ESCRIBIENDO NOMBRE USUARIO / PANTALLA 0
def get_datos_logicos_p0(reglas:dict,datos_usuario:dict)->dict:
    return {"guardo_nombre": False,
            "quiere_escribir": False,
            "max_letras_nombre": reglas["user_new"]["max_letras_name"],
            "username": datos_usuario["username"]}

def get_datos_visuales_p0(screen,datos_logicos:dict)->dict:
    data = {"pantalla":screen,
            "img_bg": get_data_img_bg("Imagenes/fondo nombre.png",None, True, (300,100)),
            "img_txt": get_data_img_txt(datos_logicos["username"],ESTILOS["nombre"],False,(340,300))}
    return data

def p0(datos_logicos:dict, datos_visuales:dict, events:list):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            analizar_click_p0(datos_logicos,datos_visuales, event)
        elif event.type == pygame.KEYDOWN and datos_logicos["quiere_escribir"]:
            analizar_tecla_p0(datos_logicos, datos_visuales,event)
    blit_p0(datos_visuales)

def analizar_tecla_p0(datos_logicos:dict,datos_visuales:dict,event:pygame.event.Event ):
    """
    Funcion que analiza la key presionada, actualizando los data y el state_game
    """
    key = event.key
    username = datos_logicos["username"]
    if key == pygame.K_RETURN:
        datos_logicos["guardo_nombre"] = True
    elif key == pygame.K_BACKSPACE:
        username = username[0:-1]
    elif len(username) <= datos_logicos["max_letras_nombre"]:
        username += event.unicode
    datos_visuales["img_txt"]["img"] = renderizar_valor(username)
    datos_logicos["username"] = username

def analizar_click_p0(datos_logicos:dict, datos_visuales:dict,event:pygame.event.Event):
    posicion_click = event.pos
    if datos_visuales["img_bg"]["rect"].collidepoint(posicion_click):
        datos_logicos["quiere_escribir"] = True

def blit_p0(datos:dict):
    datos["pantalla"].blit(datos["img_bg"]["img"],datos["img_bg"]["ubicacion"])
    datos["pantalla"].blit(datos["img_txt"]["img"],datos["img_txt"]["ubicacion"])

# ELIGIENDO PRIMERAS CARTAS/ PANTALLA 1
def get_datos_logicos_p1(configuracion:dict, datos_usuario:dict)->dict:
    calculos = get_calculos_ubication((10,10),(250,250),4)
    return{"guardo_cartas":False,
           "opciones_de_cartas":configuracion["user_new"]["cant_opciones_cartas"],
            "cant_cartas_user":datos_usuario["cant_cartas"],
            "max_cartas_elegir":configuracion["user_new"]["max_cartas_elegir"],
            "calculos":calculos,
            "desbloqueadas": datos_usuario["desbloqueadas"]}

def get_datos_visuales_p1(pantalla:pygame.Surface, img_cartas:dict, datos_logicos:dict)->dict:
    cartas_ramdom = seleccionar_cartas_random(img_cartas,datos_logicos["opciones_de_cartas"])
    asignar_ubication_cartas(cartas_ramdom,datos_logicos["calculos"])
    return{"pantalla":pantalla,
           "cartas": cartas_ramdom}

def p1(datos_logicos:dict, datos_visuales:dict,events:list):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            analizar_click_p1(datos_logicos,datos_visuales,event)
    blit_p1(datos_logicos, datos_visuales)

def analizar_click_p1(datos_logicos:dict,datos_visuales:dict,evento:pygame.event.Event):
    posicion_click = evento.pos
    for id in datos_visuales["cartas"]:
        if datos_visuales["cartas"][id]["rect"].collidepoint(posicion_click):
            datos_logicos["cant_cartas_user"] += 1
            datos_logicos["desbloqueadas"][id] = True
            if datos_logicos["cant_cartas_user"] == datos_logicos["max_cartas_elegir"]:
                datos_logicos["guardo_cartas"] = True

def blit_p1(datos_logicos:dict, datos_visuales:dict):
    for id in datos_visuales["cartas"]:
        if datos_logicos["desbloqueadas"][id] == False:
            datos_visuales["pantalla"].blit(datos_visuales["cartas"][id]["img"],datos_visuales["cartas"][id]["rect"])



# Menu / PANTALLA 2

def get_datos_visuales_p2(pantalla:pygame.Surface)->dict:
    data = {"pantalla":pantalla,
            "jugar": get_data_img_bg("Imagenes/boton_jugar.png",None, True, (300,100)),
            "ver_cartas":get_data_img_bg("Imagenes/boton_almacen.png",None, True, (300,300)),
            "salir": get_data_img_bg("Imagenes/boton_salir.png", None, True,(300,600))}
    return data

def p2(flujo_juego:dict, datos_visuales:dict, events:list):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            analizar_click_p2(flujo_juego,datos_visuales, event)
    blit_p2( datos_visuales)

def analizar_click_p2(flujo_juego:dict, datos_visuales:dict, event:pygame.event.Event):
    """
    analiza la coordenada del click con los rects, actualizando si hubo colicion, el estado de la pantalla
    """
    position_click = event.pos
    rect_jugar = datos_visuales["jugar"]["rect"]
    rect_ver_cartas = datos_visuales["ver_cartas"]["rect"]
    rect_salir = datos_visuales["salir"]["rect"]
    
    if rect_jugar.collidepoint(position_click):
        flujo_juego["pantalla"] = 3
        flujo_juego["obtener_data"] = True
    elif rect_ver_cartas.collidepoint(position_click):
        flujo_juego["pantalla"] = 4
        flujo_juego["obtener_data"] = True
    elif rect_salir.collidepoint(position_click):
        flujo_juego["running"] = False

def blit_p2(datos:dict):
    datos["pantalla"].blit(datos["jugar"]["img"],datos["jugar"]["rect"])
    datos["pantalla"].blit(datos["ver_cartas"]["img"],datos["ver_cartas"]["rect"])
    datos["pantalla"].blit(datos["salir"]["img"],datos["salir"]["rect"])

# MIRANDO LAS CARTAS / PANTALLA 4

def get_datos_logicos_p4(datos_usuario:dict)->dict:
    calculos = get_calculos_ubication((10,10),(240,240),5)
    return{"desbloqueadas": datos_usuario["desbloqueadas"],
           "orden_cartas":0,
           "calculos":calculos}

def get_datos_visuales_p4(pantalla:pygame.Surface, cartas:dict, datos_logicos:dict)->dict:
    cartas_del_usuario = filtrar_cartas_desbloqueadas(cartas,datos_logicos["desbloqueadas"])
    asignar_ubication_cartas(cartas_del_usuario,datos_logicos["calculos"]) #UBICO EL RECT DE CADA CARDA DE ESE DICT
    return {"pantalla":pantalla,
            "cartas": cartas_del_usuario}

def p4(datos_visuales:dict, eventos:pygame.event.Event):
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            analizar_click_p4(datos_visuales,evento)
    blit_p4(datos_visuales)

def analizar_click_p4(datos_visuales:dict,event:pygame.event.Event):
    boton_clickeado = event.button
    if boton_clickeado == 4 or boton_clickeado == 5:
        if boton_clickeado == 4:
            eje_y = -30
        else:
            eje_y = 30
        for id in datos_visuales["cartas"]:
            datos_visuales["cartas"][id]["rect"].y += eje_y
def blit_p4(datos:dict):
    for id in datos["cartas"]:
        datos["pantalla"].blit(datos["cartas"][id]["img"], datos["cartas"][id]["rect"])

def guardar_progreso(ruta:str, datos_logicos)-> dict:
    import json
    print(datos_logicos)
    with open(ruta, "w") as archivo:
        txt = json.dump(datos_logicos, archivo)
        return txt
    
def leer_datos_usuario(ruta:str)->dict:
    import json
    try:
        with open(ruta,"r") as archivo:
            data_user = json.load(archivo)
    except FileNotFoundError:
        with open(ruta,"w") as archivo:
            data_user = {"username": "",
            "nivel": 0,
            "gold": 0,
            "cant_cartas": 0,
            "desbloqueadas":{"01":False, "02":False, "03":False,"04":False,"05":False,
                      "06":False,"07":False,"08":False,"09":False,"10":False,
                      "11":False,"12":False}}
            json.dump(data_user, archivo)
    return data_user

def get_img(datos_visuales:dict, scale:tuple):
    for id in datos_visuales:
        imagen = pygame.image.load(datos_visuales[id]["ruta_foto"])
        datos_visuales[id]["foto"] = pygame.transform.scale(imagen, scale)

def filtrar_cartas_desbloqueadas(all_cartas:dict, desbloqueadas:dict)->dict:
    cartas_de_usuario = {}
    for id in desbloqueadas:
        if desbloqueadas[id]:
            cartas_de_usuario[id] = all_cartas[id]
    return cartas_de_usuario

def seleccionar_cartas_random(cartas:dict, cant:int)->dict:
    import random
    lista_cartas = list(cartas)
    lista_cartas_seleccionadas = []
    for numero in range(cant):
        carta_seleccionada = random.choice(lista_cartas)
        lista_cartas.remove(carta_seleccionada)
        lista_cartas_seleccionadas.append(carta_seleccionada)
    dict_cartas_seleccionadas = transform_list_a_dict(lista_cartas_seleccionadas,cartas)
    return dict_cartas_seleccionadas


def ordenar_dict_aleatoriamente(cartas:dict)->list:
    """
    ordena los keys del dict de manera aleatoria, devolviendo una lista de esos keys ya ordenados
    """
    import random
    lista_cartas = list(cartas)
    lista_ordenada = []
    for i in range(len(lista_cartas)):
        carta_aleatoria = random.choice(lista_cartas)
        lista_cartas.remove(carta_aleatoria)
        lista_ordenada.append(carta_aleatoria)
    return lista_ordenada

#   Ubicaciones

def get_calculos_ubication(point_init:tuple, dist_rect:tuple, cant_columnas:int)->dict:
    return{"eje_x": point_init[0],
        "eje_y": point_init[1],
        "dx": dist_rect[0],
        "dy": dist_rect[1],
        "columnas": cant_columnas}

def asignar_ubication_cartas(cartas:dict, calculos:dict):

    eje_x = calculos["eje_x"]
    eje_y = calculos["eje_y"]
    columnas = calculos["columnas"]
    dx = calculos["dx"]
    dy = calculos["dy"]
    contador = 0
    for id in cartas:
        cartas[id]["rect"].topleft = (eje_x,eje_y)
        if (contador+1) % columnas == 0:
            eje_x = calculos["eje_x"]
            eje_y += dy
        else:
            eje_x += dx
        contador += 1

def transform_list_a_dict(lista_keys:list, items:dict)->dict:
    dict_cartas = {}
    for key in lista_keys:
        dict_cartas[key] = items[key]
    return dict_cartas

def analizar_collidepoint_cartas_begin(cards:dict, data_user:dict,event:pygame.event.Event):
    """
    Analiza si hubo colicion con algun rect de alguna carta del diccionario de cartas
    """
    posicion_click = event.pos
    for card in cards:
        if cards[card]["rect"].collidepoint(posicion_click):
            cards[card]["desbloqueado"] = True
            data_user["cards"].append(card)

def convinar_imagenes(id:dict)->dict:
    img_convinada = id["carta"]["img"]
    for sector in id:
        img_convinada.blit(id[sector]["img"],id[sector]["ubicacion"])
    return img_convinada

def get_img_cartas(cartas:dict)->dict:
    imagenes_cartas = {}
    imgs_convinadas = {}
    for id in cartas:
        imagenes_cartas[id] = {}
        imgs_convinadas[id] = {}
        imagenes_cartas[id]["foto"] = get_data_img_bg(cartas[id]["ruta_foto"],(160,120),False,(15,15))
        imagenes_cartas[id]["carta"] = get_data_img_bg(cartas[id]["ruta_fondo"],(200,230),False,(0,0))
        imagenes_cartas[id]["nombre"] = get_data_img_txt(cartas[id]["nombre"],ESTILOS["cartas"],False,(35,140))
        imagenes_cartas[id]["hp"] = get_data_img_txt("Vida: " + str(cartas[id]["hp"]),ESTILOS["cartas"],False,(35,160))
        imagenes_cartas[id]["atk"] = get_data_img_txt("Ataque: " + str(cartas[id]["atk"]),ESTILOS["cartas"],False,(35,180))
        imagenes_cartas[id]["vel_atk"] = get_data_img_txt("Vel.Ataque: " + str(cartas[id]["vel_atk"]),ESTILOS["cartas"],False,(35,200))
        imgs_convinadas[id]["img"] = convinar_imagenes(imagenes_cartas[id])
        imgs_convinadas[id]["rect"] = imgs_convinadas[id]["img"].get_rect()
    return imgs_convinadas

def ordenar_diccionario(diccionario:dict, forma_ordenamiento:str, criterio:str)->list:
    """
    Ordena los keys del diccionario, usando una forma de ordenamiento: asc (ascendentemente) o des(descendentemente).
    Y usando un criterio como ordenamiento, daño, vida, vel_atq o el nombre

    """
    lista_cartas = list(diccionario) 
    if forma_ordenamiento == "asc":
        for i in range(len(lista_cartas)-1):
            for j in range(i+ 1, len(lista_cartas)):
                if diccionario[lista_cartas[i]][criterio] > diccionario[lista_cartas[j]][criterio]:
                    aux = lista_cartas[i]
                    lista_cartas[i] = lista_cartas[j]
                    lista_cartas[j] = aux
    elif forma_ordenamiento == "des":
        for i in range(len(lista_cartas)-1):
            for j in range(i+ 1, len(lista_cartas)):
                if diccionario[lista_cartas[i]][criterio] < diccionario[lista_cartas[j]][criterio]:
                    aux = lista_cartas[i]
                    lista_cartas[i] = lista_cartas[j]
                    lista_cartas[j] = aux
    return lista_cartas

