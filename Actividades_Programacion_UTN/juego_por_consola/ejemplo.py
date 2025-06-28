import pygame
import math

# Inicializar Pygame
pygame.init()

# Crear ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colisión con círculo")

# Definir el círculo
circle_center = (400, 300)  # centro del círculo
circle_radius = 100
circle_color = (0, 255, 0)  # verde

# Loop principal
running = True
while running:
    screen.fill((0, 0, 0))  # fondo negro

    # Dibujar el círculo
    pygame.draw.circle(screen, circle_color, circle_center, circle_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detectar clic del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            dx = mouse_pos[0] - circle_center[0]
            dy = mouse_pos[1] - circle_center[1]
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance <= circle_radius:
                print("¡Colisión con el círculo!")
            else:
                print("No hubo colisión")

    pygame.display.flip()

pygame.quit()