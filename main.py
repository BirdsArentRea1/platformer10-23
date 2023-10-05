import pygame
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
A=0
D=1
W = 2




#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform

#player variables
xpos2 = 500 #xpos of player
ypos2 = 200 #ypos of player
vx2 = 0 #x velocity of player
vy2 = 0 #y velocity of player
keys2 = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround2 = False #this variable stops gravity from pulling you down more when on a platform

while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
            
        
      
        if event.type == pygame.KEYDOWN: #looks for key presses
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            if event.key == pygame.K_a:
                   keys2[a]=True                
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            if event.key == pygame.K_d:
                keys2[d]=True
            if event.key == pygame.K_UP:
                keys[UP]=True
            if event.key == pygame.K_w:
                keys[w]=True
                

        elif event.type == pygame.KEYUP: #looks for key releases
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_w:
                keys2[w]=True
            elif event.key == pygame.K_a:
                keys2[a]=True
            elif event.key == pygame.K_d:
                keys2[d]=True

    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
        
    elif keys[RIGHT]==True:
        vx =+3
    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
    if keys2[a]==True:
        vx=-3
        direction = a
    elif keys2[d]==True:
        vx =+3
    if keys2[w] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = w

    
    #COLLISION
    if xpos>100 and xpos<200 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >550 and ypos+40 <570:
        ypos = 550-40
        isOnGround = True
        vy = 0
    elif xpos>400 and xpos<500 and ypos+40 >450 and ypos+40 <470:
        ypos = 450-40
        isOnGround = True
        vy = 0
    elif xpos>500 and xpos<600 and ypos+40 >350 and ypos+40 <370:
        ypos = 350-40
        isOnGround = True
        vy = 0
    elif xpos>600 and xpos<700 and ypos+40 >250 and ypos+40 <270:
        ypos = 250-40
        isOnGround = True
        vy = 0
    elif xpos>700 and xpos<800 and ypos+40 >150 and ypos+40 <170:
        ypos = 150-40
        isOnGround = True
        vy = 0
    else:
        isOnGround = False


    
    #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
        
    
    if ypos2 > 760:
        isOnGround2 = True
        vy2 = 0
        ypos2 = 760
    
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
    if isOnGround2 == False:
        vy2+=.2

    #update player position
    xpos+=vx 
    ypos+=vy
    
    xpos2+=vx 
    ypos2+=vy
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
  
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 20, 40))
    pygame.draw.rect(screen, (100, 200, 0), (xpos2, ypos2, 20, 40))
    #first platform
    pygame.draw.rect(screen, (200, 0, 10), (100, 750, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, (200, 0, 20), (200, 650, 100, 20))
    pygame.draw.rect(screen, (200, 0, 30), (300, 550, 100, 20))
    pygame.draw.rect(screen, (200, 0, 40), (400, 450, 100, 20))
    pygame.draw.rect(screen, (200, 0, 50), (500, 350, 100, 20))
    pygame.draw.rect(screen, (200, 0, 60), (600, 250, 100, 20))
    pygame.draw.rect(screen, (200, 0, 70), (700, 150, 100, 20))
    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
