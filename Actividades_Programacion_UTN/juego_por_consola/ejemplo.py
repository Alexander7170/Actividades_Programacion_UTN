import pygame
pygame.init()

# Configuración
ANCHO = 700
ALTO = 500
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Escribí tu nombre")

# Fuente para mostrar texto
fuente = pygame.font.SysFont("arial", 32)

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Variables
escribiendo = True
nombre = ""

while escribiendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            escribiendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                print(f"Nombre ingresado: {nombre}")
                escribiendo = False
            elif evento.key == pygame.K_BACKSPACE:
                nombre = nombre[:-1]
            else:
                nombre += evento.unicode

    # Dibujar en pantalla
    pantalla.fill(BLANCO)
    texto_superior = fuente.render("Decime tu nombre:", True, NEGRO)
    texto_nombre = fuente.render(nombre, True, NEGRO)
    pantalla.blit(texto_superior, (50, 100))
    pantalla.blit(texto_nombre, (50, 150))

    pygame.display.flip()

pygame.quit()