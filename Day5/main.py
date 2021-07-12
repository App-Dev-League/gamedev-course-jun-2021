#sound download link: https://www.soundjay.com/beep-sounds-1.html

###global variables
x = 1
print(x)#x is already global because it is defined outside of functions

def func():
   x = 1
func()
print(x) #causes error because x is only defined within the scopt of func()

def func():
   global x
   x = 1
func()
print (x)

def func2():
   print(x)
func2()

#pygame examples

import pygame
import time as t
from pygame import *
pygame.init()
screen = pygame.display.set_mode((500,500))

go = True

while go:
    screen.fill((255,0,0)) #red screen
    
    #fonts
    font = pygame.font.Font('freesansbold.ttf', 16)
    font_render = font.render('Hello World', 1, (0,0,0))
    fontRect = font_render.get_rect()
    fontRect.topleft = (100, 100)
    screen.blit(font_render,fontRect)

    #sounds - doesn't work in REPL.it
    beep = pygame.mixer.Sound('sound96.wav')
    beep.play()
    t.sleep(2)
    beep.stop()

    #convert_alpha
    sur = pygame.Surface((500,500))
    sur.fill((0,255,0))
    sur = sur.convert_alpha()
    screen.blit(sur, (0,0))

    #Clock
    clock = pygame.time.Clock()
    clock.tick(1) #changes how quickly the main loop runs (one frame every x seconds)
    
    
    pygame.display.update()
    
