
ANCHO_VENTANA = 900
ALTO_VENTANA = 700
FPS = 60
TIEMPO_MAXIMO = 7
MAXIMO_CARACTERES = 10
COLOR_NEGRO = (0,0,0)
COLOR_BLANCO = (255,255,255)
cronometro = 0
nombre_usuario = ""
opcion_usuario = ""
PUNTO_DE_PARTIDA = 15
MOVERSE_RESPUESTA_CORRECTA = 1
MOVERSE_RESPUESTA_INCORRECTA = 1
CLAVE_RESPUESTA_CORRECTA = "respuesta_correcta"
TABLERO =  [0,0,1,0,2,0,1,1,0,0,0,2,0,1,0,0,1,1,1,0,2,0,3,0,1,0,1,2,0,0,0]

#claves
ESCRIBIENDO_NOMBRE = "clave_escribiendo_nombre"
VIENDO_MENU = "clave_viendo_menu"
VIENDO_SCORE = "clave_viendo_score"
CORRER_JUEGO = "clave_correr_juego"
JUGANDO = "clave_jugando"

IMAGEN_FONDO = "clave_imagen_fondo"
IMAGEN_TEXTO = "clave_imagen_texto"
UBICACION_FONDO = "clave_ubicacion_fondo"
UBICACION_TEXTO = "clave_ubicacion_texto"
import pygame
pygame.init()
fuente_grande = pygame.font.SysFont("Comic Sans MS",40)
fuente_mediana = pygame.font.SysFont("Comic Sans MS",30)
fuente_pequeña = pygame.font.SysFont("Arial", 20)