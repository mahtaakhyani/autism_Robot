import dyna
import pygame
import time
 


pygame.init()
pygame.font.init() 
              
width, height = 64*10, 64*8
screen=pygame.display.set_mode((width, height))
screen.fill((255,255,255))


mot = dyna.motors()

speed = 250
pos_up = 530
pos_right = 500
right_hand = 200
left_hand = 874
foot_move = False 
while 1:

    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 
        if event.type == pygame.KEYDOWN:
            # if event.key==pygame.K_UP:
            #     mot.move(speed,90,0)
            #     foot_move = True
            # elif event.key==pygame.K_LEFT:
            #     mot.move(speed,0,0)
            #     foot_move = True
            # elif event.key==pygame.K_DOWN:
            #     mot.move(speed,270,0)
            #     foot_move = True
            # elif event.key==pygame.K_RIGHT:
            #     mot.move(speed,180,0)  
            #     foot_move = True          
            if event.key==pygame.K_KP8:
                pos_up = mot.constrain(pos_up + 5,445,600)
                mot.head(pos_up,0)
                foot_move = False
            elif event.key==pygame.K_KP2:
                pos_up = mot.constrain(pos_up - 5,445,600)
                mot.head(pos_up,0)
                # mot.head2(-300) 
                foot_move = False          
            elif event.key==pygame.K_KP7:
                pos_right = mot.constrain(pos_right + 5,220,780)
                mot.head(pos_right,1)
                foot_move = False
            elif event.key==pygame.K_KP9:
                pos_right = mot.constrain(pos_right - 5,220,780)
                mot.head(pos_right,1)
                foot_move = False
            # elif event.key==pygame.K_KP6:
            #     mot.move(0,0,speed-50)
            #     foot_move = True
            # elif event.key==pygame.K_KP4:
            #     mot.move(0,0,-speed+50)
            #     foot_move = True
            elif event.key==pygame.K_F1:
                right_hand = mot.constrain(right_hand + 200,10,1020)
                mot.hand(right_hand,0)
            elif event.key==pygame.K_F2:
                right_hand = mot.constrain(right_hand - 200,10,1020)
                mot.hand(right_hand,0)
            elif event.key==pygame.K_F5:
                left_hand = mot.constrain(left_hand - 200,10,1020)
                mot.hand(left_hand,1)
            elif event.key==pygame.K_F6:
                left_hand = mot.constrain(left_hand + 200,10,1020)
                mot.hand(left_hand,1)
 
        if event.type == pygame.KEYUP:
            
            mot.stop_motors()



