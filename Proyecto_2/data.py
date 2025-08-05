import pygame
from renderizar import *

width_screen = 1200
height_screen = 700
fondo_juego = pygame.image.load("Imagenes/Fondo juego.png")

#   Pantalla escribiendo

def get_data_write()->dict:
    img_username_bg = pygame.image.load("Imagenes/fondo nombre.png")
    img_username_txt = renderizar_valor("Dime tu nombre")
    return{"img_username_txt": img_username_txt,
           "img_username_bg": img_username_bg,
           "username": "",
           "max_characters": 10}

#   Pantalla Jugando

def get_card_data(name:str,vida:int,daño:int,vel_atq:float, desbloqueado:bool)->dict:
    return {"nombre":name,
            "daño":daño,
            "vida":vida,
            "vel_atq":vel_atq,
            "desbloqueado":desbloqueado}

def get_data_logica_cartas()->dict:
    return {
    "diplodocus": get_card_data("diplodocus", 500, 40, 4, False),
    "velociraptor": get_card_data("velociraptor", 700, 50, 2, False),
    "styracosaurus": get_card_data("styracosaurus", 1000, 200, 2.3, False),
    "triceratops": get_card_data("triceratops", 500, 30, 2, False),
    "torosaurus": get_card_data("torosaurus", 600, 60, 3.5, False),
    "gallimimus": get_card_data("gallimimus", 600, 60, 3.5, False),
    "stegosaurus": get_card_data("stegosaurus", 1000, 300, 4, False),
    "ankilosaurus": get_card_data("ankilosaurus", 1200, 200, 4.2, False),
    "parasaurolophus": get_card_data("parasaurolophus", 800, 120, 2.3, False),
    "carnotaurus": get_card_data("carnotaurus", 1200, 230, 3, False),
    "iguanodon": get_card_data("iguanodon", 1300, 300, 3, False),
    "pachycephalosaurus": get_card_data("pachycephalosaurus", 800, 600, 1.4, False)
    }


def get_data_proyectil(img:dict, rects:dict)->dict:
    
    return {"img": img["proyectil"],
            "eje_y": 500,
            "eje_x": 50,
            "rect": rects["proyectil"],
            "invocador": "",
            "exite": False}
