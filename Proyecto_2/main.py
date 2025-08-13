import pygame
from analisis import *
from data import *
pygame.init()
screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("Enciclopedia")


datos_usuario = leer_datos_usuario("datos_usuario")
config = leer_datos("datos_logicos")
cartas = config["cartas"]
img_cartas = get_img_cartas(cartas)

flujo_juego = {"running":True, "pantalla": 2, "obtener_data": True}
if datos_usuario["username"] == "":
    flujo_juego["pantalla"] = 0
elif datos_usuario["cant_cartas"] == 0:
    flujo_juego["pantalla"] = 1

while flujo_juego["running"]:
    events = pygame.event.get()
    analizar_correr_juego(flujo_juego, events)
    screen.blit(fondo_juego,(0,0))
    if flujo_juego["pantalla"] == 0:
        if flujo_juego["obtener_data"]:
            datos_logicos_p0 = get_datos_logicos_p0(config,datos_usuario)
            datos_visuales_p0 = get_datos_visuales_p0(screen,datos_logicos_p0)
            flujo_juego["obtener_data"] = False
        if datos_logicos_p0["guardo_nombre"]:
            datos_usuario["username"] = datos_logicos_p0["username"]
            guardar_progreso("datos_usuario",datos_usuario)
            flujo_juego["pantalla"] = 1
            flujo_juego["obtener_data"] = True
        else:
            p0(datos_logicos_p0 , datos_visuales_p0, events)
            
    elif flujo_juego["pantalla"] == 1:

        if flujo_juego["obtener_data"]:
            datos_logicos_p1 = get_datos_logicos_p1(config,datos_usuario)
            datos_visuales_p1 = get_datos_visuales_p1(screen,img_cartas,datos_logicos_p1)
            flujo_juego["obtener_data"] = False
        if datos_logicos_p1["guardo_cartas"]:
            datos_usuario["cant_cartas"] = datos_logicos_p1["cant_cartas_user"]
            datos_usuario["desbloqueadas"] = datos_logicos_p1["desbloqueadas"]
            guardar_progreso("datos_usuario",datos_usuario) 
            flujo_juego["pantalla"] = 2
            flujo_juego["obtener_data"] = True
        else:
            p1(datos_logicos_p1, datos_visuales_p1, events)

    elif flujo_juego["pantalla"] == 2:
        if flujo_juego["obtener_data"]: 
            datos_visuales_p2 = get_datos_visuales_p2(screen)
            flujo_juego["obtener_data"] = False
        p2(flujo_juego, datos_visuales_p2, events)

    elif flujo_juego["pantalla"] == 4:
        if flujo_juego["obtener_data"]:
            datos_logicos_p4 = get_datos_logicos_p4(datos_usuario)
            datos_visuales_p4 = get_datos_visuales_p4(screen,img_cartas,datos_logicos_p4)
            flujo_juego["obtener_data"] = False
        p4(datos_visuales_p4, events)
    # elif flujo_juego["screen_now"] == "viewing_cards":
    #     if initialization["viewing_cards"]:
    #         data_img_cards = get_img_cartas(datos_logicos_cartas)
    #         datos_viewing_menu = {"moviendo": False, "distancia": 20}
    #     menu_viewing_cards(screen,data_img_cards,datos_viewing_menu,events)

    # elif flujo_juego["screen_now"] == "playing":
    #     if initialization["playing"]:
    #         #img_playing = get_img_playing()
    #         #rects_playing = get_rects_playing(img_playing)
    #         initialization["playing"] = False
    #     if flujo_juego["update_data"]:
    #         #data_playing = get_data_proyectil(img_playing,rects_playing)
    #         #flujo_juego["update_data"] = False
    #         playing_screen(screen,flujo_juego,data_playing, img_playing, rects_playing, events)


        
    pygame.display.flip()
pygame.quit()
