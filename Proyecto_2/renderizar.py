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
    return {"cartas":{"fuente": pygame.font.SysFont("Arial",70),"color":(0,0,0)}}

def get_img_txt_dict(dict_anidados:dict, estilo:dict, lista_keys:list)->dict:
    imagenes = {}
    for elemento_d in dict_anidados:
        img_values = {}
        for key in lista_keys:
            txt = key + " : " + str(dict_anidados[elemento_d][key])
            img_values[key] = estilo["fuente"].render(txt, estilo["color"],False)
        imagenes[elemento_d] = img_values
    return imagenes

