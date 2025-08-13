import pygame
from renderizar import *

width_screen = 1200
height_screen = 700
fondo_juego = pygame.image.load("Imagenes/Fondo juego.png")
#   Pantalla Jugando

# def get_card_data(name:str,vida:int,daño:int,vel_atq:float, desbloqueado:bool)->dict:
#     return {"nombre":name,
#             "daño":daño,
#             "vida":vida,
#             "vel_atq":vel_atq,
#             "desbloqueado":desbloqueado}
# def get_data_logica_cartas()->dict:
#     return {
#     "diplodocus": get_card_data("diplodocus", 500, 40, 4, False),
#     "velociraptor": get_card_data("velociraptor", 700, 50, 2, False),
#     "styracosaurus": get_card_data("styracosaurus", 1000, 200, 2.3, False),
#     "triceratops": get_card_data("triceratops", 500, 30, 2, False),
#     "torosaurus": get_card_data("torosaurus", 600, 60, 3.5, False),
#     "gallimimus": get_card_data("gallimimus", 600, 60, 3.5, False),
#     "stegosaurus": get_card_data("stegosaurus", 1000, 300, 4, False),
#     "ankilosaurus": get_card_data("ankilosaurus", 1200, 200, 4.2, False),
#     "parasaurolophus": get_card_data("parasaurolophus", 800, 120, 2.3, False),
#     "carnotaurus": get_card_data("carnotaurus", 1200, 230, 3, False),
#     "iguanodon": get_card_data("iguanodon", 1300, 300, 3, False),
#     "pachycephalosaurus": get_card_data("pachycephalosaurus", 800, 600, 1.4, False)
#     }

def get_data_img_bg(ruta:str, scale:tuple|None, get_rect:bool, ubicacion:tuple):
    imagen = pygame.image.load(ruta)
    rect = None
    if get_rect:
        rect = imagen.get_rect()
        rect.topleft = ubicacion
    if scale != None:
        imagen = pygame.transform.smoothscale(imagen,scale)
    return {"img": imagen,
            "scale": scale,
            "rect": rect,
            "ubicacion":ubicacion}

def get_data_img_txt(txt:str, estilo:dict, obtener_rect:bool, ubicacion:tuple):
    fuente = pygame.font.SysFont(estilo["fuente"],estilo["tamano"])
    img_txt = fuente.render(txt,True,estilo["color"])
    rect = None
    if obtener_rect:
        rect = img_txt.get_rect()
        rect.topleft = ubicacion
    return {"img":img_txt,
            "estilo": estilo,
            "rect": rect,
            "ubicacion": ubicacion}

ESTILOS = get_estilos()

def get_data_proyectil(img:dict, rects:dict)->dict:
    
    return {"img": img["proyectil"],
            "eje_y": 500,
            "eje_x": 50,
            "rect": rects["proyectil"],
            "invocador": "",
            "exite": False}

def leer_datos(ruta:str)->dict:
    import json
    with open(ruta,"r") as archivo:
        texto = json.load(archivo)
    return texto

def leer_datos_juego(ruta:str)->dict:
    import json
    try:
        with open(ruta,"r") as archivo:
            texto = json.load(archivo)
    except FileNotFoundError:
        with open(ruta, "w") as archivo:
            texto = {"usuario_nuevo":{"datos":{"default_name":"Tu Nombre",
                                               "default_cant_cartas":0,
                                                "max_caracteres": 10,
                                               "max_cartas": 8},
                                    "surfaces": get_data_surfaces_user_nuevo()}}
            json.dump(texto, archivo)
    return texto