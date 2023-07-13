import pygame
pygame.mixer.init()

ANCHO_VENTANA = 1500
ALTO_VENTANA = 800
GROUND_LEVEL = 700
FPS = 60

SCORE_POSITION = (100,80)

DIRECTION_L = 0
DIRECTION_R = 1
GROUND_COLLIDE_H = 8
GROUND_RECT_H = 10
DEBUG = False

TIME_DAMAGE = 2000

# COLOR CONSTANTS
C_RED = (255,0,0)
C_GREEN = (0,255,0)
C_BLUE = (0,0,255)
C_BLACK = (0,0,0)
C_WHITE = (255,255,255)
C_PINK = (255, 0, 160)
C_PEACH = (255, 118, 95)
C_BLUE_2 = (38, 0, 160)
C_YELLOW_2 = (255, 174, 0)
C_GREEEN_2 = (38, 137, 0)
C_ORANGE = (255, 81, 0)

# MOUSE CONSTANTS
M_STATE_NORMAL = 0
M_STATE_HOVER = 1
M_STATE_CLICK = 3
M_BRIGHT_HOVER = (32,32,32)
M_BRIGHT_CLICK = (32,32,32)

# SOUNDS
ADV_ATTACK = pygame.mixer.Sound(r"recursos\sounds\blaster.mp3")
ADV_JUMP = pygame.mixer.Sound(r"recursos\sounds\jump.wav")
ADV_HURTED = pygame.mixer.Sound(r"recursos\sounds\hurted_r2d2.mp3")
ENEMY_ATTACK = pygame.mixer.Sound(r"recursos\sounds\blaster.mp3")
ENEMY_HURTED = pygame.mixer.Sound(r"recursos\sounds\batle_droid_death.mp3")
BOSS_ATTACK = pygame.mixer.Sound(r"recursos\sounds\grievous_attack.mp3")
BOSS_HURTED = pygame.mixer.Sound(r"recursos\sounds\grievous_death.mp3")
BOSS_DIED = pygame.mixer.Sound(r"recursos\sounds\grievous_death.mp3")