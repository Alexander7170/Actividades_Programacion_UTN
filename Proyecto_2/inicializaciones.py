import pygame

#   PANTALLA MENU
def get_img_menu()->dict:
    """
    Carga las imagenes nesesarias para esa pantalla.
    Devuelve un diccionario, con claves de la imagen guardada en su valor
    """
    img_play = pygame.image.load("Imagenes/boton_jugar.png")
    img_cards = pygame.image.load("Imagenes/boton_almacen.png")
    img_exit = pygame.image.load("Imagenes/boton_salir.png")
    return {"play":img_play,"cards":img_cards, "exit": img_exit}

def get_rects_menu(img:dict)->dict:
    """
    Obtiene el tamaño de los rect necesarios para la esa pantalla.
    Tambien los ubica en la pantalla
    """
    rect_play = img["play"].get_rect()
    rect_cards = img["cards"].get_rect()
    rect_exit = img["exit"].get_rect()
    rect_play.topleft = (300,200)
    rect_cards.topleft = (300,400)
    rect_exit.topleft = (300,600)
    return {"play":rect_play, "cards":rect_cards, "exit":rect_exit}

#   PANTALLA JUGANDO


def get_img_playing()->dict:
    """
    carga las imagenes nesesarias para esa pantalla.
    Devuelve un diccionario, con claves de la imagen guardada en su valor
    """
    img_proyectil = pygame.image.load("Imagenes/proyectil.png")
    img_carta = pygame.image.load("Imagenes/carta.png")
    img_carta = pygame.transform.scale(img_carta,(170,170))
    img_exit = pygame.image.load("Imagenes/exit.png")
    return{"proyectil": img_proyectil, "carta":img_carta, "exit": img_exit}

def get_rects_playing(img:dict)->dict:
    """
    Obtiene el tamaño de los rect necesarios para la esa pantalla.
    Tambien los ubica en la pantalla
    """
    rect_proyectil = img["proyectil"].get_rect()
    rect_carta_user_r = img["carta"]. get_rect()
    rect_carta_user_c = img["carta"]. get_rect()
    rect_carta_user_l = img["carta"]. get_rect()
    rect_carta_enemy_r = img["carta"]. get_rect()
    rect_carta_enemy_c = img["carta"]. get_rect()
    rect_carta_enemy_l = img["carta"]. get_rect()
    rect_exit = img["exit"].get_rect()
    rect_carta_enemy_r.topleft = (850,10)
    rect_carta_enemy_c.topleft = (450,10)
    rect_carta_enemy_l.topleft = (50,10)
    rect_carta_user_r.topleft = (850,500)
    rect_carta_user_c.topleft = (450,500)
    rect_carta_user_l.topleft = (50,500)
    return {"proyectil": rect_proyectil, 
            "carta_user_r": rect_carta_user_r,
            "carta_user_c": rect_carta_user_c,
            "carta_user_l": rect_carta_user_l,
            "carta_enemy_r": rect_carta_enemy_r,
            "carta_enemy_c": rect_carta_enemy_c,
            "carta_enemy_l": rect_carta_enemy_l,
            "rect_exit": rect_exit}

