import pygame
from inicializaciones import *
from analisis import *
from data import *
pygame.init()

screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("Enciclopedia")

state_game = {"init_game":True,"running":True, "screen_now": "viewing_menu", "update_data": True}
flags = {}
initialization = {"writting":True,"menu" : True, "cards" : True, "begin_cards":True,"playing": True, "options": True}
names_cards = ["diplodocus","iguanodon","velociraptor","torosaurus","triceratops","styracosaurus","gallimimus", "stegosaurus","pachycephalosaurus","carnotaurus","ankilosaurus","parasaurolophus"]
img_cards = get_img(names_cards,(200,200))
data_cards = get_cards_data(img_cards)
data_user = leer_datos_usuario("data_user")

while state_game["running"]:
    events = pygame.event.get()
    analizar_correr_juego(state_game, events)
    screen.blit(fondo_juego,(0,0))

    if state_game["init_game"]:
        if data_user["username"] == None:
            write_screen(screen,initialization, data_user, events)
        elif len(data_user["cards"]) <= 4:
            analizar_primeras_cartas(screen,initialization,data_cards,data_user, events)
        else:
            guardar_progreso("data_user",data_user)
            state_game["init_game"] = False

    elif state_game["screen_now"] == "viewing_menu":

        if initialization["menu"]:

            img_menu = get_img_menu()
            rects_menu = get_rects_menu(img_menu)

            initialization["menu"] = False

        menu_screen(screen, state_game, img_menu, rects_menu, events)


    # elif state_game["screen_now"] == "playing":
    #     if initialization["playing"]:
    #         #img_playing = get_img_playing()
    #         #rects_playing = get_rects_playing(img_playing)
    #         initialization["playing"] = False
    #     if state_game["update_data"]:
    #         #data_playing = get_data_proyectil(img_playing,rects_playing)
    #         #state_game["update_data"] = False
    #         playing_screen(screen,state_game,data_playing, img_playing, rects_playing, events)

    # elif state_game["screen_now"] == "viewing_cards":
        
    pygame.display.flip()
pygame.quit()
