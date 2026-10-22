import pygame
import math

GRON = (0,255,0)
SVART = (0,0,0)
START = (400,450)
SKALA = 2



def koordinater(distans, vinkel): 
    alpha = math.radians(vinkel)
    x = START[0] - SKALA * distans * math.cos(alpha)
    y = START[1] - SKALA * distans * math.sin(alpha)
    return x, y

def design(skarm):
    skarm.fill((0,0,0))
    
    pygame.draw.arc(skarm, GRON, (385, 435, 30, 30), 0 , math.pi, 15)
    pygame.draw.line(skarm, GRON, (0, 450), (800, 450), 2)
    pygame.draw.line(skarm, GRON, START, (400 + 400*math.cos(math.pi - math.radians(22.5)), 450 + 400*math.sin(-1*math.radians(22.5))), 2)
    pygame.draw.line(skarm, GRON, START, (400 + 400*math.cos(math.radians(22.5)), 450 + 400*math.sin(-1*math.radians(22.5))), 2)
    pygame.draw.line(skarm, GRON, START, (400 + 400*math.cos(math.pi - 2*math.radians(22.5)), 450 + 400*math.sin(-2*math.radians(22.5))), 2)
    pygame.draw.line(skarm, GRON, START, (400 + 400*math.cos(2*math.radians(22.5)), 450 + 400*math.sin(-2*math.radians(22.5))), 2)
    pygame.draw.line(skarm, GRON, START, (400 + 400*math.cos(math.pi - 3*math.radians(22.5)), 450 + 400*math.sin(-3*math.radians(22.5))), 2)
    pygame.draw.line(skarm, GRON, START, (400 + 400*math.cos(3*math.radians(22.5)), 450 + 400*math.sin(-3*math.radians(22.5))), 2)
    pygame.draw.line(skarm, GRON, START, (400, 50), 2)
    pygame.draw.arc(skarm, GRON, (0, 50, 800, 800), 0, math.pi, 2)    # 200 cm i verkligheten (MAX)
    pygame.draw.arc(skarm, GRON, (320, 370, 160, 160), 0, math.pi, 2 )  #40cm i verkligheten
    pygame.draw.arc(skarm, GRON, (80, 130, 640, 640), 0, math.pi, 2 ) #160 cm i verklighten
    pygame.draw.arc(skarm, GRON, (240, 290, 320, 320), 0, math.pi, 2 ) #80 cm i verklighten


def rita_bild(skarm, slutpunkt, matpunkter, nu):
    pulsradie = 5 + 2 * math.sin(2 * math.pi * nu / 1000)
    design(skarm)
    pygame.draw.line(skarm, GRON, START, (round(slutpunkt[0]), round(slutpunkt[1])), 5)
    for punkt_x, punkt_y, upptacktstid in matpunkter:
        pygame.draw.circle(skarm, GRON, (round(punkt_x), round(punkt_y)), round(pulsradie))
