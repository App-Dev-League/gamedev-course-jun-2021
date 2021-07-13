import random, sys, time, pygame
from pygame.locals import *

#global declarations
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FLASHSPEED = 500 #in milliseconds
FLASHDELAY = 200
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4

#Colors
#        R, G, B
WHITE = (255,255,255)
BLACK = (0,0,0)
BRIGHTRED = (255,0,0) 
RED = (155,0,0)
BRIGHTGREEN = (0,255,0)
GREEN = (0,155,0)
BRIGHTBLUE = (0,0,255)
BLUE = (0,0,155)
BRIGHTYELLOW = (255,255,0)
YELLOW = (155,155,0)
DARKGRAY = (40,40,40)
bgColor = BLACK

XMARGIN = int((WINDOWWIDTH - (2*BUTTONSIZE) - BUTTONGAPSIZE)/2)
YMARGIN = int((WINDOWHEIGHT - (2*BUTTONSIZE) - BUTTONGAPSIZE)/2)

YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)

BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)

REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)

GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)

def main():
  global FPSCLOCK, DISPLAYSURF, BASICFONT
  pygame.init() 
  FPSCLOCK = pygame.time.Clock()
  DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
  pygame.display.set_caption("Simulate")
  BASICFONT = pygame.font.Font("freesansbold.ttf", 16)
  infoSurf = BASICFONT.render("Match the pattern by clicking on the buttons", 1, DARKGRAY)
  infoRect = infoSurf.get_rect()
  infoRect.topleft = (10,WINDOWHEIGHT - 25)
  
  #local variables
  pattern = [] #stores the pattern for the Colors
  currentStep =  0 #color that the player has to push next
  lastClickTime = 0 #monitor the players last click time
  score = 0
  #if false, the pattern is playing, if true, we are waiting for t he player to click
  waitingForInput = False

  while True:
    clickedButton = None
    DISPLAYSURF.fill(bgColor)
    drawButtons()

    scoreSurf = BASICFONT.render('Score ' + str(score), 1, WHITE)

    scoreRect = scoreSurf.get_rect()

    scoreRect.topleft = (WINDOWWIDTH - 100, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

    DISPLAYSURF.blit(infoSurf, infoRect)

    checkForQuit()
    for event in pygame.event.get():
      if event.type == MOUSEBUTTONUP:
        mousex, mousey = event.pos
        clickedButton = getButtonClicked(mousex, mousey)

    if not waitingForInput:
        pygame.display.update
        pygame.time.wait(1000)
        pattern.append(random.choice((YELLOW,BLUE, RED, GREEN)))
        for button in pattern:
          flashButtonAnimation(button)
          pygame.time.wait(FLASHDELAY)
          waitingForInput = True
  else:
    #wait for the player to enter Buttons 
    if clickedButton and clickButton == pattern[current_step]:
      flashButtonAnimation(clickedButton)
      currentStep+=1
      lastClickTime = time.time()
    if currentStep == len(pattern):
      changeBackgroundAnimation()
      score+=1
      waitingForInput = False
      currentStep = 0
    elif (clickButton and clickedButton!=pattern[currentStep]) or (current_step!=0 and time.time() - TIMEOUT > lastClickTime):
      gameOverAnimation()
      #reset the variables for a new game 
      pattern = []
      currentStep =  0
      waitingForInput = False 
      score = 0
      pygame.time.wait(1000)
      changeBackgroundAnimation()
    pygame.display.update()
    FPSCLOCK.tick(FPS)


def terminate():
  pygame.quit() 
  sys.exit()


def checkForQuit():
  for event in pygame.event.get(QUIT):
    terminate()
  for event in pygame.event.get(KEYUP):
    if event.key == K_ESCAPE:
      terminate()
    pygame.event.post(event)

def flashButtonAnimation(color, animationSpeed = 50):
  if color == YELLOW:
    flashColor = BRIGHTYELLOW 
    rectangle = YELLOWRECT 
  elif color == BLUE:
    flashColor = BRIGHTBLUE
    rectangle = BLUERECT
  elif color == RED:
    flashColor = BRIGHTRED
    rectangle = REDRECT 
  elif color == GREEN:
    flashColor = BRIGHTGREEN
    rectangle = GREENRECT 
  origSurf = DISPLAYSURF.copy()
  flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))

  flashSurf =  flashSurf.convert_alpha()
  r,g,b = flashColor

  for start, end, step in ((0,255,1),(255,0,-1)):
    for alpha in range(start, end, animationSpeed*step):
      checkForQuit()
      DISPLAYSURF.blit(origSurf, (0,0))
      flashSurf((r,g,b,a))
      DISPLAYSURF.blit(flashSurf, rectangle.topleft)
      pygame.display.update()
      FPSCLOCK.tick(FPS)
  DISPLAYSURF.blit(origSurf, (0 ,0))
  

