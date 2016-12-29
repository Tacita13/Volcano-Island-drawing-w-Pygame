"""
Isamar López Rodríguez
9/11/15
"""
 
import pygame
import math
import random


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKYBLUE = (196, 239, 242)
ORANGE =(250, 127, 50)
BROWN = (117, 41, 19)
SAND = (242, 191, 141)
DEEPGREEN = (77, 150, 50)
SEABLUE = (141, 213, 242)
PALMS = (245, 203, 17)
SMOKE =(201, 209, 212)
 
pygame.init()
PI = 3.141592653

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Volcano island")
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(SAND)

############-------DRAWING------#################
    
# Draws the sea and waves
    pygame.draw.rect(screen, SEABLUE, [0,360,700,200], 0)
    for xOffset in range(0,1000, 30):
            pygame.draw.arc(screen, WHITE,   [0+xOffset,350,30,30],PI/2,   PI, 12)
            pygame.draw.arc(screen, WHITE,  [0+xOffset,350,30,30],    0, PI/2, 12)

# Draws the sky
    pygame.draw.rect(screen, SKYBLUE, [0,0,700,150], 0)

# Draws the mountains
    for xOffset in range(0, 500, 130):
        pygame.draw.polygon(screen, DEEPGREEN, [[150+xOffset,50], [0+xOffset,150], [300+xOffset,150]], 0)

# Draws the volcano, lava and smoke
    pygame.draw.polygon(screen, BROWN, [[350,50], [250,150], [450,150]], 0)  
    pygame.draw.polygon(screen, ORANGE, [[350,50], [325,75], [375,75]], 0)
    pygame.draw.polygon(screen, SMOKE, [[350,50], [315, 0], [385,0]], 0)
    pygame.draw.rect(screen, SMOKE, [0,0,700,10], 0)

    for xOffset in range(0,1000, 30):
        pygame.draw.arc(screen, SMOKE,   [0+xOffset,-15,30,30],3*PI/2,   2*PI, 10)
        pygame.draw.arc(screen, SMOKE,  [0+xOffset,-15,30,30],    PI, 3*PI/2, 10)


# Draws the huts
    for xOffset in range(0, 600, 150): 
        pygame.draw.rect(screen, PALMS, [80+xOffset,200,80,90], 0)
        pygame.draw.polygon(screen, PALMS, [[120+xOffset,150], [50+xOffset,220], [190+xOffset,220]], 0)
        pygame.draw.rect(screen, BROWN, [101+xOffset,240,40,50], 0)

        pygame.draw.line(screen, BROWN, [120+xOffset, 150], [170+xOffset, 210], 2)    
        pygame.draw.line(screen, BROWN, [120+xOffset, 150], [150+xOffset, 210], 2)
        pygame.draw.line(screen, BROWN, [120+xOffset, 150], [130+xOffset, 210], 2)
        pygame.draw.line(screen, BROWN, [120+xOffset, 150], [110+xOffset, 210], 2)
        pygame.draw.line(screen, BROWN, [120+xOffset, 150], [90+xOffset, 210], 2)
        pygame.draw.line(screen, BROWN, [120+xOffset, 150], [70+xOffset, 210], 2)

#############-------DRAWING------#################
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
