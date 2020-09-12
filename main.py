import pygame
from pygame.locals import *
import random
import math
import time
from pygame.math import Vector2

white = (255, 255, 255)
black = (0,0,0)
green = (94, 198, 0)
running = True
start = False
pygame.init()

screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)
pygame.display.set_caption("FORM3 BAB5 FORMULA GAME")
clock = pygame.time.Clock()

class TRI():
    def __init__(self,sur,rect):
        self.surr = sur
        self.rect = rect

    def draw_line(position, angle, line_length, line_width, color, screen):
        vector = Vector2()  # A zero vector.
        vector.from_polar((line_length, angle))  # Set the desired length and angle of the vector.
        # Add the vector to the `position` to get the second point.
        pygame.draw.line(screen, color, position, position+vector, line_width)

    def drawTRI():
        x = random.randint(400,550)
        y = random.randint(200,400)
        z = random.randint(1,2)
        angle = random.randint(0,361)
        screen.fill(black)
        coor = [[x,x],[y,x],[x,y]]
        sur = pygame.Surface((500,500))
        sur.set_colorkey(black)
        #tri = pygame.draw.polygon(sur, white, ((x,x),(y,x),(x,y)))
        pygame.draw.circle(sur, green, coor[z], 30, True)
        rect = sur.get_rect()  
        rect.center = (800 // 2 , 600 // 2) 
        screen.blit(sur, (0,0))
        #tri = pygame.draw.polygon(screen, white, ((400,400),(360,400),(400,360)))
        a = pygame.draw.line(sur, white, (x,x), (y,x))
        b = pygame.draw.line(sur, white, (y,x), (x,y))
        c = pygame.draw.line(sur, white, (x,y), (x,x))
        #screen.set_clip(tri)
        if coor == 1:
            ad = [[x,y],[x,x]]
            op = [[y,x],[x,y]]
            hy = [[x,x],[y,x]]
        else:
            ad = [[y,x],[x,y]]
            op = [[x,x],[y,x]]
            hy = [[x,y],[x,x]]
        print(ad,op,hy,"z:",coor[z])
        #pygame.draw.circle(screen, white, coor[z], 25)
        #pygame.draw.polygon(screen, white, ((300,400),(400,500),(500,350)))
        return sur

    def rotate(surr):
        angle = random.randint(0,361)
        ro = pygame.transform.rotate(surr, angle)
        screen.blit(ro, (800/2,600/2))
 

while running:
    for event in pygame.event.get():
        if pygame.mouse.get_pressed() == (1,0,0):
            pass
            surr = TRI.drawTRI()
            TRI.rotate(surr)
        if start == False: 
            TRI.drawTRI()
            pygame.display.update()
            start = True
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == VIDEORESIZE:
            global w, h
            w = event.w
            h = event.h
            print(f"[{w},{h}]")
            '''
        elif event.type == MOUSEBUTTONDOWN:
            mouse_position_start = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP:
            mouse_position_end = pygame.mouse.get_pos() 
            pygame.draw.line(screen, white, mouse_position_start, mouse_position_end, 1)
            #time.sleep(2)'''
            '''
            surr = TRI.drawTRI()
            TRI.rotate(surr)
            screen.fill(black)'''
            #math. sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))
    pygame.display.update()
    clock.tick(30)