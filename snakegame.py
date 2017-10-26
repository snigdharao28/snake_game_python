# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 23:21:20 2017

@author: SNEHA
"""
#importing
import sys,pygame,time,random

#initializing
cerr = pygame.init()
if cerr[1] > 0:
    print("(!) Had {0} initializing error, exiting...".format(cerr[1]))
    sys.exit(-1)
else:
    print('PyGame successfully initialized')
#play surface
playsur = pygame.display.set_mode((720,460))
#time.sleep(100)
pygame.display.set_caption("Snake Game")    

#colors
red = pygame.Color(255, 0, 0) #gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(165,42,42) #food

#FPS controller
fpsctrl = pygame.time.Clock()

#important variables
snakepos = [100,50]
snakebody = [[100,50],[90,50],[80,50]]

foodpos= [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodspwan = True

direction = 'RIGHT'
changeto = direction

score = 0

def gameover():
    myfont = pygame.font.SysFont('monaco',72)
    GOsurf = myfont.render('GAME OVER!',True,red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360,20)
    playsur.blit(GOsurf,GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit() #pygame window exit
    sys.exit() #console exit
    
def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score) , True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playsur.blit(Ssurf,Srect)
   
#setting keys 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
   #validation of direction             
    if changeto == 'RIGHT'  and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT'  and not direction == 'RIGHT':
        direction = 'LEFT'    
    if changeto == 'UP'  and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN'  and not direction == 'UP':
        direction = 'DOWN'      

#updaing snake co-ordinates(x.y)
    if direction == 'RIGHT':
       snakepos[0] += 10
    if direction == 'LEFT':
       snakepos[0] -= 10
    if direction == 'UP':
       snakepos[1]  -= 10
    if direction == 'DOWN':
       snakepos[1]  += 10

#body mechanism
    snakebody.insert(0,list(snakepos))         
    if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
        score += 1
        foodspwan = False
    else:
        snakebody.pop()
    
    if foodspwan == False:
        foodpos= [random.randrange(1,72)*10,random.randrange(1,46)*10]#set new food position
    foodspwan = True
    
    #to draw snakes
    playsur.fill(white) #background color
   
    for pos in snakebody:
        pygame.draw.rect(playsur,green,pygame.Rect(pos[0],pos[1],10,10))
    
    #to draw food



    pygame.draw.rect(playsur,brown,pygame.Rect(foodpos[0],foodpos[1],10,10))
    
    #to end game when it bangs the walls 
    if snakepos[0] > 710 or snakepos[0]< 0:
            gameover()
    if snakepos[1] > 450 or snakepos[1]< 0:
            gameover()

    #to end game when snake bangs over itself
    for block in snakebody[1:]:
        if snakepos[0] == block[0] and snakepos[1] == block[1]:
            gameover()
            
        
    showScore()    
    pygame.display.flip()#updating
    fpsctrl.tick(15)    
             
            
    

      

