import pygame
pygame.init()
fuente_grande = pygame.font.SysFont("Arial",60)
fuente_mediana = pygame.font.SysFont("Arial",50)
fuente_chica = pygame.font.SysFont("Arial",40)
COLOR_NEGRO = (0,0,0)
COLOR_BLANCO = (255,255,255)

def renderizar_valor(texto:str)->pygame.Surface:
    imagen_texto = fuente_grande.render(str(texto),True,COLOR_BLANCO)
    return imagen_texto

def get_estilos()->dict:

    return {"cartas":{"fuente": "Verdana", "tamano":17,"color":COLOR_NEGRO},
            "menu": {"fuente": pygame.font.SysFont("Verdana", 30), "color": COLOR_NEGRO},
            "nombre":{"fuente": "Verdana","tamano": 35,"color": COLOR_NEGRO}}

def renderizar_una_carta(datos_logicos:dict, estilo:dict)->dict:
    imagenes = {}
    print(datos_logicos)
    fuente_largo = pygame.font.SysFont(estilo["fuente"], estilo["tamano"]-5)
    fuente = pygame.font.SysFont(estilo["fuente"],estilo["tamano"]) 
    imagenes["txt_nombre"] = fuente.render("Nombre: "+ datos_logicos["nombre"],estilo["color"],False)
    imagenes["txt_atk"] = fuente.render("Daño: " + str(datos_logicos["atk"]),estilo["color"],False)
    imagenes["txt_hp"] = fuente.render("Vida: "+ str(datos_logicos["hp"]),estilo["color"],False)
    imagenes["txt_vel_atk"] = fuente_largo.render("Velocidad ATK: "+ str(datos_logicos["vel_atk"]),estilo["color"],False)
    return imagenes

def renderizar_cartas(datos_logicos:dict, estilo:dict)->dict:
    datos_visuales = {}
    for id in datos_logicos:
        datos_visuales[id] = renderizar_una_carta(datos_logicos[id],estilo)
    return 