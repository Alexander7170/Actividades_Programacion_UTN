import pygame
fuente_opciones = pygame.font.SysFont("Cooper Black", 20)
pygame.init()
pygame.font.init()
lista_nombres_imagenes = ["imagen_texto_cronometro", "imagen_texto_nombre", "imagen_texto_puntuacion"]

# imagen_texto_cronometro = fuente_subtitulos.render(str(cronometro),True,COLOR_NEGRO)
# imagen_texto_nombre = fuente_subtitulos.render("Nombre",True, COLOR_NEGRO)
# imagen_texto_puntuacion = fuente_subtitulos.render("Puntuacion",True, COLOR_NEGRO)
# imagen_texto_nombre_usuario = fuente_subtitulos.render(nombre_usuario,True,COLOR_NEGRO)
# imagen_texto_exit = fuente_pregunta.render("Exit",True, COLOR_NEGRO)
# imagen_texto_jugar = fuente_subtitulos.render("J u g a r", True , COLOR_NEGRO,)
# imagen_texto_score = fuente_subtitulos.render("S c o r e", True, COLOR_NEGRO)
# imagen_texto_salir = fuente_subtitulos.render("S a l i r", True, COLOR_NEGRO)
# imagen_texto_peticion_nombre = fuente_subtitulos.render(MENSAJE_PEDIR_NOMBRE ,True,COLOR_NEGRO)
# imagen_texto_fin_juego = fuente_subtitulos.render(MENSAJE_FIN_PROGRAMA,True,COLOR_NEGRO)

lista_texto_a_renderizar = ["0","nombre","puntuacion"]

def renderizar(nombres_variables:list, texto_renderizar:list, fuente:pygame.font.Font, color:tuple)->list:
    lista_imagenes = []
    for i in range(len(nombres_variables)):
        nombres_variables[i] = fuente.render(texto_renderizar[i],True,color)
        nombres_variables.append(nombres_variables[i])
    return lista_imagenes
print(renderizar(lista_nombres_imagenes,lista_texto_a_renderizar,fuente_opciones,(0,0,0)))