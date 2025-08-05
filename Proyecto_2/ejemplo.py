import pygame
from analisis import *
from data import *
from renderizar import *
pygame.init()
pantalla = pygame.display.set_mode((1200,800))
lanzo = False
flag = True
img_proyectil = pygame.image.load("Imagenes/proyectil.png")
def get_rects_cartas(dimencion:pygame.Surface, ubicacion:list)->list:
    lista_rects = []
    for ubicacion in ubicacion:
        rect = dimencion.get_rect()
        rect.topleft = ubicacion
        lista_rects.append(rect)
    return lista_rects

def get_datos_visuales_cartas(datos_logicos, img_bg:dict, img_txt:dict, rects:list):
    datos_visuales = {}
    for carta in datos_logicos:
        carta = "img_bg": img
        
def get_img_cartas(datos_logicos:dict)->dict:
    img_bg = pygame.image.load("Imagenes/carta.png")
    names_cards = ["diplodocus","iguanodon","velociraptor","torosaurus","triceratops","styracosaurus","gallimimus", "stegosaurus","pachycephalosaurus","carnotaurus","ankilosaurus","parasaurolophus"]
    img_fotos = get_img(names_cards,(200,200))
    estilos = get_estilos()
    img_txt = get_img_txt_dict(datos_logicos, estilos["cartas"],["daño","nombre","vida","vel_atq"])
    calculos = get_calculos_ubication((10,10),(200,200),6)
    ubi_img_bg = get_ubication_object(img_txt,calculos)
    rects = get_rects_cartas(img_bg,ubi_img_bg)
    print()
    return get_datos_visuales_cartas()
data_logica_cartas = get_data_logica_cartas()

estilos = get_estilos()

resultado = get_img_cartas(data_logica_cartas)

# while flag:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             flag = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:
#                 lanzo = True
#     pantalla.fill((200,200,200))

#     pygame.display.flip()
    