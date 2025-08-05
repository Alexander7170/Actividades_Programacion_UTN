import pygame
from blitear import *
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
# Escribiendo

def write_screen(screen, initialization:dict, data_user:dict, events:list):
    if initialization["writting"]:
        data = get_data_write()
        initialization["writting"] = False
    for event in events:
        if event.type == pygame.KEYDOWN:
            analizar_tecla(data_user, data, event)
    blit_write_screen(screen, data)

def analizar_tecla(data_user:dict, data:dict,event:pygame.event.Event ):
    """
    Funcion que analiza la key presionada, actualizando los data y el state_game
    """
    key = event.key
    if key == pygame.K_RETURN:
        data_user["username"] = data["username"]
    elif key == pygame.K_BACKSPACE:
        data["username"] = data["username"][0:-1]
    elif len(data["username"]) <= data["max_characters"]:
        data["username"] += event.unicode
    data["img_username_txt"] = renderizar_valor(data["username"])


# Menu


def analizar_coliciones_menu(state_game:dict, rects:dict, event:pygame.event.Event):
    """
    analiza la coordenada del click con los rects, actualizando si hubo colicion, el estado de la pantalla
    """
    position_click = event.pos

    if rects["play"].collidepoint(position_click):
        state_game["screen_now"] = "playing"

    elif rects["cards"].collidepoint(position_click):
        state_game["screen_now"] = "viewing_cards"

    elif rects["exit"].collidepoint(position_click):
        state_game["running"] = False

def menu_screen(screen:pygame.Surface, state: dict, img:dict, rects:dict, events:list):
    for event in events:

        if event.type == pygame.MOUSEBUTTONDOWN:
            analizar_coliciones_menu(state, rects, event)

    blit_menu_screen(screen, img, rects)

# def movimiento_proyectil(date_proyectil:dict)->:

#   Jugando

def guardar_progreso(ruta:str, data_user)-> dict:
    import json
    with open(ruta, "w") as archivo:
        txt = json.dump(data_user, archivo)
        return txt
    
def leer_datos_usuario(ruta:str)->dict:
    import json
    try:
        with open(ruta,"r") as archivo:
            data_user = json.load(archivo)
    except FileNotFoundError:
        with open(ruta,"w") as archivo:
            data_user = {"username": None,
            "nivel": 0,
            "gold": 0,
            "cards": []}
            json.dump(data_user, archivo)
    return data_user

def get_img(names_img:list, scale:tuple)->dict:
    dict_img = {}
    for name in names_img:
        dict_img[name] = pygame.image.load("Imagenes/" + name + ".png")
        dict_img[name] = pygame.transform.scale(dict_img[name], scale)
    return dict_img


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

def get_ubication_object(object:dict|list, calculos:dict):
    eje_x = calculos["eje_x"]
    eje_y = calculos["eje_y"]
    columnas = calculos["columnas"]
    dx = calculos["dx"]
    dy = calculos["dy"]
    lista_ubication = []
    for i in range(len(object)):
        lista_ubication.append((eje_x,eje_y))
        if (i+1) % columnas == 0:
            eje_x = calculos["eje_x"]
            eje_y += dy
        else:
            eje_x += dx
    tupla_ubication = tuple(lista_ubication)
    return tupla_ubication


def asignar_rects_cards_begin(cards:dict, key_ordenados:list, ubications:list):
    """
    le da lugar a cada carta, su dimencion y su posicion del rect en la pantalla 
    """
    for i in range(len(key_ordenados)):
        dino = key_ordenados[i]
        print(cards[dino])
        cards[dino]["rect"] = cards[dino]["img"].get_rect()
        cards[dino]["rect"].topleft = ubications[i]

def transform_list_a_dict(lista_keys:list, items:dict)->dict:
    dict_cartas = {}
    for key in lista_keys:
        dict_cartas[key] = items[key]
    return dict_cartas
def blit_cards_begin(screen:pygame.Surface,cards:dict):
    """
    Imprime en pantalla de cada carta su imagen en su respectivo rect, ubicacion
    """
    for card in cards:
        if cards[card]["desbloqueado"] == False:
            img_izquierda = pygame.transform.rotate(cards[card]["img"],180)
            screen.blit(img_izquierda, cards[card]["rect"])

def analizar_collidepoint_cartas_begin(cards:dict, data_user:dict,event:pygame.event.Event):
    """
    Analiza si hubo colicion con algun rect de alguna carta del diccionario de cartas
    """
    posicion_click = event.pos
    for card in cards:
        if cards[card]["rect"].collidepoint(posicion_click):
            cards[card]["desbloqueado"] = True
            data_user["cards"].append(card)

def analizar_primeras_cartas(screen:pygame.Surface, initialization:dict, data_cards:dict,data_user:dict, events:list):
    if initialization["begin_cards"]:
        keys_ordenados_random = ordenar_dict_aleatoriamente(data_cards)
        calculos_ubication = get_calculos_ubication((10,10),(210,210),5)
        ubi_rects_cards = get_ubication_object(keys_ordenados_random, calculos_ubication)
        asignar_rects_cards_begin(data_cards, keys_ordenados_random, ubi_rects_cards)
        initialization["begin_cards"] = False
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            analizar_collidepoint_cartas_begin(data_cards, data_user, event)
    blit_cards_begin(screen, data_cards)

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
