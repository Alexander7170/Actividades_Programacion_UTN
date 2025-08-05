import pygame

def blit_write_screen(screen:pygame.Surface, dates:dict):
    screen.blit(dates["img_username_bg"],(340,0))
    screen.blit(dates["img_username_txt"],(400,200))
    
def blit_menu_screen(screen:pygame.Surface, img:dict, rects:dict):
    screen.blit(img["play"],rects["play"])
    screen.blit(img["cards"],rects["cards"])
    screen.blit(img["exit"], rects["exit"])

def blit_playing_screen(screen:pygame.Surface, data:dict, img:dict, rects:dict):
    if data["existe"]:
        screen.blit(img["proyectil"], rects["proyectil"])
    screen.blit(img["carta"],rects["carta_user_r"])
    screen.blit(img["carta"],rects["carta_user_c"])
    screen.blit(img["carta"],rects["carta_user_l"])
    screen.blit(img["carta"],rects["carta_enemy_r"])
    screen.blit(img["carta"],rects["carta_enemy_c"])
    screen.blit(img["carta"],rects["carta_enemy_l"])