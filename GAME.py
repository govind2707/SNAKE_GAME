# complete code to design a snake game in python

import pygame as GM
import time
import random
GM.init()
D_W=500
D_H=500
#creates a display for the game of required size
DISPLAY=GM.display.set_mode((D_W,D_H))
GM.display.set_caption('SNAKE RAJA')
CLK=GM.time.Clock()
SNK_SIZE=10
SNK_SPEED=15
# a default font of size 30
FONT=GM.font.SysFont(None ,30)
# Displaying the score board
def SCORE(score):
    DISPLAY.blit(FONT.render("SCORE : "+str(score),True,(0,255,0)),[0,0])

# function in order to draw the movement of the snake
def SNK_MOV(SNK_BLK,SNK_LIST):
    for X in SNK_LIST:
        GM.draw.rect(DISPLAY,(255,255,255),[X[0],X[1],SNK_BLK,SNK_BLK])
# the function for the main functionalities of the snake
def GAME():
    COMPLETE=False
    FAIL=False
    X_COR=250
    Y_COR=250
    X_CHANGE=0
    Y_CHANGE=0
    SNK_LIST=[]
    SNK_LENGTH=1
    X_FOOD=round(random.randrange(0,D_W-SNK_SIZE)/10.0)*10.0
    Y_FOOD=round(random.randrange(0,D_H-SNK_SIZE)/10.0)*10.0
    while not COMPLETE:
        # when you failed to play the game
        while FAIL:
            DISPLAY.fill((0,255,0))
            DISPLAY.blit(FONT.render(" FAILED! Press R to replay or Q to QUIT",True,(255,0,0)),[50,50])
            SCORE(SNK_LENGTH-1)
            GM.display.update()

            # Tasked based on the selected options
            for TASKS in GM.event.get():
                if TASKS.type == GM.KEYDOWN:
                    if TASKS.key == GM.K_q:
                        COMPLETE=True
                        FAIL=False
                    elif TASKS.key == GM.K_r:
                        GAME()
                    elif event.type == GM.QUIT:
                        COMPLETE=True
                        FAIL=False
                    else:
                        # other than these two keys if any other key was pressed
                        DISPLAY.blit(FONT.render("INVALID KEY!",True,(255,0,0)),[250,250])
        for TASKS in GM.event.get():
            if TASKS.type==GM.QUIT:
                COMPLETE=True
            if TASKS.type==GM.KEYDOWN:
                if TASKS.key == GM.K_LEFT:
                    X_CHANGE = -SNK_SIZE
                    Y_CHANGE = 0
                elif TASKS.key == GM.K_RIGHT:
                    X_CHANGE = SNK_SIZE
                    Y_CHANGE = 0
                elif TASKS.key == GM.K_UP:
                    Y_CHANGE = -SNK_SIZE
                    X_CHANGE = 0
                elif TASKS.key == GM.K_DOWN:
                    Y_CHANGE = SNK_SIZE
                    X_CHANGE = 0
                else:
                    DISPLAY.blit(FONT.render("NO NO",True,(255,0,0)),[250,250])
                    GM.display.update()
        if X_COR>=D_W or X_COR<0 or Y_COR>=D_H or Y_COR<0:
            FAIL=True
        X_COR+=X_CHANGE
        Y_COR+=Y_CHANGE
        DISPLAY.fill((0,0,0))
        GM.draw.rect(DISPLAY,(0,255,0),[X_FOOD,Y_FOOD,SNK_SIZE,SNK_SIZE])
        SNK_HEAD=[X_COR,Y_COR]
        SNK_LIST.append(SNK_HEAD)
        if len(SNK_LIST)>SNK_LENGTH:
            del SNK_LIST[0]
        for X in SNK_LIST[:-1]:
            if X == SNK_HEAD:
                FAIL =True
        SNK_MOV(SNK_SIZE,SNK_LIST)
        SCORE(SNK_LENGTH-1)
        GM.display.update()
        if X_COR == X_FOOD and Y_COR==Y_FOOD:
            X_FOOD=round(random.randrange(0,D_W-SNK_SIZE)/10.0)*10.0
            Y_FOOD=round(random.randrange(0,D_H-SNK_SIZE)/10.0)*10.0
            SNK_LENGTH+=1
        CLK.tick(SNK_SPEED)
    GM.quit()
    quit()
GAME()
                    
            
